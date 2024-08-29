import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm

def index(request):
    file_path = 'orders.xlsx'
    
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        data = df.to_dict(orient='records')
    except FileNotFoundError:
        data = []
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            new_data = pd.DataFrame([data])

            try:
                df = pd.read_excel(file_path, engine='openpyxl')
                df = pd.concat([df, new_data], ignore_index=True)
            except FileNotFoundError:
                df = new_data

            df.to_excel(file_path, index=False, engine='openpyxl')
            
            return redirect('index')
        else:
            return HttpResponse("Invalid form data", status=400)
    else:
        form = ProductForm()

    return render(request, 'index.html', {'form': form, 'data': data})

def product_detail(request, product_id):
    file_path = 'orders.xlsx'
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        product = df[df['OrderID'] == int(product_id)]
        if product.empty:
            return HttpResponse("Product not found", status=404)
        return render(request, 'product_detail.html', {'product': product.to_dict(orient='records')[0]})
    except FileNotFoundError:
        return HttpResponse("Orders file not found", status=404)
