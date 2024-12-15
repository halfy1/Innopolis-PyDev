from abc import ABC, abstractmethod
import doctest


class Car(ABC):
    def __init__(self, brand: str, max_speed: float, fuel_capacity: float):

        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом")
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Вместимость бака должна быть положительным числом")

        self.brand = brand
        self.max_speed = max_speed
        self.fuel_capacity = fuel_capacity

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Проехать определенное расстояние.
        :param distance: Расстояние для поездки
        """

    @abstractmethod
    def refuel(self, amount: float) -> None:
        """
        Заправить бак автомобиля.
        :param amount: Объем топлива для заправки
        """


class Box(ABC):
    def __init__(self, length: float, width: float, height: float):

        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина должна быть положительным числом")
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")

        self.length = length
        self.width = width
        self.height = height

    @abstractmethod
    def open(self) -> None:
        """
        Открыть коробку.
        """

    @abstractmethod
    def close(self) -> None:
        """
        Закрыть коробку.
        """


class TelegramBot(ABC):
    def __init__(self, bot_name: str, token: str):

        if not isinstance(bot_name, str):
            raise TypeError("Имя бота должно быть строкой")
        if not isinstance(token, str):
            raise TypeError("Токен должен быть строкой")

        self.bot_name = bot_name
        self.token = token

    @abstractmethod
    def send_message(self, chat_id: int, message: str) -> None:
        """
        Отправить сообщение пользователю.
        :param chat_id: Идентификатор чата
        :param message: Сообщение для отправки
        """

    @abstractmethod
    def receive_message(self) -> str:
        """
        Получить сообщение от пользователя.
        :return: Текст сообщения
        """


if __name__ == "__main__":
    doctest.testmod()
