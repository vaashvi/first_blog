from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime
class Medicines(models.Model):
    name = models.CharField(max_length=300)
    image = models.FileField(upload_to='medi')
    price = models.IntegerField()
    formulation = models.CharField(max_length=30)
    sub_categoryname = models.CharField(max_length=100)
    sub_categoryno = models.IntegerField()

    def __str__(self):
        return self.name

class category(models.Model):
    cname = models.CharField(max_length=200)
    ccount = models.IntegerField()

class order(models.Model):
    User_name = models.ForeignKey(User,on_delete=models.CASCADE)
    med_id = models.IntegerField()
    quantity = models.IntegerField()
    flago = models.IntegerField(default=1)
    orderdate = models.DateTimeField(default=datetime.datetime.utcnow)
    totalprice = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)


class test(models.Model):
    name=models.CharField(max_length=300)
    text=models.CharField(max_length=500)
    price=models.IntegerField(default=1)
    duration=models.CharField(max_length=20,default="15mins")

    def __str__(self):
        return self.name

class Tablets(models.Model):
    tab_name = models.CharField(max_length=250)
    tab_price = models.FloatField()
    tab_manufacturer = models.CharField(max_length=250)
    tab_sideeff = models.CharField(max_length=250)


    def __str__(self):
        return self.tab_name

class orderTab(models.Model):
    User_name = models.ForeignKey(User,on_delete=models.CASCADE)
    tab_id = models.IntegerField()
    quantity = models.IntegerField()
    flagt = models.IntegerField(default=1)
    order_date=models.DateTimeField(default=datetime.datetime.utcnow)
    total_price =models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)

class prescription(models.Model):
    User_name = models.ForeignKey(User,on_delete=models.CASCADE)
    prescription = models.FileField(upload_to='prescription')

class bill(models.Model):
    userr = models.ForeignKey(User,on_delete=models.CASCADE)
    orders = models.ManyToManyField(orderTab)
    totalprice = models.FloatField()
    billdate = models.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return str(self.pk)

class billmed(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    ordermed = models.ManyToManyField(order)
    totalprice = models.FloatField(default=0)
    billdate = models.DateTimeField(default=datetime.datetime.utcnow)

    def __str__(self):
        return str(self.pk)


class updateuser(models.Model):
    User= models.OneToOneField(User,on_delete =models.CASCADE)
    contact_no = models.IntegerField()
    flat_no = models.IntegerField()
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    pincode = models.IntegerField()
    userprofile = models.FileField(upload_to='profile')

    def __str__(self):
        return self.Username

class checktest(models.Model):
    User_name=models.ForeignKey(User,on_delete=models.CASCADE)
    storetest=models.CharField(max_length=250)
    flagtest = models.IntegerField(default=1)
    test_id=models.IntegerField(default=1)

    def __str__(self):
        return self.User_name_id + self.storetest

class appointment(models.Model):
    User_name=models.ForeignKey(User,on_delete=models.CASCADE)
    lab=models.CharField(max_length=250)
    date_app1 =models.DateField(default=datetime.datetime.utcnow)
    time_slot=models.CharField(max_length=250,default=1)
    Date_of_booking=models.DateField(default=datetime.datetime.utcnow)
    flag_app=models.IntegerField(default=1)
    ordertest = models.ManyToManyField(checktest)
    totalprice = models.FloatField(default=0)


class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)

	contact_no = models.IntegerField(null=True, blank = True)
	address = models.TextField(max_length=300,null=True,blank=True)
	blood_group = models.CharField(max_length=2,default = 'O')
	profilepic = models.ImageField(upload_to='profilepic', null=True, blank = True)

	def __str__(self):
		return self.contact_no

class UserShippingDetails(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)
     landmark = models.CharField(max_length=200,null=True)
     city = models.CharField(max_length=100,null=True)
     pincode = models.IntegerField()
     state = models.CharField(max_length=200,null=True)
     address = models.CharField(max_length=300,null=True)