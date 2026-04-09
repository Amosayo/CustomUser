
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name ="index"),
     path("about/", views.about, name ="aboutus"),
      path("products/", views.products, name ="products"),
]