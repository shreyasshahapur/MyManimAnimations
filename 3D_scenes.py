from manim import *

class Test_3D(SpecialThreeDScene):

    def construct(self):
        # Adding Axes
        axes = ThreeDAxes()
        # Adding Sphere
        sphere = self.get_sphere()

        self.play(
            ShowCreation(sphere),
            ShowCreation(axes),
            run_time=2
        )

        self.set_camera_orientation(gamma=60*DEGREES)
        self.move_camera(theta=60*DEGREES)
