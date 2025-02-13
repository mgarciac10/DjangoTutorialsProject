from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class AboutPageView(TemplateView):
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

class ContactPageView(TemplateView):
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

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price":"1000"}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":"800"}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":"50"}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":"100"} 
    ]

class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.products 

        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):

        if int(id) > len(Product.products) or int(id) < 1:
            return HttpResponseRedirect('/')

        viewData = {} 
        product = Product.products[int(id)-1] 
        viewData["title"] = product["name"] + " - Online Store" 
        viewData["subtitle"] =  product["name"] + " - Product information" 
        viewData["product"] = product 
 
        return render(request, self.template_name, viewData)

class ProductForm(forms.Form): 
    name = forms.CharField(required=True) 
    price = forms.FloatField(required=True) 

class ProductCreateView(View): 
    template_name = 'products/create.html' 
 
    def get(self, request): 
        form = ProductForm() 
        viewData = {} 
        viewData["subtitle"] = "Create product" 
        viewData["form"] = form 
        return render(request, self.template_name, viewData) 
 
    def post(self, request): 
        form = ProductForm(request.POST) 
        if form.is_valid():
            name = form.cleaned_data["name"]
            price = form.cleaned_data["price"]
            if price < 0:
                form.add_error("price", "Price must be greater than 0")
                return render(request, self.template_name, {"form":form})
            Product.products.append({"id":str(len(Product.products)+1), "name":name, "price":price})     
            return redirect('created')
        else: 
            viewData = {} 
            viewData["title"] = "Create product" 
            viewData["form"] = form 
            return render(request, self.template_name, viewData)

class ProductCreatedView(TemplateView):
    template_name = 'products/productCreated.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Product created - Online Store',
            'subtitle': 'Create product',
            'message': 'Product created successfully'
        })
        return context