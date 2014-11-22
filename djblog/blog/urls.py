from django.conf.urls import patterns, include, url
# import .views

urlpatterns = patterns('',
                       url(r"^$", "blog.views.index", name="index"),
                       url(r"^post/(?P<pk>\d+)/$", "blog.views.post", name="post"),
                       url(r"^category/(?P<pk>\d+)/$", "blog.views.category", name="category"),
)                       
