from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='item_list'),
    path('account_info/<slug>/', account_info.as_view(), name='profile'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add_item', add_item, name='add'),
    path('delete_item/<id>', delete_item, name='delete' )
]