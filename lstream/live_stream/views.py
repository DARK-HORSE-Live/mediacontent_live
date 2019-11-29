from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def start_page(request):
    return HttpResponse('Content')


class ViewAPIStream(APIView):
    def get(self, request):
        return Response({'Content': 'Stream'})
