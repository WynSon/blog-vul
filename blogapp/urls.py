from blogapp.views.tags import tagsView
from blogapp.views.register import registerView
from blogapp.views.index import indexView
from blogapp.views import *
from django.urls import path, re_path
# from blogapp.views.post import post


urlpatterns = [
    path('', indexView.as_view(), name="index"),
    path('blog/', blogView.as_view(), name="blog"),
    path('blog/<pid>/', blogView.as_view(), name="pagination"), # parameter 'pid' phai trung ten voi agrument 'pid' trong view blog
    path('post/<id>/', postView.as_view(), name="post"),
    path('search/', searchView.as_view(), name="search"), 
    path('setting/', settingView.as_view() , name="setting"),
    path('register/', registerView.as_view(), name="register"),
    path('login', loginView.as_view(), name="user_login"),
    path('logout/', logoutView.as_view(), name="user_logout"),
    path('tag/<tag>/', tagsView.as_view(), name="tags"),
    re_path(r'profile/(?P<id>[\w])?/', profileView.as_view(), name="profile"),
]