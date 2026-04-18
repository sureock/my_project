from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Teacher, Course, Student, TeacherInfo
from .forms import TeacherForm, TeacherInfoForm, CourseForm


def index(request):
    return render(request, "index.html")


def info(request, name):
    if name != 'Alex':
        return HttpResponseRedirect('/404')
    data = {'name': name}
    return render(request, 'info.html', context=data)


def not_found(request):
    return render(request, 'not_found.html')


def index_authors(request):
    teachers = Teacher.objects.all()
    return render(request, 'index_authors.html', {"teachers": teachers})


def info_authors(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(teacher=teacher)
    teacher_info = TeacherInfo.objects.get(teacher=teacher)
    return render(request, 'info_author.html', {'teacher': teacher,
                                                'courses': courses,
                                                'teacher_info': teacher_info})


def create_author(request):
    teacher_form = TeacherForm(request.GET or None)
    teacherinfo_form = TeacherInfoForm(request.GET or None)

    if teacher_form.is_valid() and teacherinfo_form.is_valid():
        teacher_data = teacher_form.data

        teacher = Teacher.objects.create(
            first_name=teacher_data['first_name'],
            last_name=teacher_data['last_name'],
            patronymic=teacher_data['patronymic'],
        )
        TeacherInfo.objects.create(
            teacher=teacher,
            phone=teacher_data['phone'],
            bio=teacher_data['bio'],
            email=teacher_data['email'],
            birthday=teacher_data['birthday']
        )
        return redirect('/authors/')
    return render(
            request,
            'create_author.html',
            {'teacher_form': teacher_form,
             'teacherinfo_form': teacherinfo_form})


def update_authors(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacherinfo = TeacherInfo.objects.get(teacher=teacher)
    if request.method == 'GET':
        teacher_form = TeacherForm(instance=teacher)
        teacherinfo_form = TeacherInfoForm(instance=teacherinfo)

        context = {'teacher_form': teacher_form,
                   'teacherinfo_form': teacherinfo_form}

        return render(request, 'update_author.html', context)

    if request.method == 'POST':
        teacher_form = TeacherForm(request.POST)
        teacherinfo_form = TeacherInfoForm(request.POST)

        teacher_data = teacher_form.data

        teacher.first_name = teacher_data['first_name']
        teacher.last_name = teacher_data['last_name']
        teacher.patronymic = teacher_data['patronymic']

        teacherinfo.phone = teacher_data['phone']
        teacherinfo.bio = teacher_data['bio']
        teacherinfo.email = teacher_data['email']
        teacherinfo.birthday = teacher_data['birthday']

        teacher.save()
        teacherinfo.save()
        return redirect('/authors/')


def delete_authors(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.delete()
    return redirect('/authors/')


def create_course(request):
    form = CourseForm(request.GET or None)

    teachers = Teacher.objects.all()
    context = {'form': form,
               'teachers': teachers}

    if request.method == 'POST':
        form = CourseForm(request.POST)

        form_data = form.data
        teacher_id = request.POST.get('teachers')
        teacher = Teacher.objects.get(id=teacher_id)
        Course.objects.create(
            teacher=teacher,
            title=form_data['title'],
            date=form_data['date'],
        )
        return redirect('/courses/')
    return render(request, 'create_course.html', context)


def info_course(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(teacher=teacher)
    return render(request, 'index_course.html', {'courses': courses})


def index_course(request):
    courses = Course.objects.all()
    return render(request, 'index_course.html', {'courses': courses})


def update_courses(request, course_id):
    course = Course.objects.get(id=course_id)
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        if course.teacher is None:
            teacher_id = request.POST.get('teachers')
            teacher = Teacher.objects.get(id=teacher_id)
        course.teacher = teacher
        course.title = request.POST.get('title')
        course.save()
        return redirect('/courses/')
    return render(request, 'update_course.html',
                  {'course': course,
                   'teachers': teachers})


def delete_courses(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('/courses/')


def index_student(request):
    students = Student.objects.all()
    return render(request, 'index_student.html', {'students': students})


def unsign_students(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        courses_id = request.POST.getlist('courses')
        courses = Course.objects.filter(id__in=courses_id)
        for course in courses:
            student.courses.remove(course)
        student.save()
        return redirect('/students/')


def sign_students(request, student_id):
    student = Student.objects.get(id=student_id)
    courses = Course.objects.all()
    if request.method == 'POST':
        courses_id = request.POST.getlist('courses')
        courses = Course.objects.filter(id__in=courses_id)
        student.courses.set(courses)
        student.save()
        return redirect('/students/')
    return render(request, 'sign_student.html', {'student': student,
                                                 'courses': courses})


def update_students(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.save()
        return redirect('/students/')
    return render(request, 'update_student.html', {'student': student})


def delete_students(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return redirect('/students/')


def create_students(request):
    if request.method == 'POST':
        Student.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
        )
        return redirect('/students/')
    return render(request, 'create_student.html')


def orm_field(request):
    courses = Course.objects.all()
    context = {'courses': courses}

    s_students = Student.objects.all()
    a_students = []
    for s in s_students:
        if s.courses.count() == 0:
            a_students.append(s)

    b_teachers = Teacher.objects.all()
    nb_teachers = []
    for b in b_teachers:
        if TeacherInfo.objects.get(teacher=b).bio == '':
            nb_teachers.append(b)

    context['nc_students'] = a_students
    context['nb_teachers'] = nb_teachers

    if request.method == 'POST':
        courses_id = request.POST.getlist('courses')
        courses = Course.objects.filter(id__in=courses_id)

        count = request.POST.get('number')

        if count is None:
            count = 0

        authors = Teacher.objects.all()
        authors_a = []
        for author in authors:
            if Course.objects.filter(teacher=author).count() > int(count):
                authors_a.append(author)

        students = Student.objects.filter(courses__in=courses).distinct()

        context['students'] = students
        context['course'] = courses
        context['teachers'] = authors_a

        return render(request, "orm.html", context)
    return render(request, "orm.html", context)
