from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import ContactUsForm, SubscriptionForm
from ..posts.models import Post , Tag
from ..accounts.models import User

# Create your views here.

class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()[:4]
        context['tags'] = Tag.objects.all()[:7]
        context['popular'] = Post.objects.all()[3::-1]
        return context


class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'




