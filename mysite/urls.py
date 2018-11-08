from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login' ),
    path('accounts/logout/',LogoutView.as_view(), name='logout' ),
    url(r'', include('blog.urls')),
]