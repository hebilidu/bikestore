from django.shortcuts import render, HttpResponse, redirect
from .models import Customer, Vehicle, Rental
# from .forms import CategoryForm, GifForm
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.

class CustomerListView(generic.ListView):
    queryset = Customer.objects.all().order_by('l_name', 'f_name')


class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')


class CustomerDetailView(generic.DetailView):
    model = Customer


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('all_customers')
