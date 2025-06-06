from data.create_product_usecase import CreateProductUseCase
from data.drop_product_usecase import DropProductUseCase
from data.list_products_usecase import ListProductsUseCase
from domain.products.drop_product_domain import DropProductDomain
from domain.products.list_products_domain import ListProductDomain
from infra.repository.products_mongo_repository import ProductsMongoRepository


def list_products() -> ListProductDomain:
  productsMongoRepository = ProductsMongoRepository()
  listProductsUseCase = ListProductsUseCase(productsMongoRepository)
  
  return listProductsUseCase

def drop_product() -> DropProductDomain:
  productsMongoRepository = ProductsMongoRepository()
  listProductsUseCase = DropProductUseCase(productsMongoRepository)
  
  return listProductsUseCase

def create_product():
  productsMongoRepository = ProductsMongoRepository()
  createProductUseCase = CreateProductUseCase(productsMongoRepository)
  
  return createProductUseCase