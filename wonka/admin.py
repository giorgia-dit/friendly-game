from django.contrib import admin
from .models import Friend, Delivery

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "country", "has_prize", "user")
    search_fields = ("first_name", "last_name", "address")

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ("pk", "friend", "status", "eta")
    list_filter = ("status",)

