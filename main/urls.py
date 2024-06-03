from django.urls import path
from .views import HomePageView, SoonPageView, AboutPageView


urlpatterns = [
    path("home", HomePageView.as_view(), name="home-page"),
    path("", SoonPageView.as_view(), name="soon-page"),
    path("about", AboutPageView.as_view(), name="about-page"),
]
