from django.shortcuts import render


def png_to_jpg(request):
    return render(request, 'img/png_to_jpg.html')
