from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Picture


class UploadPic(CreateView):
    model = Picture
    template_name = 'picture_crud/picture_create.html'
    fields = ['name', 'file']
    success_url = reverse_lazy('piclist')

    def set_success_url(self, url):
        self.success_url = reverse_lazy(url)


class PicturesList(ListView):
    model = Picture
    template_name = "picture_crud/picture_list.html"


class PicturesDelete(DeleteView):
    model = Picture
    template_name = 'picture_crud/picture_confirm_delete.html'
    success_url = reverse_lazy('piclist')
