from django.shortcuts import render
from django.views.generic import  (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'

class PostDetailView(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single_post'

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ["title", "subtitle", "body", "status"]