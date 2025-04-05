from django.urls import path
from backend.views import home_view, chatbot_response

urlpatterns = [
    path('', home_view),
    path('chatbot/', chatbot_response),  # AI Chatbot API
]
