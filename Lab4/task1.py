class Vehicle:


    def __init__(self, make: str, model: str, year: int):
        self._make = make
        self._model = model
        self._year = year

    @property
    def make(self) -> str:
        return self._make

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(make={self.make!r}, model={self.model!r}, year={self.year!r})"

    def __str__(self) -> str:
        return f"{self.make} {self.model} ({self.year})"


# Дочерний класс
class Car(Vehicle):

    def __init__(self, make: str, model: str, year: int, seats: int = 4):
        super().__init__(make, model, year)
        self._seats = seats

    @property
    def seats(self) -> int:
        return self._seats

    def __repr__(self) -> str:
        return f"{super().__repr__()[:-1]}, seats={self.seats!r})"

    def __str__(self) -> str:
        return f"{super().__str__()} (количество мест: {self.seats})"


# Дочерний класс
class Truck(Vehicle):

    def __init__(self, make: str, model: str, year: int, max_load: float):
        super().__init__(make, model, year)
        self._max_load = max_load

    @property
    def max_load(self) -> float:
        return self._max_load

    def __repr__(self) -> str:
        return f"{super().__repr__()[:-1]}, max_load={self.max_load!r})"

    def __str__(self) -> str:
        return f"{super().__str__()} (максимальная грузоподъемность: {self.max_load} тонн)"

if __name__ == "__main__":
    car = Car(make="Toyota", model="Corolla", year=2020, seats=5)
    truck = Truck(make="Volvo", model="FH16", year=2018, max_load=40.0)

    print(car)
    print(truck)