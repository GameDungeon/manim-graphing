"""Where the base graphs are stored."""

from manim import *
import typing


class Graph(VMobject):
    """Base Class for this plugins graphs."""

    def __init__(self) -> None:
        super().__init__()


class Plot(Graph):
    """Base class for plots."""

    def __init__(self) -> None:
        super().__init__()

    def plot(self, values: typing.List[typing.Union[float, int]]) -> None:
        """To Be Defined in Child Classes."""
        pass
