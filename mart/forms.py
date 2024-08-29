from django import forms
from products.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'active', 'image'] 

    name = forms.CharField(label='Product Name', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    active = forms.BooleanField(label='Active', required=False)
    image = forms.ImageField(label='Product Image', required=False)
