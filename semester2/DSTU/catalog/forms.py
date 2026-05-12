from django import forms
from .models import Student, Course


# class TeacherForm(forms.ModelForm):
#     class Meta:
#         model = Teacher
#         fields = '__all__'
#         widgets = {
#             'patronymic': forms.TextInput(),
#         }
#         labels = {
#             'first_name': 'Имя',
#             'last_name': 'Фамилия',
#             'patronymic': 'Отчество'
#         }
#         help_texts = {
#             'patronymic': 'Необязательно'
#         }

#     def clean_first_name(self):
#         return self.cleaned_data['first_name'].split()[0]

#     def clean_last_name(self):
#         last_name = self.cleaned_data['last_name']
#         last_name = last_name.split()[0]
#         return last_name

#     # def clean_patronymic(self):
#     #     patronymic = self.cleaned_data['patronymic']
#     #     patronymic = patronymic.split()[0]
#     #     return patronymic

#     def clean(self):
#         f = self.cleaned_data.get('first_name')
#         last = self.cleaned_data['last_name']
#         p = self.cleaned_data['patronymic']

#         if f == last or last == p or p == f:
#             raise forms.ValidationError(
#                 'Имя, фамилия и отчество не должны совпадать')


# class TeacherInfoForm(forms.ModelForm):
#     class Meta:
#         model = TeacherInfo
#         fields = ['phone', 'email', 'birthday']
#         widgets = {
#             'phone': forms.TextInput(),
#             'email': forms.TextInput(),
#             'birthday': forms.DateInput(attrs={
#                 'type': 'date'
#             }),
#         }
#         labels = {
#             'phone': 'Номер телефона',
#             'email': 'Почта',
#             'birthday': 'Дата рождения'
#         }
#         help_texts = {
#             'email': 'Необязательно',
#         }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'patronymic': 'Отчество',
            'phone': 'Номер телефона',
            'birthday': 'День рождения',
            'email': 'Почта',
        }
        help_texts = {
            'patronymic': 'Необязательно',
            'birthday': 'Необязательно',
            'email': 'Необязательно',
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'date']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date'
            }),
        }
        labels = {
            'title': 'Название',
            'teacher': 'Учитель',
            'date': 'День создания'
        }
        help_texts = {
            'date': 'Необязательно',
        }

    # def clean(self):
    #     date = self.cleaned_data['date']
    #     teacher_birth = self.cleaned_data['teacher']

    #     if date < teacher_birth:
    #         print('a')
    #     else:
    #         print(date, teacher_birth)
