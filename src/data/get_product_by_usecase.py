from domain.products.get_product_by_domain import GetProductByDomain
from domain.products.product import TypeProduct
from domain.repository.products_repository import ProductsRepository


class GetProductByUseCase(GetProductByDomain):
    def __init__(self, productsRepository: ProductsRepository):
        self.__productsRepository = productsRepository
  
    async def execute(self, id: str) -> TypeProduct:
        return await self.__productsRepository.get_by_id(id)