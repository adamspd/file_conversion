from django.urls import path

from legal.views import homepage

app_name = 'legal'

urlpatterns = [
    path('', homepage, name="homepage"),
]
