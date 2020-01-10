from django.urls import path
from .import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("prices/", views.prices, name="prices"),
    path("contact/", views.contact, name="contact"),
]