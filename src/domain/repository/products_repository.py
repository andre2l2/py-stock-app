from abc import abstractmethod
from typing import List, TypedDict

class TypeProductModel(TypedDict):
  id: str
  name: str
  price: str
  stock_total: int


class ProductsRepository:
  @abstractmethod
  def create(self, product: TypeProductModel) -> TypeProductModel:
    pass
  
  def list(self) -> List[TypeProductModel]:
    pass
  
  def get_by_id(self) -> TypeProductModel:
    pass
  
  def delete(self, id: str) -> List[TypeProductModel]:
    pass