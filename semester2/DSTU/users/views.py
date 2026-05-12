import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm
from .models import Teacher, TeacherInfo
from django.http import HttpResponse
import os
from DSTU.settings import BASE_DIR

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Добро пожаловать, {user.username}!')
            logger.info(f"User {user.username} registered successfully")
            return render(request, "index.html")
        else:
            logger.warning(f"Registration validation failed: {form.errors}")
            for field, errors in form.errors.items():
                for error in errors:
                    logger.warning(f"Registration error - Field '{field}': {error}")
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'С возвращением, {user.username}!')
                logger.info(f"User {username} logged in successfully")
                return render(request, "index.html")
            else:
                logger.warning(f"Failed login attempt for username: {username}")
                messages.error(request, 'Неверное имя пользователя или пароль.')
        else:
            logger.warning(f"Login form validation failed: {form.errors}")
            messages.error(request, 'Ошибка в форме. Проверьте правильность ввода.')
    else:
        form = LoginForm(request)
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    username = request.user.username if request.user.is_authenticated else 'Unknown'
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    logger.info(f"User {username} logged out")
    return redirect('users:login')


@login_required
def profile(request, username):
    """Просмотр профиля пользователя"""
    # Защита от неправильных username
    if username in ['edit', 'create', 'delete', 'update']:
        return redirect('users:profile_edit')
    
    viewed_user = get_object_or_404(Teacher, username=username)
    
    # Получаем или создаем TeacherInfo
    viewed_info = viewed_user.info
    
    # Получаем или создаем TeacherInfo для текущего пользователя
    current_info = request.user.info
    
    is_self = request.user == viewed_user
    is_friend = False
    
    if current_info and viewed_info and not is_self:
        is_friend = current_info.is_friend(viewed_info)
    
    can_view = is_self or is_friend
    
    if not can_view:
        messages.error(request, 'У вас нет доступа к этому профилю. Только друзья могут просматривать профили.')
        return redirect('users:users_list')
    
    context = {
        'profile_user': viewed_user,
        'profile_info': viewed_info,
        'is_friend': is_friend,
        'is_self': is_self,
    }
    
    return render(request, 'registration/profile.html', context)


# views.py
@login_required
def profile_edit(request):
    """Редактирование профиля"""
    # Убеждаемся, что профиль существует
    profile = request.user.info
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            # Сохраняем форму пользователя
            user = u_form.save()
            
            # Сохраняем форму профиля
            profile = p_form.save(commit=False)
            profile.teacher = user
            profile.save()
            
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('users:profile', username=request.user.username)
        else:
            messages.error(request, 'Ошибка при обновлении профиля. Проверьте введенные данные.')
            # Выводим ошибки форм для отладки
            print(u_form.errors)
            print(p_form.errors)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'registration/profile_edit.html', context)


# views.py - полная версия без использования id
@login_required
def users_list(request):
    """Список друзей текущего пользователя"""
    try:
        current_info = request.user.info
        friends = current_info.get_friends()
    except TeacherInfo.DoesNotExist:
        current_info = TeacherInfo.objects.create(
            teacher=request.user,
            phone=''
        )
        friends = []
    
    context = {
        'friends': friends,
        'title': 'Мои друзья'
    }
    return render(request, 'registration/users_list.html', context)


@login_required
def all_users_list(request):
    """Список всех пользователей (кроме себя) для добавления в друзья"""
    # Получаем всех пользователей кроме текущего
    all_users = Teacher.objects.exclude(id=request.user.id)
    
    # Получаем друзей текущего пользователя
    try:
        current_info = request.user.info
        friends = current_info.get_friends()
        # Создаем список username друзей для быстрой проверки
        friends_usernames = [friend.teacher.username for friend in friends]
    except TeacherInfo.DoesNotExist:
        current_info = TeacherInfo.objects.create(
            teacher=request.user,
            phone=''
        )
        friends_usernames = []
    
    # Создаем список с информацией о дружбе
    users_data = []
    for user in all_users:
        try:
            user_info = user.info
            # Проверяем, является ли пользователь другом по username
            is_friend = user.username in friends_usernames
        except TeacherInfo.DoesNotExist:
            user_info = None
            is_friend = False
        
        users_data.append({
            'user': user,
            'info': user_info,
            'is_friend': is_friend,
        })
    
    context = {
        'users_data': users_data,
        'title': 'Все пользователи'
    }
    return render(request, 'registration/all_users.html', context)


@login_required
def add_friend(request, username):
    """Добавление в друзья"""
    try:
        # Получаем профиль текущего пользователя
        try:
            from_user = request.user.info
        except TeacherInfo.DoesNotExist:
            from_user = TeacherInfo.objects.create(
                teacher=request.user,
                phone=''
            )
        
        # Получаем пользователя, которого добавляем
        to_user = get_object_or_404(Teacher, username=username)
        
        try:
            to_info = to_user.info
        except TeacherInfo.DoesNotExist:
            to_info = TeacherInfo.objects.create(
                teacher=to_user,
                phone=''
            )
        
        # Проверяем, не пытается ли пользователь добавить себя
        if from_user.teacher.id == to_user.id:
            logger.warning(f"User {request.user.username} tried to add themselves as friend")
            messages.error(request, 'Нельзя добавить самого себя')
        elif from_user.add_friend(to_info):
            logger.info(f"User {request.user.username} added {to_user.username} as friend")
            messages.success(request, f'{to_user.username} добавлен в друзья!')
        else:
            logger.warning(f"User {request.user.username} tried to add {to_user.username} who is already a friend")
            messages.warning(request, f'{to_user.username} уже в друзьях')
    except Exception as e:
        logger.error(f"Error adding friend: {str(e)}", exc_info=True)
        messages.error(request, f'Ошибка: {str(e)}')
    
    # Возвращаемся на страницу, с которой пришли
    next_url = request.META.get('HTTP_REFERER', 'users:all_users_list')
    return redirect(next_url)


@login_required
def remove_friend(request, username):
    """Удаление из друзей"""
    try:
        from_user = request.user.info
        to_user = get_object_or_404(Teacher, username=username)
        to_info = to_user.info
        
        if from_user.remove_friend(to_info):
            logger.info(f"User {request.user.username} removed {to_user.username} from friends")
            messages.success(request, f'{to_user.username} удален из друзей')
        else:
            logger.warning(f"User {request.user.username} tried to remove {to_user.username} who is not in friends list")
            messages.error(request, f'{to_user.username} не в списке друзей')
    except TeacherInfo.DoesNotExist as e:
        logger.error(f"TeacherInfo not found: {str(e)}", exc_info=True)
        messages.error(request, 'Профиль пользователя не найден')
    except Exception as e:
        logger.error(f"Error removing friend: {str(e)}", exc_info=True)
        messages.error(request, f'Ошибка: {str(e)}')
    
    next_url = request.META.get('HTTP_REFERER', 'users:users_list')
    return redirect(next_url)


@login_required
def view_logs(request):
    """Просмотр логов (только для администраторов)"""
    log_files = []
    log_dir = os.path.join(BASE_DIR, 'logs')
    
    if os.path.exists(log_dir):
        for filename in os.listdir(log_dir):
            if filename.endswith('.log'):
                log_files.append(filename)
    
    if 'file' in request.GET:
        file_name = request.GET.get('file')
        file_path = os.path.join(log_dir, file_name)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return HttpResponse(f'<pre>{content}</pre>', content_type='text/html')
    
    html = '<h1>Log files:</h1><ul>'
    for file in log_files:
        html += f'<li><a href="?file={file}">{file}</a></li>'
    html += '</ul>'
    
    return HttpResponse(html)
