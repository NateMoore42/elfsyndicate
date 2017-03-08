from django.conf.urls import url
from . import views
from character.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Standard URLS
    url(r'^create/', views.character_create, name='create_character'),
    url(r'^character/(?P<pk>\w+)/(?P<c_name>\w+)/$', views.character_detail, name='character_detail'),
    url(r'^character/edit/(?P<pk>\w+)/(?P<c_name>\w+)/$', views.character_edit, name='character_edit'),

    # API URLS
    url(r'^api/character/(?P<pk>\w+)/$', views.CharacterApi.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
