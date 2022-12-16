from django.shortcuts import render
from django.views import generic as views
from products import forms as products_forms
from products import models as products_models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from user import models as user_models


# products views

class ProductCreateView(views.CreateView):
    template_name = "products/products_pages/products_create.html"
    model =  products_models.ProductsModel
    form_class = products_forms.ProductsForm
    success_url = reverse_lazy("core:home")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    

class ProductListView(views.ListView):
    template_name = "products/products_pages/products_list.html"
    model = products_models.ProductsModel
    paginate_by = 20
    context_object_name = "products"










class CatogoryListView(views.ListView):
    template_name = "products/catogory/category_list.html"
    model = products_models.CategoryModel
    context_object_name = "categories"




class ProductDetailView(views.DetailView):
    template_name = "products/products_pages/products_detail.html"
    model = products_models.ProductsModel
    context_object_name = "product"


# ****************************products includes views******************************************#

class UserProductIncludesView(views.ListView):
    template_name = "products/product_includes/product_list_by_user.html"
    model = products_models.ProductsModel
    context_object_name = "product"



#  user profilr with ads page views here

class UserProfileProducts(views.ListView):
    template_name = "user/user_products/user_profile_products.html"
    model = products_models.ProductsModel
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__id=self.kwargs.get("pk"))
        return qs