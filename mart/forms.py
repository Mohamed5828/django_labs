from django import forms

class ProductForm(forms.Form):
    OrderID = forms.IntegerField(label='Order ID')
    Product = forms.CharField(label='Product Name', max_length=100)
    Quantity = forms.IntegerField(label='Quantity')
    Status = forms.ChoiceField(label='Status', choices=[
        ('requested', 'Requested'),
        ('preparing', 'Preparing'),
        ('delivering', 'Delivering'),
        ('delivered', 'Delivered'),
    ])
