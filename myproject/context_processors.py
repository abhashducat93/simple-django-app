"""
Global context processors for templates.
"""

from django.conf import settings
from datetime import datetime

def global_context(request):
    """Add global context variables to all templates"""
    return {
        'app_name': settings.APP_NAME,
        'app_version': settings.APP_VERSION,
        'app_description': settings.APP_DESCRIPTION,
        'current_year': datetime.now().year,
        'is_debug': settings.DEBUG,
        'current_time': datetime.now(),
    }
