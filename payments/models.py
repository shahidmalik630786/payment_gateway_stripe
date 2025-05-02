from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, related_name='payment', on_delete=models.CASCADE, blank=True, null=True)
    stripe_checkout_session_id = models.CharField(max_length=255)
    stripe_payment_intent_id = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.IntegerField(null=True,blank=True)
    product = models.CharField(max_length=30, null=True,blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
