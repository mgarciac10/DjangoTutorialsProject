from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class homePageView(TemplateView):
    template_name = 'pages/home.html'

class aboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'About us - Online Store',
            'subtitle': 'About us',
            'description': 'This is an about page...',
            'author': 'Developed by: Mateo Garcia'
        })
        return context

class contactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Contact - Online Store',
            'subtitle': 'Contact',
            'email': 'onlinestore@mail.com',
            'address': '4702 University Ave, San Diego, California',
            'phoneNumber': '(619) 283-7031'
        })
        return context

