from django.conf.urls import url, include

accounts_urlpatterns = [
    url(r'^api/v1/', include('rest_framework.urls')),
    url(r'^api/v1/', include('djoser.urls')),
    url(r'^api/v1/', include('djoser.urls.authtoken')),
]