from rest_framework.views import APIView
# from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404


from .models import Artiste, Song, Lyric
from .forms import ArtisteForm, SongForm, LyricForm
from .serializers import ArtisteSerializer


class ArtisteList(APIView):
    def get(self, request):
        template = 'musicapp/artiste_list.html'
        artistes = Artiste.objects.all()
        # data = {"Playlist": list(artistes.values("stage_name", "first_name", "last_name", "age"))}
        data = ArtisteSerializer(artistes, many=True).data
        content = {"Playlist": data}
        return render(request, template, content)
        # return Response(data)


class ArtisteDetail(APIView):
    def get(self, request, pk):
        template = 'musicapp/artiste_details.html'
        artiste = get_object_or_404(Artiste, pk=pk)
        data = ArtisteSerializer(artiste).data
        content = {"Playlist": data}
        # return Response(data)
        return render(request, template, content)


class ArtisteCreateView(APIView):
    def post(self, request):
        template = 'musicapp/artiste_new.html'
        artiste_form = ArtisteForm(request.POST or None)
        song_form = SongForm(request.POST or None)
        lyric_form = LyricForm(request.POST or None)
        if artiste_form.is_valid():
            artiste_form.save()
            if song_form.is_valid():
                song_form.save()
                if lyric_form.is_valid():
                    lyric_form.save()

                    return redirect('musicapp/artiste_list.html')
        context = {"form": {"artiste": artiste_form, "song": song_form, "lyric": lyric_form}}
        return render(request, template, context)


class ArtisteUpdateView(APIView):
    def post(self, request, pk):
        template = 'musicapp/artiste_edit.html'
        artiste = get_object_or_404(Artiste, pk=pk)
        song = get_object_or_404(Song, pk=pk)
        lyric = get_object_or_404(Lyric, pk=pk)
        artiste_form = ArtisteForm(request.POST or None, instance=artiste)
        song_form = SongForm(request.POST or None, instance=song)
        lyric_form = LyricForm(request.POST or None, instance=Lyric)
        if artiste_form.is_valid():
            artiste_form.save()
            if song_form.is_valid():
                song_form.save()
                if lyric_form.is_valid():
                    lyric_form.save()

                    return redirect('musicapp/artiste_list.html')
        context = {"form": {"artiste": artiste_form, "song": song_form, "lyric": lyric_form}}
        return render(request, template, context)


class ArtisteDeleteView(APIView):
    def post(self, request, pk):
        template = 'musicapp/artiste_delete.html'
        artiste = get_object_or_404(Artiste, pk=pk)
        if request.method == 'POST':
            artiste.delete()
            return redirect('musicapp/artiste_list.html')
        context = {"book": artiste}
        return render(request, template, context)
