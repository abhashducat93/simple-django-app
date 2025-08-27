from django.contrib import admin
from django.http import JsonResponse
from django.urls import path

def home(request):
    return JsonResponse({
        'message': 'Welcome to Simple Django App!',
        'status': 'success'
    })

def health_check(request):
    return JsonResponse({
        'status': 'healthy',
        'service': 'simple-django-app'
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('health/', health_check),
]
