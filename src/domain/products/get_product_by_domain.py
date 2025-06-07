from abc import ABC, abstractmethod

from domain.products.product import TypeProduct


class GetProductByDomain(ABC):
    @abstractmethod
    def execute(self, id: str) -> TypeProduct:
        pass