from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from .managers import *
# ----------------------------------------------------------------------------------------------------------------------------
class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    north = models.DecimalField(max_digits=5, decimal_places=3)
    east = models.DecimalField(max_digits=5, decimal_places=3)



    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def averageUserRate(self):
        total = sum(item.Rating for item in self.user.all())
        return total / self.amount()

    def totalUserRate(self):
        total = sum(item.Rating for item in self.user.all())
        return total

    def amount(self):
        return self.user.all().count()

    def __str__(self):
        return str(self.name)
# ----------------------------------------------------------------------------------------------------------------------------
class User(AbstractBaseUser):
    status_reason = (
        ('u' , "sutech"),
        ('h', "highschool"),
        ('a' , "Friend"),
        ('g' , "game"),
        ('s' , "school"),
        ('o' , "other"),
        ('f' , "family"),
        ('i' , "instagram"),
        ('y' , "iust"),
    )

    status_gender = (
        ('m',"male"),
        ('f',"female")
    )

    username = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    Avatar = models.ImageField(upload_to="images/Avatar",blank=True,null=True)
    gender = models.CharField(max_length=1,choices = status_gender,default='m')


    code = models.IntegerField(blank=True,null=True)

    reason = models.CharField(max_length=1,choices = status_reason)
    city = models.ForeignKey(City,on_delete=models.CASCADE,related_name="user",blank=True,null=True)
    # Rating = models.IntegerField(default=1)

    # Friends = models.ManyToManyField("User")





    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    objects = MyUserManager()

    def __str__(self):
        return str(self.username) + " - " + str(self.name)

    def makeFriends(self,user):
        try:
            self.Friend.add(user).save()
            user.Friend.add(self).save()
            return True
        except :
            return False


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
