from django.urls import path

from image_converter.views import png_to_jpg

app_name = 'img_converter'

urlpatterns = [
    path('png-to-jpg', png_to_jpg, name="homepage"),
]
