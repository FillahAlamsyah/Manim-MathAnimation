from manim import *
from manim_rubikscube import *
from random import *

class Rubiks(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#0E1B24"
        # I use 2 dimensional rubikscube
        # set offset -> 0 , so it looks like 1 dimensional rubikscube
        cube = RubiksCube(dim=2,x_offset=0.000000000000001, y_offset=0.000000000000001, z_offset=0.000000000000001).scale(0.75)
        cube.move_to(ORIGIN)

        self.move_camera(phi=50*DEGREES, theta=0*DEGREES)
        self.renderer.camera.frame_center = cube.get_center()

        self.play(
            FadeIn(cube)
        )
        angle = ['theta','gamma','phi']
        for a in range(20) :
            a = choice(angle)
            self.begin_ambient_camera_rotation(rate=1,about=a)
            self.play(Rotating(cube, radians=2*PI, run_time=1))
            self.wait(1)
