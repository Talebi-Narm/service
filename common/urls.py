from django.urls import path

from common.apis import admin as admin_views
from common.apis import tag as tag_views

urlpatterns=[

# ----> ADMIN <----
    path('admin/tags/', admin_views.TagList.as_view()),
    path('admin/tags/<uuid:pk>/', admin_views.TagDetail.as_view()),

# ----> USER <----
    path('tags/', tag_views.TagList.as_view()),
    path('tags/<uuid:pk>/', tag_views.TagDetail.as_view()),
]