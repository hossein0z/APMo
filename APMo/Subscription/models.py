from django.db import models
from User.models import Abs_User
from datetime import date

class Subscription(models.Model):
    plan_choices=(('basic', '3 Months'),('medium', '6 Months') , ('premium', '13 Months'))

    user = models.ForeignKey(Abs_User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    plan_type = models.CharField(choices=plan_choices)
    
    @property
    def is_active(self):
        return self.end_date.date() >= date.today()

class Payment(models.Model):
    user = models.ForeignKey(Abs_User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('failed', 'Failed')])
