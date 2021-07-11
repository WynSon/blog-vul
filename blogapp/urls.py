from django.urls import path
from blogapp.views.post import post
from blogapp import views


urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.blog, name="blog"),
    path('blog/<pid>/', views.blog, name="blog"), # parameter 'pid' phai trung ten voi agrument 'pid' trong view blog
    path('post/<id>/', views.post, name="post"),
    path('search/', views.search, name="search"), 
    path('setting/', views.setting , name="setting"),
    path('register/', views.register, name="register"),
    path('login', views.login_view, name="user_login"),
    path('logout/', views.logout_view, name="user_logout"),
    path('tag/<tag>/', views.tags, name="tags"),
]
