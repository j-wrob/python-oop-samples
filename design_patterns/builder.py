class Director():
    """
    Director:
    - init with concrete builder
    - calls Abstract Builder's method to create product
    - calls Concrete Builder's methods to build parts of a product
    - return completed product
    """
    def __init__(self, builder):
        self._builder = builder

    def build_car(self):
        self._builder.create_car()
        self._builder.add_model()
        self._builder.add_engine()
        self._builder.add_color()

    def get_car(self):
        return self._builder.car


class Builder():
    """
    Abstract Builder:
    - init with product = None
    - start instance of a new product
    """
    def __init__(self):
        self.car = None

    def create_car(self):
        self.car = Car()


class SkodaFavorit(Builder):
    """
    Concrete Builder:
    - derives from Abstract Builder,
    - methods to add concrete parts to product
    """
    def add_model(self):
        self.car.model = "Skoda Favorit"

    def add_engine(self):
        self.car.engine = "3.5 Turbo"

    def add_color(self):
        self.car.color = "Golden"


class Fiat126(Builder):
    """
    Concrete Builder:
    - derives from Abstract Builder,
    - methods to add concrete parts to product
    """
    def add_model(self):
        self.car.model = "Fiat 126"

    def add_engine(self):
        self.car.engine = "Hybrid"

    def add_color(self):
        self.car.color = "Black"


class Car():
    """
    Product:
    - act like a blueprint
    - init with parameters = None
    """
    def __init__(self):
        self.model = None
        self.engine = None
        self.color = None
        
    def __str__(self):
        return f'{self.model} | {self.engine} | {self.color}'

for builder in [SkodaFavorit(), Fiat126()]:
    director = Director(builder)
    director.build_car()
    brand_new_car = director.get_car()
    print(brand_new_car)