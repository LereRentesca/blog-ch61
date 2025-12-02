from django.shortcuts import render
from django.views.generic import  (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic.edit import FormMixin
from .forms import CommentForm

from .models import Post, Status
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    template_name = 'posts/list.html'
    #model = Post
    context_object_name = 'posts'

    published_status = Status.objects.get(name="Published")
    # Queryset attribute allow us to select some data from the database by using the model class
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()

class PostDetailView(LoginRequiredMixin, FormMixin, DetailView): #GET request and POST request
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'single_post'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('post_detail',kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        context['comments'] = post.comments.all().order_by('-created_on')
        if 'form' not in context:
            context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
            
class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = [
        "title", "subtitle", "body", "status"
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    template_name = 'posts/delete.html'
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'posts/edit.html'
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        post = self.get_object()
        if self.request.user.is_authenticated:
            if self.request.user == post.author:
                return True
            else:
                return False
        else:
            return False