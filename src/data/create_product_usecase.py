from domain.products.create_product_domain import CreateProductDomain
from domain.repository.products_repository import ProductsRepository, TypeProductModel


class CreateProductUseCase(CreateProductDomain):
    def __init__(self, productsRepository: ProductsRepository):
        self.__productsRepository = productsRepository
        
        
    async def execute(self, product: TypeProductModel):
        await self.__productsRepository.create(product)