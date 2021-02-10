from manim import *


class GridAxes(VMobject):

    def __init__(self, height=4, width=7, color_axes=BLUE, **kwargs):
        self.height = height
        self.width = width
        self.color_axes = color_axes

        VMobject.__init__(self, **kwargs)

        x_axis = Line(start=self.width * LEFT, end=self.width * RIGHT).set_color(self.color_axes)
        y_axis = Line(start=self.height * DOWN, end=self.height * UP).set_color(self.color_axes)

        axes = VGroup(x_axis, y_axis)
        self.add(axes)

        for x in range(-width, width + 1):
            num = Tex(str(x)) \
                .scale(0.6) \
                .next_to(x_axis, DOWN) \
                .shift(x*RIGHT)

            self.add(num)

        for y in range(-height, height + 1):
            num = Tex(str(y)) \
                .scale(0.6) \
                .next_to(y_axis, LEFT) \
                .shift(y * UP)

            self.add(num)


class Grid(GridAxes):

    def __init__(self, line_type="dashed", color_lines=WHITE, **kwargs):
        self.line_type = line_type
        self.color_lines = color_lines

        GridAxes.__init__(self, **kwargs)

        # Lines parallel to the x axis
        x_lines = VGroup()
        for y in (list(range(-self.height, 0)) + list(range(1, self.height + 1))):
            x_lines.add(DashedLine(start=self.width * LEFT + y * DOWN, end=self.width * RIGHT + y * DOWN,
                                   dash_length=0.12, positive_space_ratio=0.6)
                        .set_color(self.color_lines))
        x_lines.set_stroke(width=0.75)

        # Lines parallel to the y axis
        y_lines = VGroup()
        for x in (list(range(-self.width, 0)) + list(range(1, self.width + 1))):
            y_lines.add(DashedLine(start=self.height * UP + x * RIGHT, end=self.height * DOWN + x * RIGHT,
                                   dash_length=0.12, positive_space_ratio=0.6).set_color(self.color_lines))
        y_lines.set_stroke(width=0.75)

        self.add(x_lines)
        self.add(y_lines)

