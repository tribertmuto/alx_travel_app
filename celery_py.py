"""
Celery configuration for alx_travel_app project.
"""

import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

# Create the Celery application
app = Celery('alx_travel_app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

# Optional: Configure periodic tasks
app.conf.beat_schedule = {
    # Add periodic tasks here
    # 'cleanup-expired-sessions': {
    #     'task': 'listings.tasks.cleanup_expired_sessions',
    #     'schedule': 60.0 * 60.0,  # Every hour
    # },
}

app.conf.timezone = 'UTC'

@app.task(bind=True)
def debug_task(self):
    """Debug task for testing Celery setup."""
    print(f'Request: {self.request!r}')