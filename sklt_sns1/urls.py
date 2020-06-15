from django.urls import path, include
from django.conf.urls import include, url

from . import views
# from sklt_sns1.views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='home'),
    # path('post_detail',views.post_detail),
    # path('profile',views.profile),
    # path('search_result',views.search_result),
    # path('log_in_page',views.log_in_page),
    # path('hello/', PostListView.as_view(), name='posts'),
    # path('<slug:slug>/', PostDetailView.as_view(), name='detail'),
    # path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    #各記事の個別ページ
    path('post_detail1/<int:pk>/', views.post_detail1, name='post_detail1'),
    #コメント投稿
    path('post_detail/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #いいね
    path('good/<int:pk>', views.good, name='good'),
    #編集
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    url(r'^hitcount-detail-view/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name="detail"),
]
 