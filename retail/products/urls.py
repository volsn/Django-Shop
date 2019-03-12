from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductsView.as_view()),
    path(r'^categories/(?P<title>\w+)$', views.CategoriesView.as_view(), name="category"),
]
