from manim import Scene, GraphScene, Text, Write, UP


class _Base:
    def __init__(self, data=None, title=None):
        self.title = title
        self.data = data

        if self.data != None:
            self.labels = [*self.data.keys()]
            self.values = [*self.data.values()]

    def display_title(self, y):
        if self.title != None:
            Title = Text(self.title).move_to(UP * y)
            self.play(Write(Title))


class Graph(_Base, Scene):
    def __init__(self, data, title=None):
        _Base.__init__(self, data, title)
        Scene.__init__(self)


class Plot(_Base, GraphScene):
    def __init__(self, data, title=None):
        _Base.__init__(self, data, title=title)
        GraphScene.__init__(self)
