from django.shortcuts import render


def django(request):
    return render(request, 'django.html', {'stylesheet': 'style1.css'})


def display(request):
    return render(request, 'display.html', {'stylesheet': 'style1.css'})


def templates(request):
    return render(request, 'templates.html', {'stylesheet': 'style2.css'})
