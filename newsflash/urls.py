"""ttd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from flashes.views import news, detail, pridat, promo
from django.conf import settings
from django.conf.urls.static import static
from .views import info, kontakt


urlpatterns = [
    url("^$", view=news, name="index"),
    url("^zprava/pridat/$", name="pridat", view=pridat),
    url("^zprava/(?P<id>[0-9-]+)/$", name="detail", view=detail),
    url("^promo/(?P<id>[0-9-]+)/$", name="promo", view=promo),
    url("^info/$", name="info", view=info),
    url("^kontakt/$", name="kontakt", view=kontakt),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
