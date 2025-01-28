from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.indexpage,name="index.html"),
   path('login',views.loginpage,name="login.html"),
   path('register',views.registerpage,name="register.html"),
   path('checkout',views.checkoutpage,name="checkout.html"),
   path('furniture',views.furniturepage,name="furniture.html"),
   path('mail', views.mailpage, name="mail.html"),
   path('products', views.productspage, name="products.html"),
   path('short-codes', views.shoetcodespage, name="short-codes.html"),
   path('single', views.singlepage, name="single.html"),
   path('fetchdata', views.fetchdata, name="fetchdata"),
   path('checklogindata', views.checklogindata, name="checklogindata"),
   path('categorywiseproduct/<int:id>', views.categorywiseproduct, name="categorywiseproduct"),
   path('singlepage/<int:id>', views.singlepage, name="singlepage"),
   path('addtocart', views.addtocart, name="addtocart"),
   path('hamper', views.hamperpage, name="hamper.html"),
   path('singleHamper', views.singleHamperpage, name="singleHamper.html"),
   path('singleHamperpage/<int:id>', views.singleHamperpage, name="singleHamperpage"),
   path('delete/<int:id>',views.deleteproduct,name="deleteproduct"),
   path('fetchinquiry',views.fetchinquiry,name="fetchinquiry"),
   path('placeorder',views.placeorder,name="placeorder"),
   path('fetchfeedback',views.fetchfeedback,name="fetchfeedback"),
   path('feedbackpage', views.feedbackpage, name="feedbackpage"),
   path('orderpage', views.orderpage, name="orderpage"),
   path('singleorderpage/<int:id>', views.singleorderpage, name="singleorderpage"),
]