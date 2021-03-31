from manim import *
from .graph import *


class PieChart(Graph):
    def __init__(self, data: dict, display_labels: bool = True):
        super().__init__()

        self.animations = None

        self.pie_colors = [YELLOW, GREEN, BLUE, ORANGE, RED]

        self.labels = list()
        self.values = list()

        for key, value in data.items():
            self.labels.append(key)
            self.values.append(value)

        angles = [x / sum(self.values) * 360 * DEGREES for x in self.values]
        sectors = list()
        labels = list()
        current_angle = 0

        pie = Circle(stroke_color=WHITE, fill_opacity=0)

        center_point = Circle(color=WHITE, radius=0.01, fill_opacity=1).move_to(
            pie.get_center()
        )
        up_line = Line(pie.get_center(), UP)

        center_point.z_index = 2
        up_line.z_index = 1

        for i, angle in enumerate(angles):
            a_point = pie.point_at_angle(current_angle)
            a2_point = pie.point_at_angle(angle)
            color = self.pie_colors[i + 1 % len(self.pie_colors)]

            piece = ArcPolygonFromArcs(
                ArcBetweenPoints(pie.get_center(), a_point, angle=0),
                Arc(start_angle=current_angle, angle=angle, radius=1),
                ArcBetweenPoints(pie.get_center(), a2_point, angle=0, stroke_opacity=0),
                color=color,
                stroke_color=WHITE,
                fill_opacity=1,
                stroke_opacity=0,
            )

            if display_labels:
                labels.append(
                    Text(self.labels[i])
                    .scale(0.4)
                    .move_to(pie.point_at_angle(current_angle + (angle / 2)) * 1.5)
                    .rotate(90 * DEGREES, about_point=pie.get_center())
                    .rotate(-90 * DEGREES)
                )
                print(self.labels[i])

            piece.rotate(90 * DEGREES, about_point=pie.get_center())

            current_angle += angle
            sectors.append(piece)

        self.add(center_point)
        self.add(up_line)
        self.add(*sectors)
        if labels:
            self.add(*labels)
