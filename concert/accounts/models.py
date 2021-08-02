from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ProfileModel(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    # ,related_name="profile")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="کاربری",related_name="profile")

    # Name=models.CharField(max_length=100,verbose_name="نام",null=True)
    # Family=models.CharField(max_length=100,verbose_name="نام خانوادگی",null=True)
    ProfileImage = models.ImageField(
        upload_to="ProfileImages/", verbose_name="عکس")

    Man = 1
    Woman = 2
    status_chioces = ((Man, "مرد"), (Woman, "زن"))

    Gender = models.IntegerField(choices=status_chioces, verbose_name="جنسیت")

    Credit = models.IntegerField(verbose_name="اعتبار", default=0)

    # def __str__(self):
    #     return "FullName: {} {}".format(Name, Family)
