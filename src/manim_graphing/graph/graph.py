from manim import Scene, GraphScene, Text, Write


class _Base:
    def __init__(self, data=None, title=None):
        self.title = title
        self.data = data

        if self.data != None:
            if type(self.data) == dict:
                self.labels = [*self.data.keys()]
                self.values = [*self.data.values()]

    def display_title(self, x, y):
        if self.title != None:
            Title = Text(self.title).move_to([x, y, 0])
            self.play(Write(Title))


class Graph(_Base, Scene):
    def __init__(self, data, title=None):
        _Base.__init__(self, data, title)
        Scene.__init__(self)


class Plot(_Base, GraphScene):
    def __init__(self, data, title=None, **kwargs):
        _Base.__init__(self, data, title)
        GraphScene.__init__(self, **kwargs)
