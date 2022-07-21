from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token 
from products import views
urlpatterns = [
path('',views.ProductListCreateAPIView.as_view()),
path('<int:pk>/', views.ProductDetialAPIView.as_view()),
path('<int:pk>/update/',views.ProductUpdateList.as_view()),
path('<int:pk>/delete/',views.ProductListDeleteAPIView.as_view()),

## Mixins urls
path('list-product/', views.CreateListProduct.as_view()),
path('<int:pk>/update_delete/',views.DetailUpdateProduct.as_view())

]
