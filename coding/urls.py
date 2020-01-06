from django.conf.urls import url

from coding import views

app_name = 'coding'

urlpatterns = [
    url(r'^$', views.CodingView.as_view(), name='index'),
]