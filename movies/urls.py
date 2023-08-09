import os
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from django.views.generic.base import TemplateView
from . import views

app_name = 'movies'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'demo')

urlpatterns = [
  path('admin/', admin.site.urls),
  path('accounts/', include('django.contrib.auth.urls')),
  path('authz/', include('authz.urls')),
  path('', TemplateView.as_view(template_name='home/main.html')),
  path('movies/', views.HomeView.as_view(), name='home'),
  path('polls/', include('polls.urls')),
  path('autos/', include('autos.urls')),
  path('hello/', include('hello.urls')),
  path('route/', include('route.urls')),
  path('gview/', include('gview.urls')),
  re_path(r'^demo/(?P<path>.*)$', serve,
        {'document_root': SITE_ROOT, 'show_indexes': True},
        name='site_path'
    )
]
