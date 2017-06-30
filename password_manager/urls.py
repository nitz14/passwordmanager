from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from rest_framework.routers import DefaultRouter

from .viewsets import ServisesViewSet
from .views import MainView

router = DefaultRouter()
router.register(r'servises', ServisesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', MainView.as_view(), name='main'),
    url(r'^login/$', views.login, {'template_name': 'login.html'}),
    url(r'^logout/$', views.logout, {'next_page': '/'}, name='logout'),
]

if settings.DEBUG:
    from rest_framework_swagger.views import get_swagger_view
    urlpatterns += [
        url(r'swagger/$', get_swagger_view()),
    ]
    urlpatterns += staticfiles_urlpatterns()
