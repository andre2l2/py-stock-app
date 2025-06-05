from abc import ABC, abstractmethod
from typing import List, TypedDict

from domain.products.product import TypeProduct


class ListProductDomain(ABC):
  @abstractmethod
  def execute(self) -> List[TypeProduct]:
    pass