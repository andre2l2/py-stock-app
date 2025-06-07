from typing import List

from domain.products.list_products_domain import ListProductDomain
from domain.products.product import TypeProduct
from domain.repository.products_repository import ProductsRepository


class ListProductsUseCase(ListProductDomain):
  def __init__(self, productsRepository: ProductsRepository):
    self.__productsRepository = productsRepository
  
  
  async def execute(self) -> List[TypeProduct]:    
    return await self.__productsRepository.list()