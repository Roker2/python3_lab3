from .models import Artist
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ArtistList(ListView):
    model = Artist
    template_name = 'artist_crud/artist_list.html'


class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_crud/artist_details.html'


class ArtistCreate(CreateView):
    model = Artist
    template_name = 'artist_crud/artist_form.html'
    fields = ['Name']
    success_url = reverse_lazy('artist_list')


class ArtistUpdate(UpdateView):
    model = Artist
    template_name = 'artist_crud/artist_form.html'
    fields = ['Name']
    success_url = reverse_lazy('artist_list')


class ArtistDelete(DeleteView):
    model = Artist
    template_name = 'artist_crud/artist_confirm_delete.html'
    success_url = reverse_lazy('artist_list')
