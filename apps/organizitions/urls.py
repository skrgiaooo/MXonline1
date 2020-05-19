from django.conf.urls import url
from apps.organizitions.views import OrgView,AddAsk

urlpatterns = [
    url(r'^',OrgView.as_view()),
    url(r'^list/$',OrgView.as_view(),name='list'),
    url(r'^add_ask/$',AddAsk.as_view(),name='add_ask'),
]