from django.urls import path, include

urlpatterns = [
    path("chatbox/", include("chatbox.urls")),
]
