from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Film
# Create your views here.
# class FilmsListView(ListView):
#     model = Film

# class FilmDetailView(DetailView):
#     model = Film


def homepage(request):
    return render (
                    request=request,
                    template_name="home.html",
                    context={"Films": Film.objects.all}
    )