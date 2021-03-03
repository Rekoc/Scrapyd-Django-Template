from django.urls import path
from main.views import crawl

urlpatterns = [
    path('crawl/', crawl)
]