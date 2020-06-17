from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from hitcount.views import HitCountDetailView
from django.contrib import admin
from django.views.generic.list import ListView
# Create your views here.
from django.contrib.auth.decorators import login_required


from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, TemplateView
from django.views.generic.list import ListView

from hitcount.views import HitCountDetailView

from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from hitcount.views import HitCountDetailView

from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import *
from django.contrib import messages
from django.db.models import Q


def home(request):
    # posts=Post.objects.order_by('-created_date')
    # latest_posts = []
    # for i in range(6):
    #     latest_posts.append(posts[i])

    # context={'posts':posts,'latest_posts':latest_posts}
    # return render(request, 'sklt_sns1/home.html',context)
    posts = Post.objects.order_by('-created_date')
    keyword = request.GET.get('keyword')
    latest_posts = []
    if keyword:
        posts1 = posts.filter(
                 Q(text__icontains=keyword) | Q(author__name__icontains=keyword)
               )
        for i in posts1:
            latest_posts.append(i)
        
        messages.success(request, '「{}」の検索結果'.format(keyword))
    else:
        for i in range(6):
            latest_posts.append(posts[i])
    context={'posts':posts,'latest_posts':latest_posts}
    return render(request, 'sklt_sns1/home.html',context)

def post_detail1(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'sklt_sns1/post_detail1.html', {'post': post})

#投稿の編集ページ
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail1', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sklt_sns1/post_edit.html', {'form': form})

#削除する
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('profile')


#投稿に対するコメント投稿
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail1', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'sklt_sns1/post_detail1.html', {'form': form})

#いいね
def good(request, pk):
    """いいねボタンをクリック."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # データの新規追加
        post.good += 1
        post.save()
    return redirect('post_detail1', pk=post.pk)


def profile(request):
    return HttpResponse('Profile')

def search_result(request):
    return HttpResponse('Search result')

def log_in_page(request):
    return HttpResponse('Log in page')


# from django.views.generic.list import ListView
# from hitcount.views import HitCountDetailView
# from .models import Post

# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     template_name = 'post_list.html'


# class PostDetailView(HitCountDetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     context_object_name = 'post'
#     slug = 'slug'

#     # slug_field = 'slug'
#     # set to True to count the hit
#     count_hit = True

#     def get_context_data(self, **kwargs):
#         context = super(PostDetailView, self).get_context_data(**kwargs)
#         context.update({
#         'popular_posts': Post.objects.order_by('-hit_count_generic__hits')[:3],
#         })
#         return context

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import DetailView, TemplateView

from hitcount.views import HitCountDetailView



class PostMixinDetailView(object):
    """
    Mixin to same us some typing.  Adds context for us!
    """
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostMixinDetailView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all()
        context['post_views'] = ["detail-with-count"]
        context['popular_posts'] = Post.objects.order_by('hit_count_generic')[:3]
        context['latest_posts'] = Post.objects.order_by('-created_date')[:4]

        return context


class IndexView(PostMixinDetailView, TemplateView):
    template_name = 'sklt_sns1/index.html'

class PostDetailView(PostMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view.
    """
    pass


class PostCountHitDetailView(PostMixinDetailView, HitCountDetailView):
    """
    Generic hitcount class based view that will also perform the hitcount logic.
    """
    count_hit = True



class PostDetailJSONView(PostMixinDetailView, DetailView):
    template_name = 'sklt_sns1/post_ajax.html'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(PostDetailJSONView, cls).as_view(**initkwargs)
        return ensure_csrf_cookie(view)