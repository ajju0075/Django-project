from django.shortcuts import render
from django.views import generic as views
from products import forms as products_forms
from products import models as products_models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth import get_user_model
from user import models as user_models

from django.conf import settings
from django.db.models import Q 

# Create your models here.
USER = get_user_model()

# products views

class ProductCreateView(views.CreateView):
    template_name = "products/products_pages/products_create.html"
    model =  products_models.ProductsModel
    form_class = products_forms.ProductsForm
    success_url = reverse_lazy('products:products_in_profile')
    
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





#  user profilr with ads page views here

class UserProfileProducts(views.ListView):
    template_name = "user/user_products/user_profile_products.html"
    model = products_models.ProductsModel
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_detail"] = USER.objects.get(id=self.kwargs.get("pk"))
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user__id=self.kwargs.get("pk"))
        return qs




class UserProductsInProfile(views.ListView):
    template_name = "products/products_in_profile.html"
    model = products_models.ProductsModel
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = context['products'].filter(user=self.request.user)

        return context

class UserProductsUpdateView( PermissionRequiredMixin, views.UpdateView):
    template_name = "products/products_pages/products_update.html"
    model = products_models.ProductsModel
    fields =  ["product_name", "price", "description"]
    success_url = reverse_lazy('products:products_in_profile')

    def has_permission(self):
        user = self.request.user
        can_update_product = False
        product = products_models.ProductsModel.objects.get(id=self.kwargs.get("pk"))
        if product.user == user:
            can_update_product = True
        return can_update_product


class UserProductsDeleteView(views.DeleteView):
    model = products_models.ProductsModel
    template_name = "products/products_pages/products_delete.html"
    context_object_name = 'products'
    success_url = reverse_lazy('products:products_in_profile')

    def has_permission(self):
        user = self.request.user
        can_delete_product = False
        product = products_models.ProductsModel.objects.get(id=self.kwargs.get("pk"))
        if product.user == user:
            can_delete_product = True
        return can_delete_product


class ProductByCategoryView(views.ListView):
    template_name = "products/products_pages/products_list.html"
    model = products_models.ProductsModel
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        category_id = self.kwargs.get("pk")
        qs = qs.filter(category__id=category_id)
        return qs



class SearchView(views.ListView):
    template_name = "products/products_pages/products_list.html"
    model = products_models.ProductsModel
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get("q")
        qs = qs.filter(product_name__icontains=q)
        return qs


            








 


