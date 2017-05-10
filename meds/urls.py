
from django.conf.urls import include,url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',include('promeds.urls')),
    url(r'^promeds/',include('promeds.urls')),
#url(r'^resetpassword/passwordsent/$', 'django.contrib.auth.views.password_reset_done',name='password_reset_done'),
#url(r'^reset/password_reset/$', 'django.contrib.auth.views.password_reset', name='reset_password_reset1'),
#url('^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',name='password_reset_confirm'),
#url('^reset/done/$', 'django.contrib.auth.views.password_reset_complete',name='password_reset_complete'),

]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
   urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

