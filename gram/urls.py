from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.index,name='index'),
    re_path(r'^timeline/$', views.timeline, name='timeline'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^image/(\d+)',views.image,name ='image'),
    re_path(r'^new/image$', views.new_image, name='new-image'),
    re_path(r'^search/profile', views.search_profile, name='search_profile'),
    re_path(r'^update/profile$', views.update_profile, name='update-profile'),
    re_path(r'^write/comment$', views.write_comment, name='write-comment'),
    re_path(r'^comment/$', views.comment, name='comment'),
    re_path(r'^like/(\d+)',views.like,name ='like'),
    re_path(r'^accounts/profile', views.profile, name='profile')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)