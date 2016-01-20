from django.shortcuts import render

# Create your views here.


def hello(request):
    context = {
        'texto': 'Shiro'
    }
    return render(request, 'core/index.html', context)
