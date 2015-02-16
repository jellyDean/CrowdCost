from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from gettingstarted import settings
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^index/', hello.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_results', hello.views.search_results, name='search_results'),
    url(r'^calculate_average/$', hello.views.search_results, name='calculate_average'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
