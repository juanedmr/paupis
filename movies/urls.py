import os
from django.urls import include, path, re_path
from django.views.static import serve
from . import views

app_name = 'movies'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'demo')

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path('polls/', include('polls.urls')),
  path('route/', include('route.urls')),
  re_path(r'^demo/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    )
]
