from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from blog.forms import RegisterForm, LoginForm, ArticleForm
from blog.models import Article

class ArticleView(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    extra_context = {
        "title":"News"
    }

class ArticleByCategory(ArticleView):
    extra_context = {
        "title":"Category"
    }
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'])

class ArticleDetail(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "blog/detail.html"
    extra_context = {
        "title":"Detail"
    }

    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    context = {
        "title":"Register",
        "form":form
    }
    return render(request,"blog/register.html", context)

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    context = {
        "title":"Login",
        "form":form
    }
    return render(request,"blog/login.html", context)

def user_logout(request):
    logout(request)
    return redirect('index')

# def add_article(request):
#     if request.method == "POST":
#         form = ArticleForm(data=request.POST)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.user = request.user
#             article.save()
#             return redirect("index")
#     else:
#         form = ArticleForm()
#     context = {
#         "title":"add",
#         "form":form
#     }
#     return render(request, "blog/add_article.html", context)

class AddArticle(CreateView):
    model = Article
    template_name = "blog/add_article.html"
    form_class = ArticleForm

class EditArticle(UpdateView):
    model = Article
    template_name = "blog/add_article.html"
    form_class = ArticleForm