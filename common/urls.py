from django.urls import path

from common.apis import admin as admin_views
from common.apis import bookmark as bookmark_views
from common.apis import tag as tag_views

urlpatterns = [

    path('admin/tags/', admin_views.TagList.as_view()),
    path('admin/tags/<uuid:pk>/', admin_views.TagDetail.as_view()),

    path('tags/', tag_views.TagList.as_view()),
    path('tags/<uuid:pk>/', tag_views.TagDetail.as_view()),

    path('plant-bookmarks/', bookmark_views.PlantBookmarkList.as_view()),
    path('plant-bookmarks/<uuid:pk>/', bookmark_views.PlantBookmarkDestroy.as_view()),
    path('tool-bookmarks/', bookmark_views.ToolBookmarkList.as_view()),
    path('tool-bookmarks/<uuid:pk>/', bookmark_views.ToolBookmarkDestroy.as_view()),
]
