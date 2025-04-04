from django.urls import path
from django.http import JsonResponse

def test_api(request):
    return JsonResponse({"message": "Hello, AI-based Learning!"})

urlpatterns = [
    path('api/test/', test_api),
]
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome to the AI-Based Assessment Backend!")
from django.urls import path

urlpatterns = [
    path("", home),  # This will handle requests to the root URL
    path("api/test/", home),  # Your existing API route
]
