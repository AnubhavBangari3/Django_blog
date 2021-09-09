
from django.urls import path
#from . import views
from . views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,CategoryView,CategoryListView,LikeView,AddCommentView

urlpatterns = [
    #path("",views.home,name="home"),
    path("",HomeView.as_view(),name="home"),
    path("article/<str:pk>",ArticleDetailView.as_view(),name="article-detail"),
    path("add_post/",AddPostView.as_view(),name="add_post"),

    # path("add_category/",AddCategoryView.as_view(),name="add_category"),
    path("article/edit/<str:pk>",UpdatePostView.as_view(),name="update_post"),
    path("article/<str:pk>/remove",DeletePostView.as_view(),name="delete_post"),
    path("category/<str:cat>/",CategoryView,name='category'),
    path("category-list/",CategoryListView,name='category-list'),
    path("like/<int:pk>",LikeView,name="like_post"),

    path("article/<int:pk>/add_comment/",AddCommentView.as_view(),name="add_comment"),
   
]