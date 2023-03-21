from modules import Display, Keyboard, Time, Buzzer


class Page:
    __name = None
    __values_mappping = {}

    def init(self, name: str) -> None:
        self.__name = name

    def update(self) -> None:
        pass

    @staticmethod
    def get_value(key: str):
        return Page.__values_mappping.get(key, None)

    @staticmethod
    def set_value(key: str, value) -> None:
        Page.__values_mappping[key] = value

    @staticmethod
    def get_values() -> dict:
        return Page.__values_mappping

    @staticmethod
    def clear_values() -> None:
        Page.__values_mappping = {}

    @property
    def name(self) -> str:
        return self.__name
