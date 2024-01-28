from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q


from .models import Contact
from .forms import ContactForm
from article.models import Article, Tags, Category


def home_view(request):
    q = request.GET.get('q')
    tags = Tags.objects.order_by("-id")
    categories = Category.objects.order_by("-id")
    articles = Article.objects.order_by('-id')[3:9:]
    if q:
        q = Q(title__icontains=q)
        articles = Article.objects.filter(q).order_by('-id')

    context = {
        'object_list': articles,
        'tags': tags,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def contact_view(request):
    forms = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST, request.FILES)
        if contact.is_valid():
            contact.save()
            messages.success(request, 'Contact sent successfully!')
            return redirect('.')
    context = {
        'forms': forms,

    }
    return render(request, 'main/contact.html', context)