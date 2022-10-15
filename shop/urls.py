from django.urls import path
from .views import (
    stores_list_view,
    stores_detail_view,
)

urlpatterns = [
    path('', stores_list_view),
    path('detail/', stores_detail_view),
]