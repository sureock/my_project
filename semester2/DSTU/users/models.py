from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from .validators import real_email, real_number, validate_image_file
from PIL import Image
import logging

logger = logging.getLogger(__name__)


class Teacher(AbstractUser):
    pass


class TeacherInfo(models.Model):
    teacher = models.OneToOneField(
        Teacher,
        on_delete=models.CASCADE,
        related_name='info',
        primary_key=True,
        verbose_name='Учитель'
    )
    first_name = models.CharField(
        'Имя',
        max_length=100,
        blank=False,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=100,
        blank=False
    )
    phone = models.CharField(
        'Номер телефона',
        max_length=30,
        blank=False,
        unique=True,
        validators=[real_number]
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        blank=True,
        null=True,
        validators=[validate_image_file]  # Добавляем валидатор
    )
    birthday = models.DateField(
        'Дата рождения',
        blank=True,
        null=True
    )
    friends = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True
    )
    
    def get_friends(self):
        return self.friends.all()
    
    def add_friend(self, profile):
        """Добавить друга"""
        if profile not in self.friends.all() and profile != self:
            self.friends.add(profile)
            return True
        return False
    
    def remove_friend(self, profile):
        """Удалить друга"""
        if profile in self.friends.all():
            self.friends.remove(profile)
            return True
        return False
    
    def is_friend(self, profile):
        """Проверить, является ли пользователь другом"""
        return profile in self.friends.all()
    
    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
            
            # Обработка аватарки
            if self.avatar:
                try:
                    img = Image.open(self.avatar.path)
                    if img.height > 300 or img.width > 300:
                        output_size = (300, 300)
                        img.thumbnail(output_size)
                        img.save(self.avatar.path)
                        logger.info(f"Avatar resized for user {self.teacher.username}")
                except Exception as e:
                    logger.error(f"Error processing avatar for {self.teacher.username}: {str(e)}", exc_info=True)
                    raise ValidationError(f'Ошибка обработки изображения: {str(e)}')
        except Exception as e:
            logger.error(f"Error saving TeacherInfo for {self.teacher.username}: {str(e)}", exc_info=True)
            raise
