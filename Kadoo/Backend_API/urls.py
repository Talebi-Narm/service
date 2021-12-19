from django.urls import path
from . import views
from . import SFSP_views as sfsp_view

urlpatterns=[
    path('', views.ProductsAPIOverview, name='api'),

# Plant API
    path('plantsList/', views.plantList, name='plantsList'),
    path('plantDetail/<str:pk>/', views.plantDetail, name='plantDetail'),
    path('createPlant/', views.createPlant, name='createPlant'),
    path('updatePlant/<str:pk>/', views.updatePlant, name='updatePlant'),
    path('deletePlant/<str:pk>/', views.deletePlant, name='deletePlant'),

# Tool API
    path('toolsList/', views.toolList, name='toolsList'),
    path('toolDetail/<str:pk>/', views.toolDetail, name='toolDetail'),
    path('createTool/', views.createTool, name='createTool'),
    path('updateTool/<str:pk>/', views.updateTool, name='updateTool'),
    path('deleteTool/<str:pk>/', views.deleteTool, name='deleteTool'),

# Tag API
    path('tagsList/', views.tagList, name='tagsList'),
    path('tagDetail/<str:pk>/', views.tagDetail, name='tagDetail'),
    path('createTag/', views.createTag, name='createTag'),
    path('updateTag/<str:pk>/', views.updateTag, name='updateTag'),
    path('deleteTag/<str:pk>/', views.deleteTag, name='deleteTag'),

# Album API
    path('albumsList/', views.albumList, name='albumsList'),
    path('albumDetail/<str:pk>/', views.albumDetail, name='albumDetail'),
    path('createAlbum/', views.createAlbum, name='createAlbum'),
    path('updateAlbum/<str:pk>/', views.updateAlbum, name='updateAlbum'),
    path('deleteAlbum/<str:pk>/', views.deleteAlbum, name='deleteAlbum'),

# Get Tag Groups
    path('plantsTags/', views.plantsTags, name='plantsTags'),
    path('toolsTags/', views.toolsTags, name='toolssTags'),

# Category API
    path('plantsWithTag/<str:pk>/', views.plantsWithSpecificTag, name='plantsWithTag'),
    path('toolsWithTag/<str:pk>/', views.toolsWithSpecificTag, name='toolsWithTag'),

# Album Images API
    path('imageList/', views.imageList, name='imageList'),
    path('plantAlbumImages/<str:pk>/', views.getPlantsAlbumImages, name='plantAlbumImages'),
    path('toolAlbumImages/<str:pk>/', views.getToolsAlbumImages, name='toolAlbumImages'),
    path('addImageToAlbum/<str:pk>/', views.createImage, name='addImageToAlbum'),

# searching and filtering for plants
    path('plantsByName/', sfsp_view.plantsByName, name='plantsByName'),
    path('plantsByPrice/', sfsp_view.plantsByPrice, name='plantsByPrice'),
    path('plantsByEnvironment/', sfsp_view.plantsByEnvironment, name='plantsByEnvironment'),
    path('plantsByWater/', sfsp_view.plantsByWater, name='plantsByWater'),
    path('plantsByLight/', sfsp_view.plantsByLight, name='plantsByLight'),
    path('plantsByGrowthRate/', sfsp_view.plantsByGrowthRate, name='plantsByGrowthRate'),
    path('plantsByTags/', sfsp_view.plantsByTags, name='plantsByTags'),

# searching and filtering for tools
    path('toolsByName/', sfsp_view.toolsByName, name='toolsByName'),
    path('toolsByPrice/', sfsp_view.toolsByPrice, name='toolsByPrice'),
    path('toolsByTags/', sfsp_view.toolsByTags, name='toolsByTags'),

# plants and tools sorting
    path('plantsSort/', sfsp_view.plantsSort, name='plantsSort'),
    path('toolsSort/', sfsp_view.toolsSort, name='toolsSort'),

# plants and tool pagination
    path('plantsPagination/', sfsp_view.plantsPagination, name='plantsPagination'),
    path('toolsPagination/', sfsp_view.toolsPagination, name='toolsPagination'),
    path('allPagination/', sfsp_view.allPagination, name='allPagination'),

# advance search
    path('plantsAdvanceSearch/', sfsp_view.plantsAdvanceSearch, name='plantsAdvanceSearch'),
    path('toolsAdvanceSearch/', sfsp_view.toolsAdvanceSearch, name='toolsAdvanceSearch'),
    path('allAdvanceSearch/', sfsp_view.allAdvanceSearch, name='allAdvanceSearch'),

# category API
    path('plantsWithTag/<str:tag_name>/', views.plantsWithSpecificTag, name='plantsWithTag'),
    path('toolsWithTag/<str:tag_name>/', views.toolsWithSpecificTag, name='toolsWithTag'),

# get plant and tool, tags
    path('plantTags/<str:pk>/', views.plantTags, name='plantsTag'),
    path('toolTags/<str:pk>/', views.toolTags, name='toolsTag'),

]
