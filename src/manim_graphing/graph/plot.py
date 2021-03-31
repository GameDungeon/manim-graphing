from manim import *
from ..graph.graph import *
import typing


class LinePlot(Plot):
    def __init__(self, *values: typing.List[typing.Union[float, int]], dot_points: bool = False) -> None:
        super().__init__()

        self.dot_points = dot_points

        self.colors = ["RED", "BLUE", "GREEN"]

        self.axes = Axes(
            x_range=[0, max([len(x) for x in values]) + 1, 1],
            y_range=[0, max([max(a) for a in values]) + 1, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": False, "include_numbers": True},
        )

        self.add(self.axes)

        for i, value in enumerate(values):
            self.value = value
            self.plot(self.colors[i])

    def plot(self, color: str) -> None:
        last_point = None
        for i, value in enumerate(self.value, start=1):
            point = self.axes.coords_to_point(i, value) 

            if last_point is not None:
                self.add(Line(point, last_point, stroke_width=3, color=color))

            last_point = point

            if self.dot_points:
                self.add(Dot(point, color=color))


class MarkerPlot(Plot):
    """Like a line plot, but with dots instead of lines."""

    def __init__(self, *values: typing.List[typing.Union[float, int]]) -> None:
        super().__init__()

        self.colors = ["RED", "BLUE", "GREEN"]

        self.axes = Axes(
            x_range=[0, max([len(x) for x in values]) + 1, 1],
            y_range=[0, max([max(a) for a in values]) + 1, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": False, "include_numbers": True},
        )

        self.add(self.axes)

        for i, value in enumerate(values):
            self.value = value
            self.plot(self.colors[i])


    def plot(self, color: str) -> None:
        for i, value in enumerate(self.value, start=1):
            self.add(Dot(self.axes.coords_to_point(i, value), color=color))


class ScatterPlot(Plot):
    def __init__(
        self, *values: typing.Tuple[typing.Union[float, int], typing.Union[float, int]]
    ) -> None:
        super().__init__()

        self.colors = ["RED", "BLUE", "GREEN"]

        self.axes = Axes(
            x_range=[0, max([x[0] for y in values for x in y]) + 1, 1],
            y_range=[0, max([x[1] for y in values for x in y]) + 1, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_tip": False, "include_numbers": True},
        )

        self.add(self.axes)

        for i, value in enumerate(values):
            for _ in value:
                for x, y in value:
                    self.x = x
                    self.y = y
                    self.plot(self.colors[i])

    def plot(self, color: str) -> None:
        self.add(Dot(self.axes.coords_to_point(self.x, self.y), color=color))

class DotPlot(Plot):
    def __init__(self, values: typing.List[typing.Union[float, int]]) -> None:
        super().__init__()
        values.sort()
        self.values = values

        print(max(values))

        self.axes = Axes(
            x_range=[0, len(values) + 1, 1],
            y_range=[0, max(values) + 1, 1],
            x_length=9,
            y_length=6,
            x_labeled_nums=range(0, max(values)),
            axis_config={"include_tip": False},
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
