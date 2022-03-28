from django.urls import re_path as url
from services import views

urlpatterns = [
    url(r'^api/services$', views.service_list),
    url(r'^api/services/(?P<pk>[0-9]+)$', views.service_detail),
]
