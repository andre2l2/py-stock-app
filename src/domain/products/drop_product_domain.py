from abc import ABC, abstractmethod


class DropProductDomain(ABC):
  @abstractmethod
  def execute(self, id: str):
    pass