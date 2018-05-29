from django.conf.urls import url,include
from . import views as app

urlpatterns = [
    url(r'^home$',app.date, name ='date'),
    url(r'^date/(?P<date_page_id>[0-9]+)/$',app.date_page, name='date_page'),
    url(r'^edit/(?P<edit_page_id>[0-9]+)/$',app.edit_page, name ='edit_page'),
    url(r'^post/$',app.page_post, name ='page_post'),
    url(r'^home$',app.return_home, name ='retuen_home'),

]
