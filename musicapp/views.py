from turtle import title
from django.shortcuts import render
from requests import request

from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.http import Http404

from django.shortcuts import get_object_or_404


from .models import Artiste, Lyric, Song

from .serializers import LyricSerializer, SongSerializer, UpdateSongSerializer, ArtisteSerializer
from musicapp import serializers

# Create your views here.

class SongListCreateApiView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        serializer.save()

# class SongListApiView(generics.ListAPIView):
#     serializer_class = SongSerializer
    
#     def get_queryset(self):
#         song_detail = Song.objects.all()
#         return song_detail

#     def perform_retrieve(self, request, *args, **kwargs):
#         params = kwargs
#         print(params['pk'])
#         song = Song.objects.filter(id=params['pk'])
#         serializer = SongSerializer(song, many=True)
#         return Response(serializer.data)


class SongRetrieveApiView(generics.RetrieveAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

class SongUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = Song.objects.all()
    serializer_class = UpdateSongSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


class SongDestroyApiView(generics.DestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class ArtisteListCreateApiView(generics.ListCreateAPIView):
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('first_name')
        serializer.save()




# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.ListModelMixin,
#     mixins.UpdateModelMixin,
#     generics.GenericAPIView
#     ):
#     queryset = Song.objects.all()
#     serializer_class = SongSerializer
#     lookup_field = 'pk'

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None: 
#             return self.update(request, *args, **kwargs)
#         #if there's no primary key (pk) then its a create function
#         return self.create(request, *args, **kwargs)

class LyricRetrieveApiView(generics.RetrieveAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer


    def perform_retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        lyric = Lyric.objects.filter(song_id=params['pk'])
        serializer = LyricSerializer(lyric, many=True)
        return Response(serializer.data)

class LyricCreateApiView(generics.CreateAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('content')
        serializer.save()

class LyricDestroyApiView(generics.DestroyAPIView):
    queryset = Lyric.objects.all()
    serializer_class = LyricSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# class SongListApiView(generics.ListAPIView):
#     serializer_class = SongSerializer
    
#     def get_queryset(self):
#         song_detail = Song.objects.all()
#         return song_detail

#     def perform_retrieve(self, request, *args, **kwargs):
#         params = kwargs
#         print(params['pk'])
#         song = Song.objects.filter(id=params['pk'])
#         serializer = SongSerializer(song, many=True)
#         return Response(serializer.data)
