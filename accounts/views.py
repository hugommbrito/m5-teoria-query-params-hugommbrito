# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AccountSerializer

from .models import Account


class AccountFindView(APIView):
    def get(self, request):
        ...
