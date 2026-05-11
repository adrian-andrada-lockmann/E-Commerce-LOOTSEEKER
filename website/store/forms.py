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
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe the product, condition, and key details.'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'placeholder': 'Price in cents'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }
