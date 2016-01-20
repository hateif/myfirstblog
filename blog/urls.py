from django.conf.urls import url
from . import views
#from blog.views import simple_chart

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.simple_chart, name='post_list'),
    url(r'^simple_chart/$', views.simple_chart, name='simple_chart'),
    url(r'^home/$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^compute/$', views.numcompute, name='compute'),
]
