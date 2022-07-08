from django.urls import path

from products import views
urlpatterns = [
path('',views.ProductListCreateAPIView.as_view()),
path('<int:pk>/', views.ProductDetialAPIView.as_view()),
path('<int:pk>/update/',views.ProductUpdateList.as_view()),
path('<int:pk>/delete/',views.ProductListDeleteAPIView.as_view())
]
