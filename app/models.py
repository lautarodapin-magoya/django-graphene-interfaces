from django.db import models

# Create your models here.


class Sale(models.Model):
    pass


class WarrantyClaim(models.Model):
    pass


class SupplyOrder(models.Model):
    sale = models.OneToOneField(
        Sale, models.CASCADE, related_name="supply_order", null=True, blank=True
    )
    warranty_claim = models.OneToOneField(
        WarrantyClaim,
        models.CASCADE,
        related_name="supply_order",
        null=True,
        blank=True,
    )

    class Meta:
        constraints = [
            # models.CheckConstraint(
            #     name="sale_or_warranty_claim",
            #     check=models.Q(sale__isnull=False, warranty_claim__isnull=False)
            #     | models.Q(sale__isnull=True, warranty_claim__isnull=True),
            #     violation_error_message="Either sale or warranty_claim must be set",
            # )
        ]
