from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.SongListCreateApiView.as_view()),
    # path('find_song/<str:pk>/', views.SongListApiView.as_view()),
    path('<int:pk>/find_song/', views.SongRetrieveApiView.as_view()),
    path('<int:pk>/update_song/', views.SongUpdateApiView.as_view()),
    path('artiste_list/', views.ArtisteListCreateApiView.as_view()),
    path('<int:pk>/song_delete/', views.SongDestroyApiView.as_view()),
    # path('<int:pk>/update_song/', views.ProductMixinView.as_view()),
    path('<int:pk>/find_lyric/', views.LyricRetrieveApiView.as_view()),
    path('create_lyric/', views.LyricCreateApiView.as_view()),
]
