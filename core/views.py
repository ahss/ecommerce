from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {
        'categories': ['kids', 'fashion', 'bags', 'shoes']
    }
    return render(request, 'core/index.html', context)
