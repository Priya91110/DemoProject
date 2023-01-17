from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from shopapp.models import NewProduct
from django.contrib.auth.models import User,auth
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse
from .forms import SignupForm
from django.contrib import messages #import messages
# Create your views here.


def home(request) :
    return render(request, "shopapp/index.html")


def signup(request):
    form=SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect("/accounts/login/")
    else:
        form=SignupForm()
    return render(request,"shopapp/signup.html",{"form":form})    

class newproduct(CreateView):
    model=NewProduct
    fields="__all__"
    def get_success_url(self):
        return reverse("/shopapp/viewallproduct/")

def viewallproduct(request) :
    newproductdata=NewProduct.objects.all()
    return render(request, "shopapp/viewallproduct.html",{"newproductdata":newproductdata})



class ProductDelete(DeleteView):
    model = NewProduct
    def get_success_url(request):
        return reverse("/shopapp/newproduct/")

class ProductUpdate(UpdateView):
    model = NewProduct
    fields="__all__"
    def get_success_url(self):
        return reverse("/shopapp/newproduct/")
    
    
# class UpdateProduct(UpdateView):
#     model=NewProduct
#     fields='__all__'
#     def get_success_url(self):
#         return reverse("home")

# class DeleteProduct(DeleteView):
#     model=NewProduct
#     fields='__all__'
#     def get_success_url(self):
#         return reverse("home")
