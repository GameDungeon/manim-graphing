"""Utility functions go here"""

from manim import *
from .animation import DefaultCreation


def show_graph(graph) -> None:
    class Show(Scene):
        def __init__(self, graph) -> None:
            super().__init__()
            self.graph = graph

        def construct(self) -> None:
            self.add(self.graph)
            self.wait(5)

    Show(graph).render(True)


def animate_graph(graph) -> None:
    class Show(Scene):
        def __init__(self, graph) -> None:
            super().__init__()
            self.graph = graph

        def construct(self) -> None:
            self.play(DefaultCreation(self.graph))

    Show(graph).render(True)


