from django.urls import path
from . import views
from . import SFSP_views as sfsp_view

urlpatterns=[
    # path('', views.ProductsAPIOverview.as_view(), name='api'),

# Plant API
#     path('plants/', views.plants.as_view(), name='plants'),
#     path('plantsRUD/<str:pk>/', views.plantsRUD.as_view(), name='plantsRUD'),
#
# # Tool API
#     path('tools/', views.tools.as_view(), name='tools'),
#     path('toolsRUD/<str:pk>/', views.toolsRUD.as_view(), name='toolsRUD'),
#
# # Tag API
#     path('tags/', views.tags.as_view(), name='tags'),
#     path('tagsRUD/<str:pk>/', views.tagsRUD.as_view(), name='tagsRUD'),
#
# # Album API
#     path('albums/', views.albums.as_view(), name='albums'),
#     path('albumsRUD/<str:pk>/', views.albumsRUD.as_view(), name='albumsRUD'),
#
# # Get Tag Groups
#     path('plantsTags/', views.plantsTags.as_view(), name='plantsTags'),
#     path('toolsTags/', views.toolsTags.as_view(), name='toolssTags'),
#
# # Category API
#     path('plantsWithTag/<str:pk>/', views.plantsWithSpecificTag.as_view(), name='plantsWithTag'),
#     path('toolsWithTag/<str:pk>/', views.toolsWithSpecificTag.as_view(), name='toolsWithTag'),
#
# # Album Images API
#     path('imageList/', views.images.as_view(), name='imageList'),
#     path('plantAlbumImages/<str:pk>/', views.getPlantsAlbumImages.as_view(), name='plantAlbumImages'),
#     path('toolAlbumImages/<str:pk>/', views.getToolsAlbumImages.as_view(), name='toolAlbumImages'),
#     path('addImageToAlbum/<str:pk>/', views.addImageToAlbum.as_view(), name='addImageToAlbum'),
#
# # searching and filtering for plants
#     path('plantsByName/', sfsp_view.plantsByName.as_view(), name='plantsByName'),
#     path('plantsByPrice/', sfsp_view.plantsByPrice.as_view(), name='plantsByPrice'),
#     path('plantsByEnvironment/', sfsp_view.plantsByEnvironment.as_view(), name='plantsByEnvironment'),
#     path('plantsByWater/', sfsp_view.plantsByWater.as_view(), name='plantsByWater'),
#     path('plantsByLight/', sfsp_view.plantsByLight.as_view(), name='plantsByLight'),
#     path('plantsByGrowthRate/', sfsp_view.plantsByGrowthRate.as_view(), name='plantsByGrowthRate'),
#     path('plantsByTags/', sfsp_view.plantsByTags.as_view(), name='plantsByTags'),
#
# # searching and filtering for tools
#     path('toolsByName/', sfsp_view.toolsByName.as_view(), name='toolsByName'),
#     path('toolsByPrice/', sfsp_view.toolsByPrice.as_view(), name='toolsByPrice'),
#     path('toolsByTags/', sfsp_view.toolsByTags.as_view(), name='toolsByTags'),
#
# # plants and tools sorting
#     path('plantsSort/', sfsp_view.plantsSort.as_view(), name='plantsSort'),
#     path('toolsSort/', sfsp_view.toolsSort.as_view(), name='toolsSort'),
#
# # plants and tool pagination
#     path('plantsPagination/', sfsp_view.plantsPagination.as_view(), name='plantsPagination'),
#     path('toolsPagination/', sfsp_view.toolsPagination.as_view(), name='toolsPagination'),
#     path('allPagination/', sfsp_view.allPagination.as_view(), name='allPagination'),
#
# # advance search
#     path('plantsAdvanceSearch/', sfsp_view.plantsAdvanceSearch.as_view(), name='plantsAdvanceSearch'),
#     path('toolsAdvanceSearch/', sfsp_view.toolsAdvanceSearch.as_view(), name='toolsAdvanceSearch'),
#     path('allAdvanceSearch/', sfsp_view.allAdvanceSearch.as_view(), name='allAdvanceSearch'),
#
# # category API
#     path('plantsWithTag/<str:tag_name>/', views.plantsWithSpecificTag.as_view(), name='plantsWithTag'),
#     path('toolsWithTag/<str:tag_name>/', views.toolsWithSpecificTag.as_view(), name='toolsWithTag'),
#
# # get plant and tool, tags
#     path('plantTags/<str:pk>/', views.plantTags.as_view(), name='plantsTag'),
#     path('toolTags/<str:pk>/', views.toolTags.as_view(), name='toolsTag'),

]
