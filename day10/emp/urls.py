from django.urls import path
from emp import views

urlpatterns=[
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('abc/',views.contact,name="abc"),
	path('log/',views.login,name="lg"),
]