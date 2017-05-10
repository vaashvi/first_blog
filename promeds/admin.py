from django.contrib import admin
from promeds.models import Medicines,category,order,test,Tablets,orderTab,bill,billmed,prescription,checktest,appointment, UserShippingDetails

admin.site.register(Medicines)
admin.site.register(category)
admin.site.register(order)
admin.site.register(orderTab)
admin.site.register(test)
admin.site.register(Tablets)
admin.site.register(bill)
admin.site.register(billmed)
admin.site.register(prescription)
admin.site.register(checktest)
admin.site.register(appointment)
admin.site.register(UserShippingDetails)
