
from django.contrib import admin
from django.urls import path
from shopapp import views

urlpatterns = [
    path("viewallproduct/",views.viewallproduct, name="/shopapp/viewallproduct/"),
    path("newproduct/",views.newproduct.as_view(),name="/shopapp/newproduct/"),
    path("signup/",views.signup,name="/shopapp/signup/"),
    path('delete/<pk>',views.ProductDelete.as_view()),
    path('update/<pk>',views.ProductUpdate.as_view()),

]