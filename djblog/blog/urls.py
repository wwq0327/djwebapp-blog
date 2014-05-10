from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r"^$", "blog.views.index", name="blog:index"),
                       url(r"^post/(?P<pk>\d+)/$", "blog.views.post", name="blog:post"),
)                       
