from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.InfosView.as_view()),
    url(r'^read_csv/$',views.Read_csvView.as_view()),


]