from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from utils import generate_code

# Create your models here.
from utils.generate_times import two_min_from_now


class User(AbstractUser):
    """User Model class

    attributes:
        username: str - user phone number
        first_name: str
        last_name: str
        is_active: bool
        is_staff: bool
        is_superuser: bool
        date_joined: datetime
        last_login: datetime
        national_code: str

    methods:
        __str__: str
        get_full_name: str
    """

    username = models.CharField(max_length=100, unique=True, verbose_name='شماره تلفن',
                                error_messages={'unique': 'این شماره تلفن قبلا ثبت شده است',
                                                'blank': 'وارد کردن شماره تلفن اجباری است',
                                                'null': 'وارد کردن شماره تلفن اجباری است'})

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
        indexes = [
            models.Index(fields=['username', ]),
        ]

    def __str__(self):
        return self.username

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.username


class AuthRequest(models.Model):
    """Store all authorization requests for users


    attributes:
        username : str - phone number
        code : str - digit


    """

    class Meta:
        verbose_name = 'درخواست تایید'
        verbose_name_plural = 'درخواست های تایید'

    class RequestType(models.IntegerChoices):
        register = 1, 'ثبت نام'
        login = 2, 'ورود'
        reset_password = 3, 'بازیابی رمز عبور'
        payment = 4, 'پرداخت'
        change_password = 5, 'تغییر رمز عبور'

    class Status(models.IntegerChoices):
        pending = 1, 'در انتظار'
        success = 2, 'موفق'
        failed = 3, 'ناموفق'

    username = models.CharField(max_length=100, verbose_name='شماره تلفن')
    code = models.CharField(max_length=6, verbose_name='کد تایید', default=generate_code)
    request_type = models.IntegerField(choices=RequestType.choices, verbose_name='نوع درخواست',
                                       default=RequestType.register)
    status = models.IntegerField(choices=Status.choices, verbose_name='وضعیت درخواست',
                                 default=Status.pending)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    expire_at = models.DateTimeField(verbose_name='تاریخ انقضا', default=two_min_from_now)
    is_registered = models.BooleanField(verbose_name='ثبت نام شده', default=False)

    def __str__(self):
        return f'{self.username} - {self.code} - {self.request_type} - {self.status}'
