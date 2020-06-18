from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin
from .views import SearchResultsView

from . import views
# from sklt_sns1.views import PostListView, PostDetailView
admin.autodiscover()

urlpatterns = [
    path('post_list', views.home2, name='home2'),
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
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # url(r'^hitcount-detail-view/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name="detail"),
    # url(r'^home/$', views.IndexView.as_view(), name="index"),
    url(r'^$', views.IndexView.as_view(), name="index"),


    url(r'^generic-detail-view-ajax/(?P<pk>\d+)/$',
        views.PostDetailJSONView.as_view(),
        name="ajax"),
    url(r'^hitcount-detail-view/(?P<pk>\d+)/$',
        views.PostDetailView.as_view(),
        name="detail"),
    url(r'^hitcount-detail-view-count-hit/(?P<pk>\d+)/$',
        views.PostCountHitDetailView.as_view(),
        name="detail-with-count"),

    # for our built-in ajax post view
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
]

try:
    urlpatterns.append(url(r'^admin/', include(admin.site.urls)))
except:
    urlpatterns.append(url(r'^admin/', admin.site.urls))

 