from django.conf.urls import include, url
from register.views import *

urlpatterns = [
    url(r'^signup/$', UserRegistrationView.as_view(), name='signup'),
    url(r'^dash/$', UserdashView.as_view(), name='dash'),
    url(r'^user/success/$', UserRegistrationSuccessView.as_view(), name='success'),
]