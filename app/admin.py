from django.contrib import admin


from .models import Sale, WarrantyClaim, SupplyOrder

admin.site.register(Sale)
admin.site.register(WarrantyClaim)
admin.site.register(SupplyOrder)
