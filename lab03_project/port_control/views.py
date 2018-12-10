from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def set_pin(request, pk=None):
    if request.method == 'GET':
        return Response({"pin": pk})