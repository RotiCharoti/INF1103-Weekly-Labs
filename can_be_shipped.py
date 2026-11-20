from abc import ABC, abstractmethod

class CanBeShipped(ABC):
    @abstractmethod 
    def calculate_shipping_cost(self) -> float: # returns shipping cost of physical product
        pass
