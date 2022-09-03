from django.urls import path

from app.views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('landing_alternate/', landing, name='landing_alternate'),

    path('stats/', stats, name='stats'),
]
