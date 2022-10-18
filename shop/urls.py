from django.urls import path
import shop.views as views

urlpatterns = [
    path('', views.stores_list_view),
    path('<int:id>/', views.stores_detail_view),
    path('<int:id>/add/', views.add_product_view),
]