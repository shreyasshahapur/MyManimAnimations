from manim import *


def show_positional_values_2D(self, obj):
    show_critical_points_2D(self, obj)
    show_half_length_2D(self, obj)
    show_critical_coords_2D(self, obj)


def show_critical_points_2D(self, obj):

    self.play(
        Write(Dot(obj.get_critical_point(DOWN + LEFT))),
        Write(Dot(obj.get_critical_point(DOWN))),
        Write(Dot(obj.get_critical_point(DOWN + RIGHT))),
        Write(Dot(obj.get_critical_point(LEFT))),
        Write(Dot(obj.get_critical_point(ORIGIN))),
        Write(Dot(obj.get_critical_point(RIGHT))),
        Write(Dot(obj.get_critical_point(UP + LEFT))),
        Write(Dot(obj.get_critical_point(UP))),
        Write(Dot(obj.get_critical_point(UP + RIGHT))),
        run_time=0.5
    )


def show_half_length_2D(self, obj):

    horizontal_distance = obj.get_width() / 2
    vertical_distance = obj.get_height() / 2
    horizontal_line = DashedLine(
        start=obj.get_critical_point(DOWN + LEFT),
        end=obj.get_critical_point(DOWN)
    )
    vertical_line = DashedLine(
        start=obj.get_critical_point(DOWN + LEFT),
        end=obj.get_critical_point(LEFT)
    )

    self.play(
        Write(horizontal_line),
        Write(vertical_line),
        Write(
            TextMobject(str(horizontal_distance)).scale(0.75).next_to(horizontal_line, DOWN)
        ),
        Write(
            TextMobject(str(vertical_distance)).scale(0.75).next_to(vertical_line, LEFT)
        ),
        run_time=0.5
    )


def show_critical_coords_2D(self, obj):

    bottom_left = obj.get_critical_point(LEFT+DOWN).tolist()
    bottom_right = obj.get_critical_point(RIGHT+DOWN).tolist()
    top_left = obj.get_critical_point(LEFT+UP).tolist()
    top_right = obj.get_critical_point(RIGHT+UP).tolist()
    center = obj.get_critical_point(ORIGIN).tolist()

    bottom_left_text = "(" + str(bottom_left[0]) + ", " + str(bottom_left[1]) + ")"
    bottom_right_text = "(" + str(bottom_right[0]) + ", " + str(bottom_right[1]) + ")"
    top_left_text = "(" + str(top_left[0]) + ", " + str(top_left[1]) + ")"
    top_right_text = "(" + str(top_right[0]) + ", " + str(top_right[1]) + ")"
    center_text = "(" + str(center[0]) + ", " + str(center[1]) + ")"

    self.play(
        Write(
            TextMobject(bottom_left_text).scale(0.6).next_to(obj.get_critical_point(LEFT+DOWN), LEFT+DOWN)
        ),
        Write(
            TextMobject(bottom_right_text).scale(0.6).next_to(obj.get_critical_point(RIGHT + DOWN), RIGHT + DOWN)
        ),
        Write(
            TextMobject(top_left_text).scale(0.6).next_to(obj.get_critical_point(LEFT + UP), LEFT + UP)
        ),
        Write(
            TextMobject(top_right_text).scale(0.6).next_to(obj.get_critical_point(RIGHT+UP), RIGHT+UP)
        ),
        Write(
            TextMobject(center_text).scale(0.6).next_to(obj.get_critical_point(ORIGIN), UP)
        )
    )