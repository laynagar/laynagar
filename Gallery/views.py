from django.shortcuts import render
from .models import PictureCategoryModel, PictureModel
from django.views.generic import TemplateView, ListView, FormView
from .forms import ContactForm
from django.urls import reverse_lazy



class IndexView(ListView):
    template_name = 'Gallery/index.html' 
    model = PictureModel
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context

class PortfolioView1(ListView):
    model = PictureModel
    template_name = 'Gallery/portfolio.html'
    paginate_by = 12


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PictureCategoryModel.objects.distinct()
        return context


class PortfolioView2(ListView):
    model = PictureModel
    paginate_by = 9
    template_name = 'Gallery/portfolio-1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PictureCategoryModel.objects.distinct()
        return context

class PortfolioView3(ListView):
    model = PictureModel
    # paginate_by = 10  
    template_name = 'Gallery/portfolio-2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = PictureCategoryModel.objects.distinct()
        return context

class Contact(FormView):
    template_name = 'Gallery/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('Gallery:index')

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)
    

class About(TemplateView):
    template_name = 'Gallery/about.html'