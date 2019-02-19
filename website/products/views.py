from django.shortcuts import render

# Create your views here.
def product (request):
    return render(request, 'product.html',{'name':'product'})


def product_detail(request):
    return render(request, 'product_detail.html',{'name':'product_detail'})