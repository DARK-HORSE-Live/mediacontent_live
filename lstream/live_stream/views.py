from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


def start_page(request):
    return HttpResponse('Content')


class ViewAPIStream(APIView):
    def get(self, request):
        return Response({'url1': 'http://46.61.193.124/play/hls/flag/index.m3u8',
                         'url2': 'http://46.61.193.124/play/hls/bbb/index.m3u8'})





