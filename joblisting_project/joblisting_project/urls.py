from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_api(request):
    return redirect('/api/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.urls')),
    path('', redirect_to_api),  # Redirect root URL to /api/
]
