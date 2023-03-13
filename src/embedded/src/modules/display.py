import dType


class Display:
    @staticmethod
    def print(text: str) -> None:
        dType.PrintInfo(0, text)

    @staticmethod
    def set_progress_bar(progress: int) -> None:
        dType.SetProgbar(0, int(progress))
