from typing import List
from bson import ObjectId
from pymongo import MongoClient

from domain.repository.products_repository import ProductsRepository, TypeProductModel


class ProductsMongoRepository(ProductsRepository):
  def __init__(self):
    self.__client =  MongoClient('mongodb://localhost:27017/')
    self.__database = self.__client['py-stock']
    self.__collection = self.__database['products']
    
  
  def _to_dto(self, doc):
    return {
      "id": str(doc["_id"]),
      "name": doc["name"],
      "price": doc["price"],
      "stock_total": doc["stock_total"]
    }
    
  async def create(self, product: TypeProductModel) -> TypeProductModel:
    return self.__collection.insert_one(product)
  
  async def list(self) -> List[TypeProductModel]:
    cursor = self.__collection.find()
    products = []
    
    for doc in cursor:
      products.append(self._to_dto(doc))
      
    return products
  
  async def get_by_id(self, id) -> TypeProductModel:
    document = self.__collection.find_one({
      "_id": ObjectId(id)
    })
    
    return self._to_dto(document)
  
  async def delete(self, id: str):
    self.__collection.delete_one({
      "_id": ObjectId(id)
    })
    