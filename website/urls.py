from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', views.home, name='home'),
    path('external', views.external),

]

urlpatterns += staticfiles_urlpatterns()