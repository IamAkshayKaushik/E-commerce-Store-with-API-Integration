from django import forms
from .models import Product, Category, Attribute

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ['name']