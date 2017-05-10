from django.conf.urls import url,handler404

from promeds.views import menupage, subcategorypage, addtocartpage
from . import views

#import promeds.views

urlpatterns = [
url(r'^myprofile/$', views.ProfileView, name='profile'),
    url(r'^edit/$', views.UserProfileFormView, name='profileedit'),
    url(r'^home/$', views.homepage,name='home'),
    url(r'menu1/$', menupage, name='menu1'),
    url(r'^login/$', views.login, name='login'),
    url(r'^createaccount/$',views.UserFormView.as_view(),name='createaccount'),
    url(r'healthcare/$',views.healthcarepage,name='healthcarepage'),
    url(r'diagnostic/$', views.diagnosticpage, name='diagnosticpage'),

    url(r'^sub/(?P<subcat_id>[0-9]+)$',subcategorypage,name='subcategorypage'),
    url(r'logout/$', views.log_out, name='logoutpage'),
    url(r'^addtocart/(?P<medid>[0-9]+)$', addtocartpage, name='addtocart'),
    url(r'^ordermedicines/$', views.index, name='ordermedicines'),
    url(r'shippingdetail/$', views.shippingdetailspage, name='shippingdetails'),
    url(r'^ordermedicines/(?P<tablet_id>[0-9]+)/$', views.detailTablet, name='detailTablet'),
    url(r'^subtest/$', views.subtest, name='subtest'),
    url(r'^review/$',views.reviewpage,name='review'),
    url(r'^review/(?P<tabb_id>[0-9]+)/$' , views.deleteitem , name='delete'),
    url(r'^bill/$',views.billpage,name ='billpage'),
    url(r'shipping/$', views.shippingdetailspage1, name='shippingdetails1'),
    url(r'^revieworder/$', views.reviewpage1, name='reviewmeds'),
    url(r'^revieworder/(?P<medd_id>[0-9]+)/$',views.deletemed,name='deletemed'),
    url(r'^bills/$', views.billmedpage, name='bill'),
    url(r'^history/$',views.historypage,name='history'),
    url(r'^history/(?P<bill_id>[0-9]+)/(?P<order_id>[0-9]+)/$',views.deleteorder,name='deleteorder'),
    url(r'^time_check/$', views.time, name='time'),
    url(r'^subtest/(?P<test1_id>[0-9]+)/$', views.deletetest, name='deletetest'),
    url(r'^Reviewtest/$', views.createbill, name='Create_bill'),
    url(r'^history1/(?P<bill_id>[0-9]+)/(?P<order_id>[0-9]+)/$',views.deleteorders,name='deleteorders'),
    url(r'^history2/(?P<test_id>[0-9]+)/$', views.deleteorder_test, name='deleteorder_test'),

]
