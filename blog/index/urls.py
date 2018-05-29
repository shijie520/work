from django.conf.urls import url,include
from . import views as app

urlpatterns = [
    url(r'^$',app.date, name ='index'),
    url(r'^date/(?P<date_page_id>[0-9]+)/$',app.date_page, name='date_page'),
    

]
