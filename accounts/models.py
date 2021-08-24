from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('必须输入用户名')
        if not password:
            raise ValueError('必须输入密码')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        user = self.create_user(
            username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=200, unique=True, verbose_name='用户名')
    fullname = models.CharField(max_length=200, null=True, verbose_name='全名')
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default=u'男')
    phone = models.CharField(max_length=11,verbose_name=u"手机号码", null=True, blank=True)
    department = models.CharField(max_length=10, choices=(("jishu", u'技术部'), ("xingzheng", u'行政部')), default=u'技术部')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # avatar = models.ImageField(upload_to='avator/%Y%m%d', blank=True)


    USERNAME_FIELD = 'username'
    objects = MyUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    class Meta:
        verbose_name= u'用户信息'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin