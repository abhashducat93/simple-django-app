from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import JsonResponse
import datetime

def home(request):
    return render(request, 'home.html', {
        'title': 'Simple Django App',
        'welcome_message': 'Welcome to our Modern Django Application!',
        'current_time': datetime.datetime.now(),
        'features': [
            'Modern Dashboard UI',
            'Real-time Health Monitoring',
            'Interactive Components',
            'Responsive Design',
            'Easy Deployment'
        ]
    })

def health_check(request):
    # Return both HTML and JSON based on request
    if 'application/json' in request.headers.get('Accept', ''):
        return JsonResponse({
            'status': 'healthy',
            'service': 'simple-django-app',
            'timestamp': datetime.datetime.now().isoformat(),
            'version': '2.0.0'
        })
    return render(request, 'health.html', {
        'status': 'healthy',
        'timestamp': datetime.datetime.now()
    })

def dashboard(request):
    return render(request, 'dashboard.html', {
        'title': 'Dashboard',
        'stats': {
            'uptime': '99.9%',
            'requests': 1250,
            'users': 42,
            'response_time': '125ms'
        }
    })

def api_docs(request):
    return render(request, 'api_docs.html', {
        'title': 'API Documentation',
        'endpoints': [
            {'path': '/', 'method': 'GET', 'description': 'Home Page'},
            {'path': '/health/', 'method': 'GET', 'description': 'Health Check'},
            {'path': '/dashboard/', 'method': 'GET', 'description': 'Dashboard'},
            {'path': '/api/docs/', 'method': 'GET', 'description': 'API Documentation'},
            {'path': '/admin/', 'method': 'GET', 'description': 'Admin Panel'}
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('health/', health_check, name='health'),
    path('dashboard/', dashboard, name='dashboard'),
    path('api/docs/', api_docs, name='api_docs'),
]
