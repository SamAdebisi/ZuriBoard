from django.urls import path
from musicapp import views
from .views import artiste_list, artiste_details
from .apiviews import ArtisteList, ArtisteDetail, ArtisteCreateView, ArtisteUpdateView, ArtisteDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('artistes/', views.artiste_list, name='artiste_list'),
    path('artistes/<int:pk>', views.artiste_details, name='artiste_details'),
    path('artiste/', ArtisteList.as_view(), name='artiste_list'),
    path('artiste/<int:pk>/', ArtisteDetail.as_view(), name='artiste_details'),
    path('artiste/new/', ArtisteCreateView.as_view(), name='artiste_new'),
    path('artiste/<int:pk>/edit/', ArtisteUpdateView.as_view(), name='artiste_edit'),
    path('artiste/<int:pk>/delete', ArtisteDeleteView.as_view(), name='artiste_delete')
]
