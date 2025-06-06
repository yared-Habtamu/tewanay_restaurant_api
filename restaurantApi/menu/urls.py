from django.urls import path
from .views import MenuItemListView, MenuItemCreateView, MenuItemDetailView

urlpatterns = [
    path('', MenuItemListView.as_view(), name='menu-list'),  # GET (Public)
    path('create/', MenuItemCreateView.as_view(), name='menu-create'),  # POST (Manager/Admin)
    path('<int:pk>/', MenuItemDetailView.as_view(), name='menu-detail'),  # GET/PUT/DELETE (Manager/Admin)
]