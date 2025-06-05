from domain.products.drop_product_domain import DropProductDomain
from domain.products.product import TypeProduct
from domain.repository.products_repository import ProductsRepository


class DropProductUseCase(DropProductDomain):
    def __init__(self, productsRepository: ProductsRepository):
        self.__productsRepository = productsRepository
        
        
    async def execute(self, id: str) -> list[TypeProduct]:
        return await self.__productsRepository.delete(id)