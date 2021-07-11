from django.db import models

# Create your models here.

class Stock(models.Model):
    symbol=models.CharField(max_length=50,blank=True,null=True)
    name=models.CharField(max_length=50,blank=True,null=True)
    sector=models.CharField(max_length=50,blank=True,null=True)
    price=models.FloatField(default="0",blank=True,null=True)
    price_earnings=models.FloatField(default="0",blank=True,null=True)
    dividend_yield=models.FloatField(default="0",blank=True,null=True)
    earnings_share=models.FloatField(default="0",blank=True,null=True)
    fifty_two_week_low=models.FloatField(default="0",blank=True,null=True)
    fifty_two_week_high=models.FloatField(default="0",blank=True,null=True)
    market_cap=models.FloatField(default="0",blank=True,null=True)
    ebitda=models.FloatField(default="0",blank=True,null=True)
    price_sales=models.FloatField(default="0",blank=True,null=True)
    price_book=models.FloatField(default="0",blank=True,null=True)
    sec_fillings=models.CharField(max_length=50,blank=True,null=True)

def _str_(self):
    return self.symbol +" | "+ self.name +" | "+ self.sector +" | "+ str(self.price) +" | "+ str(self.price_earnings)+" | "+ str(self.dividend_yield) +" | "+ str(self.earnings_share)+" | "+str(self.fifty_two_week_low)+" | "+str(self.fifty_two_week_high)+" | "+str(self.market_cap)+" | "+str(self.ebitda)+" | "+str(self.price_sales)+" | "+str(self.price_book)+" | "+self.sec_fillings


