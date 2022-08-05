from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *

# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Avatar = models.ImageField(upload_to="images/Avatar",blank=True,null=True)

    code = models.IntegerField(blank=True,null=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return str(self.username) + " - " + str(self.name)

    def full_name(self):
        return str(self.name)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin
# ----------------------------------------------------------------------------------------------------------------------------
