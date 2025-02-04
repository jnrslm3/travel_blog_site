from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import *
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-created_at')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['popular'] = Post.objects.all()[:4]
        context['tags'] = Tag.objects.all()[:7]
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'
    queryset = Post.objects.all()
