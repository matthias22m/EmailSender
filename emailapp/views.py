from django.core.mail import EmailMessage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmailSerializer

class EmailAPIView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.save()
            try:
                msg = EmailMessage(
                    subject=email.subject,
                    body='Full Name: '+email.full_name+'\n'+'From: '+email.from_email+'\n'+'Phone Number: '+email.phone_number+'\n'+email.body,
                    to=[email.to_email]
                )
                msg.send()
                return Response({'status': 'Email sent'}, status=status.HTTP_200_OK)
            except:
                return Response({'status': 'Email sending failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


