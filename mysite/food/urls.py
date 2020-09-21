from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),

    path('<int:item_id>', views.detail, name='detail'),
    #add items
    path('add', views.create_item, name='create_item'),
]