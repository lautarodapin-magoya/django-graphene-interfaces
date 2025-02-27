from django.db.migrations import graph
import graphene
from graphene_django import DjangoObjectType

from app.models import WarrantyClaim, Sale, SupplyOrder


class WarrantyClaimType(DjangoObjectType):
    class Meta:
        model = WarrantyClaim


class SaleType(DjangoObjectType):
    class Meta:
        model = Sale


class SupplyOrderWithWarrantyClaimType(DjangoObjectType):
    warranty_claim = graphene.Field(WarrantyClaimType, required=True)

    class Meta:
        exclude = ("sale",)
        model = SupplyOrder


class SupplyOrderWithSaleType(DjangoObjectType):
    sale = graphene.Field(SaleType, required=True)

    class Meta:
        exclude = ("warranty_claim",)
        model = SupplyOrder


class SupplyOrderUnion(graphene.Union):
    class Meta:
        types = (
            SupplyOrderWithWarrantyClaimType,
            SupplyOrderWithSaleType,
        )

    @classmethod
    def resolve_type(cls, instance: SupplyOrder, info):
        if instance.sale is not None:
            return SupplyOrderWithSaleType
        return SupplyOrderWithWarrantyClaimType


class Query(graphene.ObjectType):
    supply_orders = graphene.List(SupplyOrderUnion)

    def resolve_supply_orders(self, info):
        return SupplyOrder.objects.all()


schema = graphene.Schema(query=Query)
