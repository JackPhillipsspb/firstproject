from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post_new/', views.post_new, name='post_new'),
	path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]