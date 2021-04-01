from django.urls import path
from pstp import views

urlpatterns=[
	path('rt/',views.home,name="home"),
	path('demo/',views.chk),
	path('home/',views.homepage),
	path('lg/',views.lgn),
	path('rg/',views.reg,name="reg"),
	path('',views.bthm),
	path('about/',views.about,name="about"),
	path('contact/',views.contact,name="contact"),
]