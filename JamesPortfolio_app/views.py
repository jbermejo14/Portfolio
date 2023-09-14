from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

topics = [
    {'name': 'Django'},
    {'name': 'Python'},
    {'name': 'Html'},
]


def index(request):
    return render(request, 'jbb/index.html', {'topics': topics})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'jbb/SContact.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'jbb/contact.html', context)


def about(request):
    return render(request, 'jbb/about.html')


def blog(request):
    return render(request, 'jbb/blog.html')


def article_1(request):
    return render(request, 'jbb/articles/article-1.html')
