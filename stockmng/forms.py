from django import forms
from .models import Stock


class StockCreateForm(forms.ModelForm):
   class Meta:
       model=Stock
       fields=['symbol','name','sector','price','price_earnings','dividend_yield',	'earnings_share','fifty_two_week_low','fifty_two_week_high','market_cap','ebitda','price_sales','price_book','sec_fillings'
]
