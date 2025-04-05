from django.http import JsonResponse

def chatbot_response(request):
    return JsonResponse({"message": "Hello, I'm your AI chatbot!"})
