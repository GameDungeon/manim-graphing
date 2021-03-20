from manim import *
from .graph import Graph


class PieChart(Graph):
    def construct(self):

        self.pie_colors = [YELLOW, GREEN, BLUE, ORANGE, RED]

        angles = [x / sum(self.values) * 360 * DEGREES for x in self.values]
        sectors = []
        label_ani = []
        current_angle = 0

        Pie = Circle(stroke_color=WHITE, fill_opacity=0)
        up_line = Line(Pie.get_center(), UP)

        for i, angle in enumerate(angles):
            a_point = Pie.point_at_angle(current_angle)
            a2_point = Pie.point_at_angle(angle)
            color = self.pie_colors[i + 1 % len(self.pie_colors)]

            piece = ArcPolygonFromArcs(
                ArcBetweenPoints(Pie.get_center(), a_point, angle=0),
                Arc(start_angle=current_angle, angle=angle, radius=1),
                ArcBetweenPoints(Pie.get_center(), a2_point, angle=0, stroke_opacity=0),
                color=color,
                stroke_color=WHITE,
                fill_opacity=1,
                stroke_opacity=0,
            )

            label_ani.append(
                Write(
                    Text(self.labels[i])
                    .scale(0.4)
                    .move_to(Pie.point_at_angle(current_angle + (angle / 2)) * 1.5)
                    .rotate(90 * DEGREES, about_point=Pie.get_center())
                    .rotate(-90 * DEGREES)
                )
            )

            piece.rotate(90 * DEGREES, about_point=Pie.get_center())

            current_angle += angle
            sectors.append(piece)

        self.display_title(2)
        self.play(ShowCreation(Pie))
        self.add_foreground_mobject(Circle(color=WHITE, radius=0.01, fill_opacity=1))
        self.add_foreground_mobject(up_line)
        self.play(*[DrawBorderThenFill(sector) for sector in sectors])
        self.play(*[ani for ani in label_ani])
