from django.conf.urls import url
from . import views
#from blog.views import simple_chart

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.simple_chart, name='post_list'),
    url(r'^simple_chart/$', views.simple_chart, name='simple_chart'),
]
