# from FilMixs.main import views
from django.contrib import admin
# from django.contrib.admin.sites import site
from django.urls.conf import include
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    # path('', views.FilmsListView.as_view(), name = "list")
]