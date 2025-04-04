import openai
from django.http import JsonResponse

# Replace with your OpenAI API Key
openai.api_key = "your_openai_api_key"

def chatbot_response(request):
    user_input = request.GET.get("message", "")

    # Send user input to OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )

    bot_message = response["choices"][0]["message"]["content"]
    
    return JsonResponse({"response": bot_message})
