# docanalyzer/urls.py
from django.contrib import admin
from django.urls import path
from analyzer.views import analyze_url, revise_content

urlpatterns = [
    path('admin/', admin.site.urls),
    path('analyze/', analyze_url),
    path('revise/', revise_content),
]

