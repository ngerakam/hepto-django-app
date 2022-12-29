from django.shortcuts import render, redirect

from blog.models import Article, ProfileDetails

from .models import Volunteer

from .forms import VolunteerForm

# pagination
from django.core.paginator import Paginator


def Home(request):
    user = request.user.id

    if user:

        profile = ProfileDetails.objects.filter(user=user)

        paginated_article = Paginator(Article.objects.all(), 2)

        page = request.GET.get("page")

        article = paginated_article.get_page(page)

        context = {"article": article, "profile": profile}

        return render(request, 'main/index.html', context)
    else:
        paginated_article = Paginator(Article.objects.all(), 2)

        page = request.GET.get("page")

        article = paginated_article.get_page(page)

        context = {"article": article}

        return render(request, 'main/index.html', context)


def Glance(request):
    return render(request, 'main/about.html')


def Strategy(request):
    return render(request, 'main/strategic.html')


# def Goals(request):
#     return render(request, 'main/test.html')


def Health(request):
    return render(request, 'main/403.html')


def Error_403(request):
    return render(request, 'main/403.html')


def Health1(request):
    return render(request, 'blog/blog-user/index.html')


def Health2(request):
    return render(request, 'main/404.html')


def Services(request):
    return render(request, 'main/500.html')


def Kenya(request):
    return render(request, 'main/404.html')


def Somalia(request):
    return render(request, 'main/500.html')


def Ethiopia(request):
    return render(request, 'main/403.html')


def Donate(request):
    return render(request, 'main/donate.html')


# def Fundraise(request):
#     return render(request, 'main/test.html')


def Campaign(request):
    return render(request, 'main/408.html')


def Volunteer(request):
    if request.method == 'POST':

        form = VolunteerForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect('home')
    else:

        form = VolunteerForm()

        context = {"form": form}

        return render(request, 'main/volunteer.html', context)


# Errors

def Status_403(request):
    return render(request, 'main/403.html')


def Status_404(request):
    return render(request, 'main/404.html')


def Status_408(request):
    return render(request, 'main/408.html')


def Status_500(request):
    return render(request, 'main/500.html')
