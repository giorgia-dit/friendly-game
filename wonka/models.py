from django.db import models
from django.contrib.auth.models import User

class Friend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    has_prize = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Delivery(models.Model):
    friend = models.OneToOneField(Friend, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('preparing', 'Preparing'), ('shipped', 'Shipped'), ('delivered', 'Delivered')],
        default='preparing'
    )
    eta = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Delivery'
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return f"Delivery for {self.friend.first_name} - {self.status}"
    
    def get_status_verbose(self):
        description = {}
        if self.status == 'preparing':
            description['title'] = "It's almost ready!"
            description['content'] = "It just takes veeery little time more..."
        elif self.status == 'shipped':
            description['title'] = "It's on the road!"
            description['content'] = "Are you ready to unveil the mystery?"
        else:
            description['title'] = "Destination!"
            description['content'] = "I really hope you enjoyed it."
        return description