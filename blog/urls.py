from django.urls import path

from blog.views import *

urlpatterns = [
    path("", ArticleView.as_view(), name="index"),
    path("category/<int:pk>/", ArticleByCategory.as_view(), name="category"),
    path("article/<int:pk>/", ArticleDetail.as_view(), name="detail"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("add_article/", AddArticle.as_view(), name="add"),
    path("edit/<int:pk>/", EditArticle.as_view(), name="edit"),
]