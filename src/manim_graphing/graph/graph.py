from manim import Scene, GraphScene


class _Base:
    def __init__(self, data, title=None):
        self.title = title
        self.data = data  # {"Hi": 5, "Bye":69}

        self.labels = [*self.data.keys()]
        self.values = [*self.data.values()]

        print(self.labels)


class Graph(_Base, Scene):
    def __init__(self, data, title=None):
        _Base.__init__(self, data, title)
        Scene.__init__(self)


class Plot(_Base, GraphScene):
    def __init__(self, data, title=None):
        _Base.__init__(self, data, title)
        Scene.__init__(self)
