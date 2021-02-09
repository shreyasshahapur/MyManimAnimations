from manim import *
from MyManimAnimations.tools.show_positional_values_2D import *



# class RightTriangle(Scene):
#
#     # color associations
#     CONFIG = {
#         "r": COLOR_MAP["RED_D"],
#         "g": COLOR_MAP["GREEN_D"],
#         "b": COLOR_MAP["BLUE_D"]
#         }

    # def construct(self):
    #
    #     triangle = Polygon(np.array([0,0,0]), 4*RIGHT, 3*UP)
    #     triangle.scale(0.5, about_point=ORIGIN).get_fill_opacity()
    #     triangle.move_to(4*LEFT)
    #     self.play(Write(triangle))
    #
    #     a = TextMobject("a").set_color(self.g)
    #     b = TextMobject("b").set_color(self.b)
    #     c = TextMobject("c").set_color(self.r)
    #     a.next_to(triangle, LEFT ,buff=0.3)
    #     b.next_to(triangle, DOWN,buff=0.3)
    #     c.move_to(triangle.get_center()+0.3*(UP+RIGHT))
    #     self.play(Write(a),
    #               Write(b),
    #               Write(c))
        
        # pythagoras formula

        # formula = TexMobject(r"\{a^2}+{b^2}")


class Pythagoras(Scene):

    # color associations
    # CONFIG = {
    #     "r": COLOR_MAP["RED_D"],
    #     "g": COLOR_MAP["GREEN_D"],
    #     "b": COLOR_MAP["BLUE_D"]
    # }

    def construct(self):

        # creating grid
        grid = ImageMobject('MyManimAnimations/tools/grid.png').scale(0.75)
        self.add(grid)

        # making right triangle
        triangle = Polygon(np.array([0, 0, 0]), 4 * RIGHT, 3 * UP)
        triangle.scale(0.5, about_point=ORIGIN).get_fill_opacity()
        triangle.shift(4 * LEFT)
        self.play(Write(triangle))

        a = TextMobject("a")
        b = TextMobject("b")
        c = TextMobject("c")
        a.next_to(triangle, LEFT, buff=0.3)
        b.next_to(triangle, DOWN, buff=0.3)
        c.move_to(triangle.get_center() + 0.3 * (UP + RIGHT))
        self.play(Write(a),
                  Write(b),
                  Write(c))

        # making right triangle with squares
        triangle = Polygon(np.array([0,0,0]), 4*RIGHT, 3*UP)
        triangle.scale(0.5, about_point=ORIGIN)
        self.play(Write(triangle))
        
        # adding text
        a = TextMobject("a")
        b = TextMobject("b")
        c = TextMobject("c")
        a.next_to(triangle, LEFT ,buff=0.3)
        b.next_to(triangle, DOWN,buff=0.3)
        c.move_to(triangle.get_center()+0.3*(UP+RIGHT))
        self.play(Write(a),
                  Write(b),
                  Write(c))
        
        # making squares
        s1 = Square(side_length=3).scale(0.5, about_point=ORIGIN).next_to(triangle,LEFT, buff=0)
        s2 = Square(side_length=4).scale(0.5, about_point=ORIGIN).next_to(triangle, DOWN, buff=0)
        s3 = Square(side_length=5).scale(0.5, about_point=ORIGIN) \
            .next_to(triangle, UP, buff=0, aligned_edge=LEFT). \
            rotate(-np.arctan(3/4), about_point=triangle.get_critical_point(LEFT+UP))

        self.play(
            Write(s1),
            Write(s2),
            Write(s3)
        )

        # show_critical_points_2D(self, s3)
        # show_critical_coords_2D(self, s3)
        # show_half_length_2D(self, s3)

        self.wait()

