"""File for storing animations"""

from manim import *
from .graph.graph import Graph

#TODO: Make a pull and add this to manim.
class DefaultCreation(AnimationGroup):
    def __init__(self, graph: Graph) -> None:
        animation = graph.get_default_animation()

        if animation is None:
            raise TypeError(f"{graph.__class__.__name__} does not support this animation")

        super().__init__(*animation)