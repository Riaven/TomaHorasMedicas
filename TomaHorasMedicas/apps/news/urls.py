from apps.news.views import index, somos
from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^quienessomos$', somos, name="quienessomos"),
]
