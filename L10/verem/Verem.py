from typing import Any

class Verem:
    def __init__(self) -> None:
        self._values: list[Any] = []

    def __str__(self) -> str:
        return f"{self._values}"[:-1]
    def ures(self) -> bool:
        return len(self._values) == 0
    def betesz(self, value: Any) -> None:
        self._values.append(value)
    def kivesz(self) -> Any | None:
        if(not self.ures()):
            return self._values.pop()
        else:
            return None
    def meret(self) -> int:
        return len(self._values)
    def get_current(self) -> Any | None:
        return self._values[-1]