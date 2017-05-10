import pytz as pytz
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.views import generic
from django.views.generic import View
#from .forms import AddCartForm
#from registration.forms import User
from django.core.mail import EmailMessage

from promeds import forms
from .models import order, Tablets,orderTab, bill,billmed,checktest,appointment, UserProfile, UserShippingDetails
from django.utils import timezone
from promeds.models import Medicines,category,test
from .forms import UserForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
import pytz
from .forms import UserForm,UserProfileForm

class UserFormView(View):
  form_class = UserForm
template_name = 'promeds/trialregform.html'

#
display a blank form
def get(self, request):
  form = self.form_class(None)
return render(request, self.template_name, {
  'form': form
})

# process form dattr
def post(self, request):
  form = self.form_class(request.POST)

if form.is_valid():

  user = form.save(commit = False)

# cleaned data
username = form.cleaned_data['username']

password = form.cleaned_data['password1']
first_name = form.cleaned_data['first_name']
last_name = form.cleaned_data['last_name']
email = form.cleaned_data['email']
user.set_password(password)
user.save()

user = authenticate(username = username, password = password)
if user is not None:
  if user.is_active:
  auth_login(request, user)
user = request.user

return render(request, 'promeds/menu.html', {
  'user': user
})
else :
  return HttpResponse("user is not active")
else :
  return HttpResponse("user is none")

else :
  return render(request, self.template_name, {
    'form': form
  })

def homepage(request):

  return render(request, 'promeds/trialhome.html', None)

def menupage(request):
  return render(request, 'promeds/menu.html', None)

def login(request):
  context = RequestContext(request)
if request.method == 'POST':
  username = request.POST.get('username')
password = request.POST.get('password')
if not username:
  if not password:
  return render(request, 'promeds/trialhome.html', {
    'error_message': 'Please enter the Username and Password'
  })
else :
  return render(request, 'promeds/trialhome.html', {
    'error_message': 'Please enter the Username'
  })
elif not password:
  return render(request, 'promeds/trialhome.html', {
    'error_message': 'Please enter the Password'
  })

user = authenticate(username = username, password = password)

if user is not None:
  if user.is_active:
  auth_login(request, user)
user = request.user
return render(request, 'promeds/menu.html', {
  'user': user
})
else :
  return render(request, 'promeds/trialhome.html', {
    'error_message': 'Your account has been disabled'
  })
else :
  return render(request, 'promeds/trialhome.html', {
    'error_message': 'Username and Password do not match'
  })
else :
  return render_to_response('promeds/home.html', {}, context)

def log_out(request):
  o1 = orderTab.objects.filter(flagt = 1)
o1.delete()
orderTab.objects.all().update(flagt = 0)
o2 = order.objects.filter(flago = 1)
o2.delete()
order.objects.all().update(flago = 0)
appointment.objects.all().update(flag_app = 0)
checktest.objects.all().update(flagtest = 0)

logout(request)
return redirect('home')

def healthcarepage(request):
  all_medicines = Medicines.objects.all()
all_subcategory = category.objects.all()
return render(request, 'promeds/firstaid.html', {
  'all_medicines': all_medicines,
  'all_subcategory': all_subcategory
})

def subcategorypage(request, subcat_id):
  all_medicines = Medicines.objects.filter(sub_categoryno = subcat_id)
all_subcategory = category.objects.all()
value = 1
return render(request, 'promeds/firstaid.html', {
  'all_medicines': all_medicines,
  'all_subcategory': all_subcategory,
  'value': value
})

def addtocartpage(request, medid):
  ordered = order.objects.filter(User_name = request.user).filter(flago = 1).filter(med_id = medid)
if ordered:
  value = 3
else :
  orders = order()
user = request.user
orders.User_name = user
orders.quantity = request.POST['quantity']
orders.med_id = medid
orders.orderdate = datetime.datetime.utcnow()
orders.save()
value = 2
all_medicines = Medicines.objects.all()
all_subcategory = category.objects.all()
medicinename = Medicines.objects.get(pk = medid)

return render(request, 'promeds/firstaid.html', {
  'all_medicines': all_medicines,
  'all_subcategory': all_subcategory,
  'medicinename': medicinename,
  'value': value
})

def diagnosticpage(request):

  app = appointment.objects.filter(User_name = request.user).filter(flag_app = 1)
app.delete()
all_test = test.objects.all()
context = {
  'all_test': all_test,

}
return render(request, 'promeds/diagnostic.html', context)

def index(request):

  all_tablets = Tablets.objects.all()
context = {
  'all_tablets': all_tablets
}
return render(request, 'promeds/ordertab.html', context)

def detailTablet(request, tablet_id): #return HttpResponse(tablet_id)

if request.method == "POST":
  ordered = orderTab.objects.filter(User_name = request.user).filter(flagt = 1).filter(tab_id = tablet_id)
if ordered:
  value = 3
else :
  value = 2
ordersTab = orderTab()
user = request.user
ordersTab.User_name = user
ordersTab.quantity = request.POST['quantity']
ordersTab.tab_id = tablet_id
ordersTab.order_date = datetime.datetime.utcnow()
ordersTab.save()
else :
  value = 1

tablet = Tablets.objects.get(pk = tablet_id)# return HttpResponse("hi" + tablet.tab_name)
return render(request, 'promeds/tabpage.html', {
  'tablet': tablet,
  'value': value
})

def shippingdetailspage(request):
  return render(request, 'promeds/checkout.html')

def subtest(request):
  all_test = test.objects.all()
x = checktest.objects.filter(User_name = request.user).filter(flagtest = 1)
app = appointment()
user = request.user
app.User_name = user
app.lab = request.POST.get('labbook')
app.date_app1 = request.POST.get('date')
app.time_slot = request.POST.get('timebook')
print(app.date_app1)
print(app.time_slot)
app.save()

context = {
  'all_test': all_test,
  'x': x,
  'app': app,
}
return render(request, 'promeds/check.html', context)

#
return HttpResponse(some_var)

def reviewpage(request):
  tabletss = orderTab.objects.filter(User_name = request.user).filter(flagt = 1)
tab = Tablets.objects.all()

if UserShippingDetails.objects.filter(user = request.user).exists():
  UserShippingDetails.objects.get(user = request.user).delete()
shp = UserShippingDetails()
shp.user = request.user
shp.landmark = request.POST.get('landmark')
shp.city = request.POST.get('city')
shp.state = request.POST.get('state')
shp.pincode = request.POST.get('pincode')
shp.address = request.POST.get('address')
print(shp.landmark)
shp.save()
return render(request, 'promeds/revieworder.html', {
  'tabletss': tabletss,
  'tab': tab
})

def deleteitem(request, tabb_id):
  order = orderTab.objects.filter(User_name = request.user).filter(flagt = 1).filter(tab_id = tabb_id)
order.delete()
tabletss = orderTab.objects.filter(User_name = request.user).filter(flagt = 1)
tab = Tablets.objects.all()
return render(request, 'promeds/revieworder.html', {
  'tabletss': tabletss,
  'tab': tab
})

def deletemed(request, medd_id):
  orderss = order.objects.filter(User_name = request.user).filter(flago = 1).filter(med_id = medd_id)
orderss.delete()
medss = order.objects.filter(User_name = request.user).filter(flago = 1)
med = Medicines.objects.all()
return render(request, 'promeds/reviewmeds.html', {
  'medss': medss,
  'med': med
})

def billpage(request):

  tabletss = orderTab.objects.filter(User_name = request.user).filter(flagt = 1)

for tab in tabletss:
  tab.flagt = 2
tab.save()
tab = Tablets.objects.all()
t1 = 0
for o in tabletss:
  for t in tab:
  if t.pk == o.tab_id:
  o.total_price = o.quantity * t.tab_price
t1 = t1 + o.total_price
bills = bill()
user = request.user
bills.userr = user
bills.totalprice = t1
bills.save()
bills.orders.set(tabletss)
spd = UserShippingDetails.objects.get(user = request.user)
email = EmailMessage("Order Confirm", "Thank you for Ordering Medicines from Promeds", to = [user.email], )
email.send()

return render(request, 'promeds/billdet.html', {
  'tabletss': tabletss,
  'tab': tab,
  'bills': bills,
  'user': user,
  't1': t1,
  'spd': spd
})

def shippingdetailspage1(request):
  return render(request, 'promeds/shipping.html')

def reviewpage1(request):
  medss = order.objects.filter(User_name = request.user).filter(flago = 1)
med = Medicines.objects.all()
if UserShippingDetails.objects.filter(user = request.user).exists():
  UserShippingDetails.objects.get(user = request.user).delete()
shp = UserShippingDetails()
shp.user = request.user
shp.landmark = request.POST.get('landmark')
shp.city = request.POST.get('city')
shp.state = request.POST.get('state')
shp.pincode = request.POST.get('pincode')
shp.address = request.POST.get('address')
print(shp.landmark)
shp.save()

return render(request, 'promeds/reviewmeds.html', {
  'medss': medss,
  'med': med
})

def billmedpage(request):
  medss = order.objects.filter(User_name = request.user).filter(flago = 1)
for m in medss:
  m.flago = 2
m.save()

med = Medicines.objects.all()
t2 = 0
for m in medss:
  for e in med:
  if e.pk == m.med_id:
  m.total_price = m.quantity * e.price
t2 = t2 + m.total_price

bills = billmed()
user = request.user
bills.users = user
bills.totalprice = t2

bills.save()
bills.ordermed.set(medss)
email = EmailMessage("Order Confirm", "Thank you for Ordering from Promeds  ", to = [user.email], )
email.send()
spd = UserShippingDetails.objects.get(user = request.user)
print(spd.landmark)
return render(request, 'promeds/billmed.html', {
  'medss': medss,
  'med': med,
  'bills': bills,
  'user': user,
  't2': t2,
  "spd": spd
})

def historypage(request):
  bills = bill.objects.filter(userr = request.user)
bills1 = billmed.objects.filter(users = request.user)
medss = order.objects.filter(User_name = request.user)
med = Medicines.objects.all()
tabletss = orderTab.objects.filter(User_name = request.user)
tab = Tablets.objects.all()
app = appointment.objects.filter(User_name = request.user)
return render(request, 'promeds/history.html', {
  'bills': bills,
  'bills1': bills1,
  'medss': medss,
  'med': med,
  'tabletss': tabletss,
  'tab': tab,
  'app': app,
})

def deleteorder(request, bill_id, order_id):
  order1 = orderTab.objects.get(pk = order_id)
time = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
c = time - order1.order_date
if c < datetime.timedelta(days = 1):

  bill1 = bill.objects.get(pk = bill_id)
bill1.orders.remove(order_id)

bill1.totalprice = bill1.totalprice - order1.total_price
bill1.save()
value = 1

else :
  value = 2

bills = bill.objects.filter(userr = request.user)
bills1 = billmed.objects.filter(users = request.user)
medss = order.objects.filter(User_name = request.user)
med = Medicines.objects.all()
tabletss = orderTab.objects.filter(User_name = request.user)
tab = Tablets.objects.all()
return render(request, 'promeds/history.html', {
  'bills': bills,
  'bills1': bills1,
  'medss': medss,
  'med': med,
  'tabletss': tabletss,
  'tab': tab,
  'value': value
})

def deleteorders(request, bill_id, order_id):
  order1 = order.objects.get(pk = order_id)

time = datetime.datetime.utcnow().replace(tzinfo = pytz.UTC)
c = time - order1.order_date
if c < datetime.timedelta(days = 1):

  bill1 = billmed.objects.get(pk = bill_id)
bill1.ordermed.remove(order_id)

bill1.totalprice = bill1.totalprice - order1.totalprice
bill1.save()
value = 1

else :
  value = 2

bills = bill.objects.filter(userr = request.user)
bills1 = billmed.objects.filter(users = request.user)
medss = order.objects.filter(User_name = request.user)
med = Medicines.objects.all()
tabletss = orderTab.objects.filter(User_name = request.user)
tab = Tablets.objects.all()
app = appointment.objects.filter(User_name = request.user)
return render(request, 'promeds/history.html', {
  'app': app,
  'bills': bills,
  'bills1': bills1,
  'medss': medss,
  'med': med,
  'tabletss': tabletss,
  'tab': tab,
  'value': value
})

def deleteorder_test(request, test_id):
  app = appointment.objects.get(pk = test_id)
print(app.Date_of_booking.day)
print(app.Date_of_booking.month)
today = datetime.datetime.today()
m = today.month - app.Date_of_booking.month
print(m)
if (m >= 0):
  c = app.Date_of_booking.day - (today.day)
else :
  c = today.day - app.Date_of_booking.day

print(c)
if c == 1 or - 1:
  app.delete()
value = 1
else :
  value = 2

app = appointment.objects.filter(User_name = request.user)
bills = bill.objects.filter(userr = request.user)
bills1 = billmed.objects.filter(users = request.user)
medss = order.objects.filter(User_name = request.user)
med = Medicines.objects.all()
tabletss = orderTab.objects.filter(User_name = request.user)
tab = Tablets.objects.all()
return render(request, 'promeds/history.html', {
  'bills': bills,
  'bills1': bills1,
  'medss': medss,
  'med': med,
  'tabletss': tabletss,
  'tab': tab,
  'value': value,
  'app': app
})

def deletetest(request, test1_id):
  ctest = checktest.objects.filter(User_name = request.user).filter(test_id = test1_id)
ctest.delete()
all_test = test.objects.all()
x = checktest.objects.filter(User_name = request.user).filter(flagtest = 1)
app = appointment.objects.filter(User_name = request.user).get(flag_app = 1)
print(app.date_app1)

context = {
  'all_test': all_test,
  'x': x,
  'app': app,
}
return render(request, 'promeds/check.html', context)

def time(request):

  x = request.POST.getlist('checks[]')
user = request.user

for t in x:
  test1 = test.objects.get(name = t)
checktest1 = checktest()
checktest1.test_id = test1.id
checktest1.User_name = user
checktest1.storetest = t
print(checktest1.storetest)
checktest1.save()
return render(request, 'promeds/time_check.html', None)

def createbill(request):
  all_test = test.objects.all()
x = checktest.objects.filter(User_name = request.user).filter(flagtest = 1)
app = appointment.objects.filter(User_name = request.user).get(flag_app = 1)
t2 = 0
print(app.date_app1)
for m in x:
  for t in all_test:
  if m.storetest == t.name:
  t2 = t.price + t2

context = {
  'all_test': all_test,
  'app': app,
  'x': x,
  't2': t2
}
user = request.user
email = EmailMessage("Order Confirm", "Thank you for Booking Test from Promeds ", to = [user.email], )
email.send()

return render(request, 'promeds/Create_bill_test.html', context)

## def billpage(request): ##tabletss = orderTab.objects.filter(User_name = request.user).filter(flagt = 1)# for tab in tabletss: #tab.flagt = 2## tab = Tablets.objects.all()# t1 = 0#
for o in tabletss: #for t in tab: #if t.pk == o.tab_id: #o.total_price = o.quantity * t.tab_price# t1 = t1 + o.total_price# bills = bill()# user = request.user# bills.userr = user# bills.totalprice = t1# bills.billdate = datetime.datetime.utcnow()# bills.save()# bills.orders.set(tabletss)# return render(request, 'promeds/billdet.html', {
  'tabletss': tabletss,
  'tab': tab,
  'bills': bills,
  'user': user,
  't1': t1
})

def ProfileView(request):
  try:
  upro = UserProfile.objects.get(user = request.user)
except UserProfile.DoesNotExist:
  return render(request, 'promeds/profile.html', {})
return render(request, 'promeds/profile.html', {
  'profiles': upro
})

def UserProfileFormView(request):
  form = UserProfileForm(request.POST or None, request.FILES)
if request.method == "POST":

  print(1)

if UserProfile.objects.filter(user = request.user).exists():
  UserProfile.objects.get(user = request.user).delete()
if form.is_valid():
  print(2)
profile = form.save(commit = False)
profile.user = request.user
profile.save()
return redirect('profile')
context = {
  'form': form
}
return render(request, 'promeds/profileedit.html', context)
