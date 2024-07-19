
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        incoming_message = request.POST.get('Body', '').lower()
        response = MessagingResponse()

        if 'hola' in incoming_message:
            response.message('¡Hola! ¿Cómo puedo ayudarte?')
        elif 'ayuda' in incoming_message:
            response.message('Puedo ayudarte con información básica. ¿Qué necesitas saber?')
        else:
            response.message('Lo siento, no entiendo tu mensaje.')

        return HttpResponse(str(response))

    return HttpResponse('Method not allowed', status=405)
