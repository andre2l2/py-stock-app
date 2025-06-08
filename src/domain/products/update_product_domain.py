from abc import ABC, abstractmethod


class UpdateProductDomain(ABC):
  @abstractmethod
  def execute(self):
    pass