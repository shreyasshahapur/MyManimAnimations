from manimlib.imports import *
import numpy

class rightTriangle(Scene):
    #color associations
    CONFIG = {
        "r":COLOR_MAP["RED_D"],
        "g":COLOR_MAP["GREEN_D"],
        "b":COLOR_MAP["BLUE_D"]
        }
    def construct(self):
        

        triangle = triangle = Polygon(np.array([0,0,0]), 4*RIGHT, 3*UP)
        triangle.scale(0.5, about_point=ORIGIN)
        triangle.move_to(4*LEFT)
        self.play(Write(triangle))

        a = TextMobject("a").set_color(self.g)
        b = TextMobject("b").set_color(self.b)
        c = TextMobject("c").set_color(self.r)
        a.next_to(triangle, LEFT ,buff=0.3)
        b.next_to(triangle, DOWN,buff=0.3)
        c.move_to(triangle.get_center()+0.3*(UP+RIGHT))
        self.play(Write(a),
                  Write(b),
                  Write(c))
        
        #pythagoras formula

        formula =  TexMobject(r"\{a^2}+{b^2}")


class pythagoras(Scene):
    #color associations
    CONFIG = {
        "r":COLOR_MAP["RED_D"],
        "g":COLOR_MAP["GREEN_D"],
        "b":COLOR_MAP["BLUE_D"]
    }

    def construct(self):
        
        #making right triangle
        triangle = Polygon(np.array([0,0,0]), 4*RIGHT, 3*UP)
        triangle.scale(0.5, about_point=ORIGIN)
        self.play(Write(triangle))
        
        #adding text
        a = TextMobject("a").set_color(self.g)
        b = TextMobject("b").set_color(self.b)
        c = TextMobject("c").set_color(self.r)
        a.next_to(triangle, LEFT ,buff=0.3)
        b.next_to(triangle, DOWN,buff=0.3)
        c.move_to(triangle.get_center()+0.3*(UP+RIGHT))
        self.play(Write(a),
                  Write(b),
                  Write(c))
        
        #making squares

        s1 = Square(side_length=3).scale(0.5, about_point=ORIGIN).next_to(triangle,LEFT, buff=0).set_color(self.g)
        s2 = Square(side_length=4).scale(0.5, about_point=ORIGIN).next_to(triangle, DOWN, buff=0).set_color(self.b)
        s3 = Square(side_length=5).scale(0.5, about_point=ORIGIN) \
            .next_to(triangle, UP, buff=0, aligned_edge=LEFT). \
            rotate(-np.arctan(3/4), about_point=triangle.get_critical_point(LEFT+UP)).set_color(self.r)

        self.play(
            Write(s1),
            Write(s2),
            Write(s3)
        )



        # square1 = Square(side_length=5)
        # square1.set_color(self.r)
        # square1.move_to(5.5*UP+2.5*RIGHT)
        # #square1.move_to((square1.get_width()/2)*UP, ((square1.get_height()/2)+ triangle.get_top())*LEFT)
        # square1.rotate(-np.arctan(3/4), about_point=np.array([0,3,0]))
        # square1.scale(0.5, about_point=ORIGIN)
        #
        # self.play(Write(square1))
        #
        # square2 = Square(side_length=4)
        # square2.set_color(self.b)
        # square2.move_to(np.array([1,-1,0])).scale(0.5)
        # self.play(Write(square2))
        #
        # square3 = Square(side_length=3)
        # square3.set_color(self.g)
        # square3.move_to(np.array([-0.75,0.75,0])).scale(0.5)
        # self.play(Write(square3))

    
        self.wait()

