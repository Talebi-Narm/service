from django.urls import path

from store.apis import admin as admin_views
from store.apis import product as product_views
from store.apis import comment as comment_views

urlpatterns = [

    # ----> ADMIN <----
    path('admin/plants/', admin_views.PlantList.as_view(), name="admin_plants"),
    path('admin/plants/<uuid:pk>/', admin_views.PlantDetail.as_view(), name="admin_plants_detail"),
    path('admin/tools/', admin_views.ToolList.as_view(), name="admin_tools"),
    path('admin/tools/<uuid:pk>/', admin_views.ToolDetail.as_view(), name="admin_tools_detail"),

    # ----> USERS <----
    path('plants/', product_views.PlantList.as_view(), name="plants"),
    path('plants/<uuid:pk>/', product_views.PlantDetail.as_view(), name="plants_detail"),
    path('tools/', product_views.ToolList.as_view(), name="tools"),
    path('tools/<uuid:pk>/', product_views.ToolDetail.as_view(), name="tools_detail"),
    path('admin/plant-comment-approve/<uuid:pk>/', comment_views.PlantCommentAdminApprove.as_view(), name="plant_admin_comment_approve"),
    path('admin/tool-comment-approve/<uuid:pk>/', comment_views.ToolCommentAdminApprove.as_view(), name="tool_admin_comment_approve"),
    path('plant-comment/', comment_views.PlantCommentCreate.as_view(), name="plant_comment"),
    path('tool-comment/', comment_views.ToolCommentCreate.as_view(), name="tool_comment"),
    path('plant-comments/<uuid:pk>/', comment_views.PlantComments.as_view(), name="plant_comments"),
    path('plant-comments/<uuid:pk>/', comment_views.ToolComments.as_view(), name="tool_comments"),

    # # Plant API
    #     path('plants/', views.plants.as_view(), name='plants'),
    #     path('plantsRUD/<str:pk>/', views.plantsRUD.as_view(), name='plantsRUD'),

    # # Tool API
    #     path('tools/', views.tools.as_view(), name='tools'),
    #     path('toolsRUD/<str:pk>/', views.toolsRUD.as_view(), name='toolsRUD'),

    # # Tag API
    #     path('tags/', views.tags.as_view(), name='tags'),
    #     path('tagsRUD/<str:pk>/', views.tagsRUD.as_view(), name='tagsRUD'),

    # # Get Tag Groups
    #     path('plantsTags/', views.plantsTags.as_view(), name='plantsTags'),
    #     path('toolsTags/', views.toolsTags.as_view(), name='toolssTags'),

    # # Category API
    #     path('plantsWithTag/<str:pk>/', views.plantsWithSpecificTag.as_view(), name='plantsWithTag'),
    #     path('toolsWithTag/<str:pk>/', views.toolsWithSpecificTag.as_view(), name='toolsWithTag'),

    # # searching and filtering for plants
    #     path('plantsByName/', sfsp_views.plantsByName.as_view(), name='plantsByName'),
    #     path('plantsByPrice/', sfsp_views.plantsByPrice.as_view(), name='plantsByPrice'),
    #     path('plantsByEnvironment/', sfsp_views.plantsByEnvironment.as_view(), name='plantsByEnvironment'),
    #     path('plantsByWater/', sfsp_views.plantsByWater.as_view(), name='plantsByWater'),
    #     path('plantsByLight/', sfsp_views.plantsByLight.as_view(), name='plantsByLight'),
    #     path('plantsByGrowthRate/', sfsp_views.plantsByGrowthRate.as_view(), name='plantsByGrowthRate'),
    #     path('plantsByTags/', sfsp_views.plantsByTags.as_view(), name='plantsByTags'),

    # # searching and filtering for tools
    #     path('toolsByName/', sfsp_views.toolsByName.as_view(), name='toolsByName'),
    #     path('toolsByPrice/', sfsp_views.toolsByPrice.as_view(), name='toolsByPrice'),
    #     path('toolsByTags/', sfsp_views.toolsByTags.as_view(), name='toolsByTags'),

    # # plants and tools sorting
    #     path('plantsSort/', sfsp_views.plantsSort.as_view(), name='plantsSort'),
    #     path('toolsSort/', sfsp_views.toolsSort.as_view(), name='toolsSort'),

    # plants and tool pagination
    # path('plantsPagination/', sfsp_views.plantsPagination.as_view(), name='plantsPagination'),
    # path('toolsPagination/', sfsp_views.toolsPagination.as_view(), name='toolsPagination'),
    # path('allPagination/', sfsp_views.allPagination.as_view(), name='allPagination'),

    # # advance search
    #     path('plantsAdvanceSearch/', sfsp_views.plantsAdvanceSearch.as_view(), name='plantsAdvanceSearch'),
    #     path('toolsAdvanceSearch/', sfsp_views.toolsAdvanceSearch.as_view(), name='toolsAdvanceSearch'),
    #     path('allAdvanceSearch/', sfsp_views.allAdvanceSearch.as_view(), name='allAdvanceSearch'),

    # # category API
    #     path('plantsWithTag/<str:tag_name>/', views.plantsWithSpecificTag.as_view(), name='plantsWithTag'),
    #     path('toolsWithTag/<str:tag_name>/', views.toolsWithSpecificTag.as_view(), name='toolsWithTag'),

    # # get plant and tool, tags
    #     path('plantTags/<str:pk>/', views.plantTags.as_view(), name='plantsTag'),
    #     path('toolTags/<str:pk>/', views.toolTags.as_view(), name='toolsTag'),
]
