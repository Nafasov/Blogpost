from django.shortcuts import render


def article_view(request):

    context = {

    }
    return render(request, 'article/archive.html', context)


def article_detail_view(request):

    context = {

    }
    return render(request, 'article/single-blog.html', context)


def element_view(requests):

    context = {

    }
    return render(requests, 'article/elements.html', context)