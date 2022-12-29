from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group, User
from .models import *

from django.db.models import Q
#
from django.contrib import messages
from .forms import CreateUserForm, ArticlesForm

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticateduser, allowed_users

# pagination
from django.core.paginator import Paginator


@unauthenticateduser
def Register_User(request):

    if request.method == 'POST':
        login_form = CreateUserForm(request.POST)

        if login_form.is_valid():
            user = login_form.save()

            username = login_form.cleaned_data.get('username')

            group = Group.objects.get(name='basic')
            user.groups.add(group)
            Author.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )

            ProfileDetails.objects.create(
                user=user
            )

            messages.success(
                request, 'You are successfuly registered!! ' + username)

        return redirect('login')

    else:

        login_form = CreateUserForm()

        context = {'login_form': login_form}

        return render(request, 'registration/signup.html', context)


def Login_User(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            print(user)

            return redirect('status')

        else:
            messages.error(request, "Invalid Password")
            return redirect("login")

    else:

        return render(request, 'registration/login.html',)


@login_required(login_url='login')
def Logout(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')


def Blog(request):
    tags = Tag.objects.all()
    art = Article.objects.all()

    paginated_article = Paginator(Article.objects.all(), 2)

    # paginated for side bar
    paginated_article_sb = Paginator(Article.objects.all(), 5)

    page = request.GET.get("page")

    article = paginated_article.get_page(page)

    article_sb = paginated_article_sb.get_page(page)

    context = {"article": article, "tags": tags,
               "art": art, "article_sb": article_sb}
    return render(request, 'blog/index.html', context)


def BlogDetail(request, pk):
    single = Article.objects.get(id=pk)
    tags = Tag.objects.all()

    profile_user = ProfileDetails.objects.get(user=single.author.user)

    paginated_article_sb = Paginator(Article.objects.all(), 5)

    page = request.GET.get("page")

    article_sb = paginated_article_sb.get_page(page)

    categories = Category.objects.filter(featured_article=single)
    context = {"single": single, "tags": tags,
               "categories": categories, "article_sb": article_sb, "profile_user": profile_user}

    return render(request, 'blog/single-blog.html', context)


def Tag_articles(request, pk):
    single_tag = Tag.objects.get(id=pk)
    tags = Tag.objects.all()

    paginated_article = Paginator(Article.objects.filter(tag=single_tag), 2)

    paginated_article_sb = Paginator(Article.objects.all(), 5)

    page = request.GET.get("page")

    article_sb = paginated_article_sb.get_page(page)

    article = paginated_article.get_page(page)

    context = {"article": article, "tags": tags, "article_sb": article_sb}
    return render(request, 'blog/cat_blog.html', context)


def search(request):
    if request.method == 'POST':
        keyword = request.POST['searched']

        art = Article.objects.filter(
            Q(content__icontains=keyword) | Q(title__icontains=keyword))

        paginated_article = Paginator(art, 2)
        page = request.GET.get("page")

        article = paginated_article.get_page(page)

        tags = Tag.objects.all()
        paginated_article_sb = Paginator(Article.objects.all(), 5)
        article_sb = paginated_article_sb.get_page(page)

        context = {"article": article,
                   "tags": tags, "article_sb": article_sb}

        return render(request, 'blog/search-blog.html', context)
    else:

        tags = Tag.objects.all()
        art = Article.objects.all()

        paginated_article = Paginator(Article.objects.all(), 2)

        # paginated for side bar
        paginated_article_sb = Paginator(Article.objects.all(), 5)

        page = request.GET.get("page")

        article = paginated_article.get_page(page)

        article_sb = paginated_article_sb.get_page(page)

        context = {"article": article, "tags": tags,
                   "art": art, "article_sb": article_sb}
        return render(request, 'blog/index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['author', 'basic'])
def Status(request):
    # pk=request.user.id
    author = request.user
    articles = request.user.author.article_set.all()

    profile = ProfileDetails.objects.get(user=author)

    number = articles.count()

    context = {'articles': articles, 'number': number,
               "author": author, "profile": profile}
    return render(request, 'blog/blog-user/index.html', context)


#


@login_required(login_url='login')
@allowed_users(allowed_roles=['author'])
def Add_Article(request, pk):

    author = Author.objects.get(id=pk)
    form = ArticlesForm()

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)

        if form.is_valid():
           # My niddle in a haystack
            form = form.save(commit=False)
            form.author = request.user.author
            form.save()
            return redirect('status')

    context = {'form': form, "author": author,
               }
    return render(request, 'blog/blog-user/add-article.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['author'])
def Edit_Article(request, pk):

    article = Article.objects.get(id=pk)
    form = ArticlesForm(instance=article)

    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES, instance=article)
        # print(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user.author
            form.save()
            return redirect('status')

    context = {'form': form, "article": article,
               }
    return render(request, 'blog/blog-user/edit-article.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['author'])
def delete_article(request, pk):

    article = Article.objects.get(id=pk)

    if request.method == 'POST':

        article.delete()
        return redirect('status')

    context = {'form': article}
    return render(request, 'blog/blog-user/delete_article.html', context)
