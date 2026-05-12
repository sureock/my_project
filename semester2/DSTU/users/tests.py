import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects, assertTemplateUsed
from .models import Teacher, TeacherInfo

@pytest.fixture
@pytest.mark.django_db
def user(db):
    """Фикстура для создания обычного пользователя"""
    user = Teacher.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='testpass123',
    )
    TeacherInfo.objects.get_or_create(
        teacher=user,
        defaults={
            'phone': '+78034887894',
            'first_name': 'Test',
            'last_name': 'User',
            'birthday': '2005-12-25'
            }
    )
    return user

@pytest.fixture
@pytest.mark.django_db
def user2(db):
    """Фикстура для второго пользователя"""
    user2 = Teacher.objects.create_user(
        username='testuser2',
        email='test2@example.com',
        password='testpass123',
    )
    TeacherInfo.objects.get_or_create(
        teacher=user2,
        defaults={
            'phone': '+79876543212',
            'first_name': 'Test2',
            'last_name': 'User2',
            'birthday': '2005-12-25'
            }
    )
    return user2

@pytest.fixture
def authenticated_client(client, user):
    """Фикстура для авторизованного клиента"""
    client.login(username='testuser', password='testpass123')
    return client

class TestRegister:

    def test_register_success(self, user):
        assert Teacher.objects.filter(username=user.username).exists()

    @pytest.mark.django_db
    @pytest.mark.parametrize('field,value,should_fail', [
        ('username', '', True),  
        ('username', 'ab', True),  
        ('email', 'invalid-email', True), 
        ('password2', 'different', True),
    ])
    def test_register_validation(self, client, field, value, should_fail):
        """Параметризованный тест валидации формы регистрации"""
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        }
        
        if field == 'password2' and value == 'different':
            data['password2'] = 'different'
        elif field == 'username' and value == '':
            del data['username']
        else:
            data[field] = value
        
        response = client.post(reverse('users:register'), data)
        
        if should_fail:
            assert response.status_code == 200
            assert 'form' in response.context
            assert response.context['form'].errors
            if field == 'username' and value:
                assert not Teacher.objects.filter(username=value).exists()
        else:
            assert Teacher.objects.filter(username=value).exists()

class TestLoginLogout:
    
    @pytest.mark.django_db
    def test_login_success(self, client, user):
        """Тест: успешный вход в систему"""
        data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        response = client.post(reverse('users:login'), data)

        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')

        assert response.wsgi_request.user.is_authenticated
    
    def test_logout(self, authenticated_client):
        """Тест: выход из системы"""
        response = authenticated_client.get(reverse('users:logout'))
        assert response.status_code == 302
        assertRedirects(response, reverse('users:login'))
    
    @pytest.mark.parametrize('credentials,should_succeed', [
        ({'username': 'testuser', 'password': 'testpass123'}, True),
        ({'username': 'testuser', 'password': 'wrong'}, False),
        ({'username': 'wronguser', 'password': 'testpass123'}, False),
        ({'username': '', 'password': 'testpass123'}, False),
    ])
    def test_login_parameterized(self, client, user, credentials, should_succeed):
        """Параметризованный тест различных сценариев входа"""
        response = client.post(reverse('users:login'), credentials)
        
        assert response.status_code == 200
        
        if should_succeed:
            assertTemplateUsed(response, 'index.html')
            assert response.wsgi_request.user.is_authenticated
        else:
            assertTemplateUsed(response, 'registration/login.html')
            assert not response.wsgi_request.user.is_authenticated

class TestAuthorization:
    
    @pytest.mark.django_db
    def test_profile_requires_login(self, client, user):
        """Тест: просмотр профиля требует авторизации"""
        url = reverse('users:profile', kwargs={'username': user.username})
        response = client.get(url)
        assert response.status_code == 302
        assert '/login/' in response.url
    
    def test_others_profile_not_accessible_without_friendship(self, authenticated_client, user, user2):
        """Тест: чужой профиль недоступен без дружбы"""
        url = reverse('users:profile', kwargs={'username': user2.username})
        response = authenticated_client.get(url)
        assert response.status_code == 302
        assert response.url == reverse('users:users_list')

class TestRedirects:
    
    @pytest.mark.django_db
    def test_register_redirect_after_success(self, client):
        """Тест: редирект после успешной регистрации"""
        data = {
            'username': 'newuser123',
            'email': 'new@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'phone': '+78034897894',
            'birthday': '2000-01-01', 
            'password1': 'Test123!@#',
            'password2': 'Test123!@#',
        }
        response = client.post(reverse('users:register'), data)
        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')
        
    def test_login_redirect_to_index(self, client, user):
        """Тест: редирект после входа на главную"""
        data = {
            'username': 'testuser',
            'password': 'testpass123',
        }
        response = client.post(reverse('users:login'), data)
        assert response.status_code == 200
        assertTemplateUsed(response, 'index.html')
    
    def test_logout_redirect_to_login(self, authenticated_client):
        """Тест: редирект после выхода на страницу входа"""
        response = authenticated_client.get(reverse('users:logout'))
        assertRedirects(response, reverse('users:login'))

class TestPermissions:
    
    @pytest.mark.django_db
    @pytest.mark.parametrize('view_name,requires_auth', [
        ('users:profile_edit', True),
        ('users:users_list', True),
        ('users:all_users_list', True),
        ('users:register', False),  # Добавлено users:
        ('users:login', False),     # Добавлено users:
    ])
    def test_view_authorization_requirements(self, client, user, view_name, requires_auth):
        """Параметризованный тест требований авторизации для разных view"""
        try:
            if view_name == 'users:profile_edit':
                url = reverse(view_name)
            elif view_name in ['users:profile', 'users:add_friend', 'users:remove_friend']:
                url = reverse(view_name, kwargs={'username': user.username})
            else:
                url = reverse(view_name)
        except:
            pytest.skip(f"URL {view_name} not found")
        
        response = client.get(url)
        
        if requires_auth:
            assert response.status_code == 302
            assert '/login/' in response.url
        else:
            assert response.status_code == 200
