from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int


class MousePositions:
    anki_expression = Coordinates(1541, 167)
    anki_scroll_bar = Coordinates(1430, 114)
    copy_position = Coordinates(1464, 821)
    input_position = Coordinates(1041, 936)
    top_scroll_bar = Coordinates(1914, 214)
    bottom_scroll_bar = Coordinates(1914, 860)
