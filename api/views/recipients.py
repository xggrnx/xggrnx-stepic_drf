from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipients.models import Recipient


@api_view(http_method_names=['GET'])
def recipient_list(request):
    return Response(Recipient.all())


@api_view(http_method_names=['GET'])
def recipient_detail(request, pk):
    recipient: dict = Recipient.get_by_key('id', pk)
    if recipient:
        return Response(recipient)
    return Response(status=status.HTTP_404_NOT_FOUND)
