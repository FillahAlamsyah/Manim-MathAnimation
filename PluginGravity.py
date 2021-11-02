from manim import *
from manim_physics import *

code = '''from manim import *
from manim_physics import *
#Install manim plugin at command line with pip install manim_physics
# Check this plugin at https://pypi.org/project/manim-physics/
# Or check at description
class TwoObjectsFalling(SpaceScene):
    def construct(self):
        text = Text("Gravity On",
                   font="Hanging Letters")
        for letter in text:
            letter.set_color(random_bright_color()) #Setting Color  
        text.scale(2)
        text.to_edge(UP)
        print(text)
        print(len(text))
        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2).set_color(TEAL)
        self.add(walls)

        self.play(DrawBorderThenFill(text)) # Mobjects will move with gravity
        self.make_rigid_body(text[0:10])
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(8)
'''
"Rigid Mechanics"
# use a SpaceScene to utilize all specific rigid-mechanics methods
class TwoObjectsFalling(SpaceScene):
    def construct(self):
        title = VGroup(Text("Manim Plugin - Manim_Physics"),
                       Text("Gravity")).arrange(DOWN)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait()
        self.play(Uncreate(title))
        self.wait()
        
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)
        
        text = Text("Gravity On",
                   font="Hanging Letters")
        for letter in text:
            letter.set_color(random_bright_color())
        text.scale(2)
        text.to_edge(UP)
        print(text)
        print(len(text))
        ground = Line([-4, -3.5, 0], [4, -3.5, 0])
        wall1 = Line([-4, -3.5, 0], [-4, 3.5, 0])
        wall2 = Line([4, -3.5, 0], [4, 3.5, 0])
        walls = VGroup(ground, wall1, wall2).set_color(TEAL)
        self.add(walls)
        listing = Code(
                code=code,
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                insert_line_no=True,
                style=Code.styles_list[17],
                background="window",
                language="python",
                ).scale(0.6)
        #self.play(
        #    DrawBorderThenFill(circle),
        #    DrawBorderThenFill(rect),
        #)
        self.play(DrawBorderThenFill(text))
        #self.make_rigid_body(rect, circle)  # Mobjects will move with gravity
        self.make_rigid_body(text[0:10])
        #for i in len(text):
        #    self.make_rigid_body(text[i])
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(9)
        C = Square(fill_color=BLACK).scale(10)
        self.play(Write(C))
        self.play(FadeIn(listing))
        self.wait(2)
        self.play(FadeOut(listing))
        A = Text("Thanks For Watching").scale(1.5)
        self.play(GrowFromCenter(A))
        self.wait()
        self.play(FadeOut(A))
        # during wait time, the circle and rect would move according to the simulate updater
