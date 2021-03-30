from manim import *
from ..graph.graph import *
import typing


class MarkerPlot(Plot):
    def __init__(self, values: typing.List[typing.Union[float, int]]) -> None:
        super().__init__()

        self.values = values

        self.axes = Axes(
            x_range=[0, len(values) + 1, 1],
            y_range=[min(values) if min(values) < 0 else 0, max(values) +1, 1],
            x_length=9,
            y_length=6,
        )

        self.add(self.axes)
        self.plot()

    def plot(self) -> None:
        for i, value in enumerate(self.values, start=1):
            self.add(Dot(self.axes.coords_to_point(i, value)))


class DotPlot(Plot):
    def __init__(self, values: typing.List[typing.Union[float, int]]) -> None:
        super().__init__()
        values.sort()
        self.values = values

        print(max(values))

        self.axes = Axes(
            x_range=[min(values) if min(values) < 0 else 0, max(values) + 1, 1],
            y_range=[0, max(values) + 1, 1],
            x_length=9,
            y_length=6,
        )

        self.add(self.axes)
        self.plot()

    def plot(self) -> None:
        last_val = None

        for value in self.values:
            if value != last_val:
                last_val = value
                i = 1

            self.add(Dot([self.axes.coords_to_point(value, i)]))
            i += 1

class LinePlot(Plot):
    def __init__(self, values: typing.List[typing.Union[float, int]]) -> None:
        super().__init__()

        self.values = values

        self.axes = Axes(
            x_range=[0, len(values) + 1, 1],
            y_range=[min(values) if min(values) < 0 else 0, max(values) + 1, 1],
            x_length=9,
            y_length=6,
        )

        self.add(self.axes)
        self.plot()

    def plot(self) -> None:
        last_point = None
        for i, value in enumerate(self.values, start=1):
            point = Dot(self.axes.coords_to_point(i, value))

            if last_point is not None:
                self.add(Line(point.get_center(), last_point))
            
            last_point = point.get_center()
            self.add(point)
