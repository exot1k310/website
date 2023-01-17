from django.urls import path
from .views import SignUpView
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("coment/new", views.comm_new, name="comm_new"),
    path("kabinet/<int:pk>/", views.kab_detail, name="kab_detail")
]