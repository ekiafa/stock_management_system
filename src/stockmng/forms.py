from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields=['symbol','name','sector','price','price_earnings']


class StockSearchForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields=["name","sector"]
