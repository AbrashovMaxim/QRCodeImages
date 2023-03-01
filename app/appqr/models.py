from django.db import models

from django.contrib.auth.models import User

class QrImageGenerator(models.Model):
    image_image = models.ImageField(upload_to='photo/%Y/%m/%d/%H/%M/%S', verbose_name='Изображение')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель')
    
