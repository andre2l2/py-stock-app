from abc import ABC, abstractmethod


class CreateProductDomain(ABC):
  @abstractmethod
  def execute(self, name: str, price: str, total: int):
    pass