from django.urls import path
from .views import homePageView, aboutPageView, contactPageView, productIndexView, productShowView

urlpatterns = [
    path('', homePageView.as_view(), name='home'),
    path('about/', aboutPageView.as_view(), name='about'),
    path('contact/', contactPageView.as_view(), name='contact'),
    path('products/', productIndexView.as_view(), name='index'),
    path('products/<str:id>', productShowView.as_view(), name='show')
]