from manim.animation.creation import ShowCreation
from .graph import _Base
from manim import GraphScene


class PlotFunction(_Base, GraphScene):
    def __init__(self, function, title=None, **kwargs):
        _Base.__init__(self, title=title)
        GraphScene.__init__(self, **kwargs)

        self.function = function

    def construct(self):
        self.setup_axes()
        graph = self.get_graph(self.function)
        self.play(ShowCreation(graph))
