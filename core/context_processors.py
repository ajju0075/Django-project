from products.models import CategoryModel, ProductsModel


def common_data(request):
    categories = CategoryModel.objects.all()
    context = {
        "categories": categories,
        
    }
    return context


# def common_data(request):
#     product = ProductsModel.objects.all()
#     context = {
#         "product": product,
#     }
#     return context
