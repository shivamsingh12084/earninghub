from django.urls import path
from .views import HomePageView, AuthenticationPageView, SearchPageView # new

urlpatterns = [
    path('authentication/', AuthenticationPageView.as_view(), name='auth'),
    path('search/', SearchPageView.as_view(), name='search'), # new
    path('', HomePageView.as_view(), name='home'),
]