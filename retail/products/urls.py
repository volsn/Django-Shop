from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='index'),
    path(r'^ctg/(?P<title>\w+)$', views.CategoriesView.as_view(), name="category"),
    path(r'prd/', views.ProductView.as_view(), name='product'),
]
