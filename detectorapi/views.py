from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer
import joblib
from .forms import NewsLetterForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse

logistic_regression_model = joblib.load('lr_model.pkl')
countvectorizer = joblib.load('Countvectorizer.pkl')


# Create our predict api which deploys our ML models
@api_view(['POST'])
def predict(request):
    data = request.data
    text = data.get('text', '')
    transformed_text = countvectorizer.transform([text])
    prediction = logistic_regression_model.predict(transformed_text)
    result = "Real News" if prediction[0] == 1 else "Fake News"
    return Response({'prediction': result})


def index(request):
    return render(request, 'index.html')


def detector(request):
    return render(request, 'detector.html')


def contact(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            contact = form.save()
            send_contact_email(contact)
            messages.success(request, 'Your message has been sent successfully!')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = NewsLetterForm()
    return render(request, 'contact.html', {'form': form})

def send_contact_email(contact):
    subject = 'Thank you for contacting us!'
    message = f'Hi {contact.username},\n\nThank you for reaching out to us. We have received your message and will get back to you shortly.\n\nBest Regards,\nData Alchemists'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [contact.email]
    send_mail(
        subject,
        message,
        email_from,
        recipient_list,
        fail_silently=False,
        html_message=f'''
        <html>
            <head>
                <title>Data Alchemists</title> 
            </head>
            <body>
                <p>Hi {contact.username},</p>
                <p>Thank you for reaching out to us. We have received your message and will get back to you shortly.</p>
                <img src="{settings.BASE_URL}/static/images/da_logo.jpeg" alt="Logo" style="height: 50px;"> <!-- Add BASE_URL to ensure the image loads properly -->
                <p>Best Regards,<br>Data Alchemists</p>
            </body>
        </html>
        ''',
    )