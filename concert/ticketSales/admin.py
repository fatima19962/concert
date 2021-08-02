from django.contrib import admin

# Register your models here.
from ticketSales.models import concertModel
from ticketSales.models import locationModel
from ticketSales.models import timeModel
from ticketSales.models import ticketModel
#from ticketSales.models import ProfileModel

admin.site.register(concertModel)
admin.site.register(locationModel)
admin.site.register(timeModel)
admin.site.register(ticketModel)
#admin.site.register(ProfileModel)