from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, area):
        self.area = area
    
    @abstractmethod
    def calculate_quantity(self):
        pass
    
    @abstractmethod
    def calculate_cost(self):
        pass

class Wallpaper(Material):
    def calculate_quantity(self):
        pass
    
    def calculate_cost(self):
        pass

class Tile(Material):
    def calculate_quantity(self):
        pass
    
    def calculate_cost(self):
        pass

class Laminate(Material):
    def calculate_quantity(self):
        pass
    
    def calculate_cost(self):
        pass
