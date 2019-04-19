from django.conf.urls import url,re_path
from django.urls import path,include
from djoser import views as djoser_views
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    re_path(r'^user_register/$', views.UserRegister.as_view(), name='user-register'),
    re_path(r'^user_register/confirm/(?P<user_id>[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_=]*)/$', views.UserConfirm, name='user-confirm'),
    re_path(r'^user_register/create/$', views.UserCreateView, name='user-create'),
    # re_path(r'^user_register/$', djoser_views.UserCreateView.as_view(), name='user-create'),
    # Views are defined in Rest Framework JWT, but we're assigning custom paths.
    re_path(r'^user_login/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^user_login/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
