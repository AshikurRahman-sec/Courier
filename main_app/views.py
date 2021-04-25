from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import *

# Create your views here.

class Home(View):
    template_name = 'home.html'
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)


class Signup(View):
    def get(self,request,*args,**kwargs):
        return render(request,'signup.html')

    def post(self,request,*args,**kwargs):
        u = User()
        u.username = request.POST['username'] 
        u.set_password(request.POST['psw'])
        u.save()
        m = Merchant()
        m.user= u
        m.save()
        return HttpResponseRedirect(reverse("login"))

class LoginView(View):
    
    def get(self, request, *args, **kwargs):
           return render(request,'login.html') 
    
    def post(self, request):
        password = request.POST['psw']
        username = request.POST['uname']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request,'login.html',{'error':1})
        
        
        

class Logout(View):
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect(reverse('login'))

def create_order(request):
    forms = OrderForm()
    if request.user.is_superuser:
        if request.method == 'POST':
            print("Bangladesh is my country")
            print(request.POST)
            o = Order()
            o.merchant = Merchant.objects.get(id=request.POST['merchant'])
            o.product_type = request.POST['product_type']
            o.location = request.POST['location']
            o.price = request.POST['price']
            o.save()
            return HttpResponseRedirect(reverse('orderlist'))
        context = {
            'form': forms
        }
        return render(request, 'create_order.html', context)
    else:
        context={
            'check':1
        }
        return render(request, 'login.html', context)
class OrderList(View):
    
    def get(self, request, *args, **kwargs):
        """
        if request.user.is_authenticated:
            logout(request)
        """
        context= {
            'orders':Order.objects.all()
        }
        return render(request,'order_list.html',context)
