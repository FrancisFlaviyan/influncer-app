from django.db import models

class AllData(models.Model):
    brand_name = models.CharField(max_length=100)
    brand_product = models.CharField(max_length=100, blank=True, null=True)
    
    campaign_name = models.CharField(max_length=100)
    campaign_type = models.CharField(max_length=50, blank=True, null=True)
    campaign_start_date = models.DateField(blank=True, null=True)
    campaign_end_date = models.DateField(blank=True, null=True)

    engagement_notes = models.TextField(blank=True, null=True)

    termsConditionsInfo=models.TextField(blank=True, null=True)

    income_statement_last_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    income_statement_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)