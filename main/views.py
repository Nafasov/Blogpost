from django.shortcuts import render


def home_view(request):

    context = {

    }
    return render(request, 'main/index.html', context)


def contact_view(request):

    context = {

    }
    return render(request, 'main/contact.html', context)