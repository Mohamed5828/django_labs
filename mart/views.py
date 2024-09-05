from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm
from products.models import Product
from django.views.generic import TemplateView

def index(request):
    products = Product.objects.filter(active=True)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid form data", status=400)
    else:
        form = ProductForm()

    return render(request, 'mart/index.html', {'form': form, 'products': products})


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return render(request, 'mart/product_detail.html', {'product': product})
    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)


class CBVView(TemplateView):
    template_name = 'mart/cbvTest.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello world')

    def post(self, request, *args, **kwargs):
        return HttpResponse('This is a POST request')
