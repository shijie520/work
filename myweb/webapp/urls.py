from django.conf.urls import url
from . import views as ap
urlpatterns = [

    #url(r'^admin/', admin.site.urls),
    url(r'^$',ap.hello),


]
