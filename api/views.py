from django.shortcuts import render

import json
from urllib import response
from django.forms.models import model_to_dict
# from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from yaml import serialize

from musicapp.models import Artiste, Song, Lyric
from musicapp.serializers import SongSerializer

# Create your views here.
@api_view(['GET'])
def song_api(request, *args, **kwargs):
    model_data = Song.objects.all()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'date_released', 'likes'])

    return Response(data)

