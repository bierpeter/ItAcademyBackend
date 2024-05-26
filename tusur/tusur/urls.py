from django.urls import path
from tusurBackSite import views
from django.urls import path


urlpatterns = [
    path('login/', views.login, name='login'),
    path('users/', views.Users.user_list, name='user_list'),
    path('users/edit/<int:user_id>/', views.Users.edit_User, name='user_edit'),
    path('profile/', views.Users.user_profile_view, name='user_profile'),
    path('buildings/', views.Properties.edit_Property, name='building_select'),
    path('buildings/<int:building_id>/rooms/', views.Properties.select_view, name='room_select'),
    path('buildings/<int:building_id>/rooms/<int:room_id>/', views.Properties.detail_view, name='room_detail'),
    path('properties/<int:asset_id>/', views.Properties.detail_view, name='property_detail'),
    path('properties/edit/<int:asset_id>/', views.Properties.edit_Property, name='property_edit'),
    path('catalog/', views.Properties.property_catalog_view, name='property_catalog'),
]



