from manim import*
class Count(Scene):
    def construct(self):
        code = '''from manim import*
config.background_color = WHITE
class Count(Scene):
    def construct(self):
        number = Text("10").set_color(BLACK).scale(4)
        self.play(Write(number))
        for i in range(9,-2,-1):
            if i != -1 :
                self.play(Transform(number,
                Text(str(i)).set_color(BLACK).scale(4)),run_time=1)
                self.wait()
            elif i == -1 :
                self.play(Transform(number,
                Text(str(i)).set_color(WHITE).scale(4)),run_time=0.05)
        self.wait()
'''
        Title = Text("Countdown").set_color(BLACK).scale(2)
        self.play(DrawBorderThenFill(Title))
        self.wait()
        self.play(Uncreate(Title))
        number = Text("10").set_color(BLACK).scale(4)
        self.play(Write(number))
        #self.add_sound("click.wav")
        self.wait()
        for i in range(9,-2,-1):
            if i != -1 :
                self.play(Transform(number,
                                    Text(str(i)).set_color(BLACK).scale(4)),run_time=1)
                #self.add_sound("click.wav")
                self.wait()
            elif i == -1 :
                self.play(Transform(number,
                                    Text(str(i)).set_color(WHITE).scale(4)),run_time=0.001)
        self.wait(0.5)
        codes = Code(
            code=code,
            tab_width=4,
            background_stroke_width=1,
            background_stroke_color=WHITE,
            insert_line_no=True,
            style=Code.styles_list[14],
            background="window",
            language="python",
            ).scale(0.8)
        self.play(Write(codes))
        self.wait(3)
        self.play(FadeOut(codes))
        A = Text("Thanks For Watching").scale(1.5).set_color(BLACK)
        self.play(GrowFromCenter(A))
        self.wait()
        self.play(FadeOut(A))
