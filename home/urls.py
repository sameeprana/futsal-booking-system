import imp
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from home import views

admin.site.site_header = "Futsal Admin"
admin.site.site_title = "Futsal Admin Portal"
admin.site.index_title = "Welcome to Futsal Researcher Portal"

urlpatterns = [
    path("",views.index, name='home'),
    path("home",views.index,name=''),
    path("news",views.news, name="news"),
    path("events",views.events, name="events"),
    path("bookings",views.bookings_list, name="bookings"),
    path("showbookings",views.showbookings,name="showbookings"),
    path("login",views.login, name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout, name="logout"),
    path("profile",views.profile, name = "profile"),
    path("payment",views.payment, name="payment"),
    path("delete/<str:product_id>",views.cancelBookings, name="delete"),
    path("update/<id_user>", views.updateProfile,name="update"),
    path("aboutus",views.Aboutus,name="aboutus"),
    path("helpcentre",views.helpcentre,name="helpcentre"),
    path("khaltirequest/<str:price><str:product_id>",views.khaltirequest,name="khaltirequest"),
    path("khaltiVerify",views.khaltiVerify,name="khaltiVerify")
  
    
    
     
    
    

]

urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)