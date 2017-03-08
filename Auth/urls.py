from django.conf.urls import url
from . import views
from Auth.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Standard URLS
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/(?P<username>\w+)/$', views.get_user_profile, name='profile'),
    url(r'^profile/edit/(?P<username>\w+)/$', views.user_profile_edit, name='profile_edit'),

    # API URLS
    url(r'^api/profile/(?P<pk>\w+)/$', views.UserAPI.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
