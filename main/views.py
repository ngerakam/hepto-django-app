from django.shortcuts import render

from blog.models import Article

# pagination
from django.core.paginator import Paginator


def Home(request):

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
    return render(request, 'main/volunteer.html')


# Errors

def Status_403(request):
    return render(request, 'main/403.html')


def Status_404(request):
    return render(request, 'main/404.html')


def Status_408(request):
    return render(request, 'main/408.html')


def Status_500(request):
    return render(request, 'main/500.html')
