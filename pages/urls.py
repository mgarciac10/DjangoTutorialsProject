from django.urls import path
from .views import homePageView, aboutPageView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about')
]