from django.db import models
from fernet_fields import EncryptedTextField
from django.core.validators import URLValidator


class Servises(models.Model):
    page_name = models.CharField('Page Name', max_length=100)
    page_url = models.TextField('Page URL', validators=[URLValidator()])
    user = models.TextField('User')
    password = EncryptedTextField('Password')

    class Meta:
        ordering = ('-id', )
