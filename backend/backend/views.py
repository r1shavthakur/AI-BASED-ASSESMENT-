from django.http import JsonResponse

def home_view(request):
    return JsonResponse({"message": "Welcome to AI-Based Assessment API!"})

def chatbot_response(request):
    user_message = request.GET.get("message", "")
    return JsonResponse({"response": f"AI Response to '{user_message}'"})
