from django.contrib import admin

from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "phone_number", "city")
    search_fields = ("email", "city")
    ordering = ("-date",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date", "course", "lesson", "amount", "payment_method")
    search_fields = ("user", "course", "lesson")
    ordering = ("-date",)
