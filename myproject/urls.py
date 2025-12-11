"""
URL configuration for myproject project.
"""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.http import JsonResponse
import datetime

def home(request):
    """Home page view"""
    return render(request, 'home.html', {
        'title': 'Modern Django App',
        'welcome_message': 'Welcome to our Modern Django Application!',
        'current_time': datetime.datetime.now(),
        'features': [
            'Modern Dashboard UI',
            'Real-time Health Monitoring',
            'Interactive Components',
            'Responsive Design',
            'Easy Deployment',
            'API Documentation'
        ]
    })

def health_check(request):
    """Health check view - returns JSON for API, HTML for browser"""
    if 'application/json' in request.headers.get('Accept', ''):
        return JsonResponse({
            'status': 'healthy',
            'service': 'simple-django-app',
            'timestamp': datetime.datetime.now().isoformat(),
            'version': '2.0.0',
            'uptime': '99.9%'
        })
    return render(request, 'health.html', {
        'status': 'healthy',
        'timestamp': datetime.datetime.now(),
        'metrics': {
            'cpu': 24,
            'memory': 68,
            'disk': 42,
            'response_time': 125
        }
    })

def dashboard(request):
    """Dashboard view"""
    return render(request, 'dashboard.html', {
        'title': 'Dashboard',
        'stats': {
            'uptime': '99.9%',
            'requests': 1250,
            'users': 42,
            'response_time': '125ms'
        },
        'current_time': datetime.datetime.now()
    })

def api_docs(request):
    """API Documentation view"""
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
    path('core/', include('core.urls')),
]
