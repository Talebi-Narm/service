from django.urls import path

from common.apis import bookmark as bookmark_views

urlpatterns = [
    path('plant-bookmarks/', bookmark_views.PlantBookmarkList.as_view()),
    path('plant-bookmarks/<uuid:pk>/', bookmark_views.PlantBookmarkDestroy.as_view()),
    path('tool-bookmarks/', bookmark_views.ToolBookmarkList.as_view()),
    path('tool-bookmarks/<uuid:pk>/', bookmark_views.ToolBookmarkDestroy.as_view()),
]
