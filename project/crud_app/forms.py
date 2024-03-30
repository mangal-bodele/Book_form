from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'book_name' : forms.TextInput(attrs={'class':"form-control"}),
            'author' : forms.TextInput(attrs={'class':"form-control"}),
            'publication' : forms.TextInput(attrs={'class':"form-control"}),
            'date_of_publish' : forms.DateInput(attrs={'type':'date','class':"form-control"}),
            'price' : forms.NumberInput(attrs={'class':"form-control"})
        }
