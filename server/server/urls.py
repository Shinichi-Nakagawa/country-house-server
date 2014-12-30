from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^house/', include('house.urls')),
)
