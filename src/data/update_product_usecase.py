from domain.products.product import TypeProduct
from domain.products.update_product_domain import UpdateProductDomain
from domain.repository.products_repository import ProductsRepository


class UpdateProductUseCase(UpdateProductDomain):
    def __init__(self, productsRepository: ProductsRepository):
        self.__productsRepository = productsRepository
        
        
    async def execute(self, product: TypeProduct):
        await self.__productsRepository.update_by_id(product)