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
    path('albumImages/<str:pk>/', views.getAlbumImages, name='albumImages'),
    path('addImageToAlbum/<str:pk>/', views.createImage, name='addImageToAlbum'),

# searching and filtering for plants
    path('plantsByName/<str:_name>/', sfsp_view.plantsByName, name='plantsByName'),
    path('plantsByPrice/<str:prices>/', sfsp_view.plantsByPrice, name='plantsByPrice'),
    path('plantsByEnvironment/<str:_environment>/', sfsp_view.plantsByEnvironment, name='plantsByEnvironment'),
    path('plantsByWater/<str:_water>/', sfsp_view.plantsByWater, name='plantsByWater'),
    path('plantsByLight/<str:_light>/', sfsp_view.plantsByLight, name='plantsByLight'),
    path('plantsByGrowthRate/<str:_growthRate>/', sfsp_view.plantsByGrowthRate, name='plantsByGrowthRate'),
    path('plantsByTags/<str:tags>/', sfsp_view.plantsByTags, name='plantsByTags'),

# searching and filtering for tools
    path('toolsByName/<str:_name>/', sfsp_view.toolsByName, name='toolsByName'),
    path('toolsByPrice/<str:prices>/', sfsp_view.toolsByPrice, name='toolsByPrice'),
    path('toolsByTags/<str:tags>/', sfsp_view.toolsByTags, name='toolsByTags'),

# plants sorting
    path('plantsSortByName/<str:kind>/', sfsp_view.plantsSortByName, name='plantsSortByName'),
    path('plantsSortByPrice/<str:kind>/', sfsp_view.plantsSortByPrice, name='plantsSortByPrice'),
    path('plantsSortByNewest/', sfsp_view.plantsSortByCreateDate, name='plantsSortByCreateDate'),

# tools sorting
    path('toolsSortByName/<str:kind>/', sfsp_view.toolsSortByName, name='toolsSortByName'),
    path('toolsSortByPrice/<str:kind>/', sfsp_view.toolsSortByPrice, name='toolsSortByPrice'),
    path('toolsSortByNewest/', sfsp_view.toolsSortByCreateDate, name='toolsSortByCreateDate'),

# advance search
    path('plantsAdvanceSearch/<str:filters>/', sfsp_view.plantsAdvanceSearch, name='plantsAdvanceSearch'),
    path('toolsAdvanceSearch/<str:filters>/', sfsp_view.toolsAdvanceSearch, name='toolsAdvanceSearch'),
]
