import os
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application
from django.core.management import execute_from_command_line

# Define the view that will display the text
def home(request):
    return HttpResponse("""
        <h1>Sample Python Application</h1>
        <p>This application is running on Docker Image in AWS Elastic Container Service</p>
    """)

# Configure Django settings in a minimal way
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY='a_random_secret_key',  # You can generate a random one or leave this
    ALLOWED_HOSTS=['*'],
    MIDDLEWARE=[],
)

# Define the URL route for the homepage
urlpatterns = [
    path('', home),
]

# Set up the WSGI application for serving the app
application = get_wsgi_application()

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', __name__)
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:8000'])
