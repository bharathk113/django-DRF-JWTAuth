from django.db import models
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.utils import timezone
# class GameAppUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#         user = self.model(
#             email=self.normalize_email(email),
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and
#         password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
# class tempUser(AbstractBaseUser):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.BooleanField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=150)
#     email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
#     is_staff = models.BooleanField()
#     is_active = models.BooleanField()
#     date_joined = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#         return self.username
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
