from abc import ABC, abstractmethod
import logging
from typing import Type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Engine started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model}: Engine started")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Type[Vehicle]:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Type[Vehicle]:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Type[Vehicle]:
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Type[Vehicle]:
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Type[Vehicle]:
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Type[Vehicle]:
        return Motorcycle(f"{make} (EU Spec)", model)


def main() -> None:
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()

    vehicle2 = eu_factory.create_motorcycle("Ducati", "Panigale")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
