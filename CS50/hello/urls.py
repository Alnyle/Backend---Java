from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Elniel", views.Elniel, name="Elniel"),
    # path("SignUp", views.signUp, name="signUp"),
    path("<str:name>", views.greet, name="greet"),
]
