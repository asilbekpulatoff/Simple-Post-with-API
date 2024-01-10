from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView

from django.urls import reverse_lazy
from post.models import Post
from post.forms import PostCreateForm, PostEditForm


def home(request):
    posts = Post.objects.filter(public=True).order_by('-created')
    return render(request, 'home.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created']

    def get_queryset(self):
        queryset = super().get_queryset().filter(public=True)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.public = True
        return super().form_valid(form)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, public=True)
    return render(request, 'post/post_detail.html', {'post': post})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk, public=True)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostEditForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk, public=True)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'post/post_delete.html', {'post': post})

