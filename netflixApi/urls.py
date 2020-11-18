from django.urls import include,path,re_path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('youtube/',views.youtube,name = 'home')
]