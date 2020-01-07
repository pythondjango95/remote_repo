
from django.contrib import admin
from django.conf.urls import url
from durgasoftapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home/',views.home),
    url(r'^aboutus/',views.aboutus),
    url(r'^contact/',views.contact),
    url(r'^services/',views.services),
    url(r'^gallery/',views.gallery),

]
