from typing import Dict, Any

from apps.products.models import Product


class ProductRepository:
    """CRUD by pattern REPOSITORY"""
    async def insert_product(self, details: Dict[str, Any]):
        product = await Product.objects.create(**details)
        return product

    async def update_product(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            product = await Product.objects.get(pk=id)
            await product.update(**details)
        except Exception as e:
            return False
        return True

    async def delete_product(self, id: int) -> bool:
        try:
            product = await Product.objects.get(pk=id)
            await product.delete()
        except Exception as e:
            return False
        return True

    async def get_all_product(self):
        return await Product.objects.all()

    async def get_product(self, id: int):
        return await Product.objects.get(pk=id)
