from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactSerializer

@api_view(['POST'])
def contact_form(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        # Send email to admin
        try:
            send_mail(
                subject=f"New message from {data['firstName']} {data.get('lastName','')}",
                message=f"Email: {data['email']}\n\nMessage:\n{data['message']}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return Response({"message": "Message sent successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
