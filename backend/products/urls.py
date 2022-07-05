from django.urls import path

from products import views
urlpatterns = [
path('<int:pk>/', views.ProductDetialAPIView.as_view())
]
