from data.create_product_usecase import CreateProductUseCase
from data.drop_product_usecase import DropProductUseCase
from data.get_product_by_usecase import GetProductByUseCase
from data.list_products_usecase import ListProductsUseCase
from data.update_product_usecase import UpdateProductUseCase
from domain.products.create_product_domain import CreateProductDomain
from domain.products.drop_product_domain import DropProductDomain
from domain.products.get_product_by_domain import GetProductByDomain
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

def create_product() -> CreateProductDomain:
  productsMongoRepository = ProductsMongoRepository()
  createProductUseCase = CreateProductUseCase(productsMongoRepository)
  
  return createProductUseCase

def get_product_by() -> GetProductByDomain:
  productsMongoRepository = ProductsMongoRepository()
  getProductByUseCase = GetProductByUseCase(productsMongoRepository)
  
  return getProductByUseCase

def update_product_by():
  productsMongoRepository = ProductsMongoRepository()
  updateProductUseCase = UpdateProductUseCase(productsMongoRepository)
  
  return updateProductUseCase