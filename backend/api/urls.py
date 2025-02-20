from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name='home'),
    path('scrape_jobs', scrape_jobs, name='scrape_jobs'),
]
