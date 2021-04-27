from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment

# Create your views here.


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']
    paginate_by = 10


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'author', 'body']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/accounts/login/'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')


class CommentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = Comment
    # template_name = 'comment.html'
    template_name = 'post_detail.html'
    fields = ['comment', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['post_pk'])
        return super().form_valid(form)
