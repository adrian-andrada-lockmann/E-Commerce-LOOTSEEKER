from django import forms

from .models import Product, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name','last_name','address','zipcode','city')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
widgets = {
    'category': forms.Select(attrs={
        'class': 'form-select'
    }),
    'title': forms.TextInput(attrs={
        'class': "form-control",
        'style': 'max-width: 300px;',
                'placeholder': 'Name'
    }),
    'description': forms.Textarea(attrs={
        'class': 'form-control',
    }),
    'price': forms.TextInput(attrs={
        'class': 'form-control',
    }),
    'image': forms.FileInput(attrs={
        'class': 'form-control',
    })
}   