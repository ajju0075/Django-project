from django.urls import path 
from products import views as products_views

app_name = "products"
urlpatterns = [

    path("products/create",products_views.ProductCreateView.as_view(), name = "products_create"),

    

    path("product_list/",products_views.ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/details/",products_views.ProductDetailView.as_view(), name="product_details"),
    

    path("user_product_list/", products_views.UserProductIncludesView.as_view(), name="user_product_list"),
    path("profile/<int:pk>/products/",products_views.UserProfileProducts.as_view(), name= "profile_products" ),



]