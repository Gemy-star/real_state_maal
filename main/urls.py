from django.urls import path
from .views import HomePageView , SoonPageView


urlpatterns = [
    path("home", HomePageView.as_view(), name="home-page"),
    path("", SoonPageView.as_view(), name="soon-page"),

]
