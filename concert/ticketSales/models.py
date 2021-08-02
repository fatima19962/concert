from django.db import models
from jalali_date import date2jalali,datetime2jalali
# Create your models here.
from accounts.models import ProfileModel

class concertModel(models.Model):
    class Meta:

        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"

    Name = models.CharField(max_length=100, verbose_name=" نام کنسرت")
    SingerName = models.CharField(max_length=100,
                                  verbose_name="نام خواننده")
    lenght = models.IntegerField(verbose_name="مدت زمان")
    Poster = models.ImageField(upload_to="concertImages/",
                               null=True,
                               verbose_name="پوستر")

    def __str__(self):
        return self.SingerName


class locationModel(models.Model):
    class Meta:

        verbose_name = " مکان برگذاری  "
        verbose_name_plural = "مکان برگذاری"

    IdNumber = models.IntegerField(primary_key=True,
                                   verbose_name="آیدی")
    Name = models.CharField(max_length=100, verbose_name="نام")
    Address = models.CharField(max_length=500,
                               default="تهران-برج میلاد",
                               verbose_name="آدرس ")
    Phone = models.CharField(max_length=11,
                             null=True,
                             verbose_name="تلفن")
    capacity = models.IntegerField(verbose_name="ظرفیت")

    def __str__(self):
        return self.Name


class timeModel(models.Model):
    class Meta:

        verbose_name = "سانس"
        verbose_name_plural = "سانس"

    concertModel = models.ForeignKey("concertModel",
                                     on_delete=models.PROTECT,
                                     verbose_name=" کنسرت")
    locationModel = models.ForeignKey(to=locationModel,
                                      on_delete=models.PROTECT,
                                      verbose_name=" مکان برگذاری")
    StartDateTime = models.DateTimeField(verbose_name="تاریخ برگذاری")
    seats = models.IntegerField(verbose_name="تعداد صندلی")

    start = 1
    End = 2
    Cancle = 3
    Sales = 4
    status_chioces = ((start, "فروش بلیط شروع شده است"),
                      (End, "فروش بلیط تمام شده است"),
                      (Cancle,
                       "این سانس کنسل شده است"), (Sales, "در حال فروش بلیط"))

    Status = models.IntegerField(choices=status_chioces,verbose_name="وضعیت")

    def __str__(self):
        return "Time:{} ConcertName: {} Location: {}". format(self.StartDateTime, self.concertModel.Name, self.locationModel.Name)
    
    def get_jalali_date(self):
        return datetime2jalali(self.StartDateTime)

# class ProfileModel(models.Model):
#     class Meta:

#         verbose_name = "کاربر"
#         verbose_name_plural = "کاربر"

#     Name = models.CharField(max_length=100, verbose_name="نام")
#     Family = models.CharField(max_length=100,
#                               verbose_name="نام خانوادگی")
#     ProfileImage = models.ImageField(upload_to="ProfileImages/",
#                                      verbose_name="  تصویر پروفایل")

#     Man = 1
#     Woman = 2
#     status_chioces = (("Man", "مرد"), ("Woman", "زن"))

#     Gender = models.IntegerField(choices=status_chioces,
#                                  verbose_name=" جنسیت ")

#     def __str__(self):
#         return "FullName: {} {}".format(Name, Family)


class ticketModel(models.Model):
    class Meta:

        verbose_name = "بلیط"
        verbose_name_plural = "بلیط"

    ProfileModel = models.ForeignKey(ProfileModel,
                                     on_delete=models.PROTECT,
                                     verbose_name="پروفایل")
    timeModel = models.ForeignKey("timeModel", on_delete=models.PROTECT,
                                  verbose_name="زمان")
    ticketImage = models.ImageField(upload_to="TicketImages/",
                                    verbose_name=" تصویر بلیط ")

    Name = models.CharField(max_length=100, verbose_name="نام")
    Price = models.IntegerField(verbose_name="قیمت")

    def __str__(self):
        return "TicketInfo:Profile: {} ConcertInfo : {} ".format(timeModel.__str__())
