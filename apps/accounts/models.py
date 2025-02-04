from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password = None,**extra_fields):
        if not email:
            raise ValueError('Поле email должно быть заполнено')
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Супер пользователь должен иметь is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Супер пользователь должен иметь is_superuser=True')

        return self.create_user(email,password,**extra_fields)


class User(AbstractUser):
    GENDER_CHOICE = [('Мужчина','Мужчина'),
                     ("Женщина","Женщина")]
    username = models.CharField('Никнейм',max_length=25,unique=True)
    email = models.EmailField('Почта', max_length=100, unique=True)
    avatar = models.ImageField('Аватар',upload_to='avatar/',blank=True,null=True)
    age = models.DateField('День рождения',blank=True,null=True)
    bio = models.TextField('О себе',blank=True,null=True)
    phone = models.IntegerField('Мобильный номер',blank=True,null=True)
    created_at = models.DateTimeField('Дата регистрации', auto_now_add=True)
    city = models.CharField('Город',max_length=50,blank=True,null=True)
    male = models.CharField('Пол',choices=GENDER_CHOICE,default=None,blank=True,null=True, max_length=20)

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Ползователь'
        verbose_name_plural = 'Ползователи'