from manim.animation.creation import ShowCreation
from .graph import Plot
from manim import Dot


class SequencePlot(Plot):
    def __init__(self, data, title=None, **kwargs):

        x = {"x_min": 0, "x_max": len(data)}

        for key in ("x_min", "x_max"):
            if key in kwargs:
                setattr(self, key, kwargs[key])
            else:
                kwargs[key] = x[key]

        super().__init__(data, title, **kwargs)

    def construct(self):
        self.setup_axes()

        for time, dat in enumerate(self.data):
            dot = Dot().move_to(self.coords_to_point(time, dat))
            self.play(ShowCreation(dot))
