from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse("<h2 style='color:white;background-color:green'>Welcome to Home Page</h2>")


def chk(request):
	return HttpResponse("<script>alert('hi good afternoon')</script><h2>welcome</h2>")


def homepage(request):
	return render(request,'rm/homepage.html')

def lgn(re):
	return render(re,'rm/login1.html')

def reg(rt):
	return render(rt,'rm/register.html')

def bthm(qw):
	return render(qw,'rm/bthome.html')

def about(req):
	return render(req,'rm/about.html')

def contact(req):
	return render(req,'rm/contact.html')