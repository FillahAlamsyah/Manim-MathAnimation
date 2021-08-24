from manim import*



class CodeMobject(Scene):
    def construct(self):
        #Intro
        I = Title("Code Mobject").move_to(ORIGIN).set_color(BLUE)
        
        I1 = Text('''Code Mobject adalah salah satu Mobject atau Preset yang dapat menampilkan kode
dari berbagai bahasa pemrograman dengan highlight sesuai dengan style yang tersedia.''').scale(0.5)
        I2 = Text ("Berikut adalah 18 Style yang telah tersedia.").scale(0.5)
        
        self.play(Write(I))
        self.wait()
        self.play(Uncreate(I))
        self.play(Write(I1))
        self.wait()
        self.play(Uncreate(I1))
        self.play(Write(I2))
        self.wait()
        self.play(Uncreate(I2))
        self.wait()
        #CodeMobject
        code = '''from manim import*
class CodeFromString(Scene):
    def construct(self):
        code = \''' Tulis Kode di sini
\'''
        rendered_code = Code(code=code, tab_width=4, background="window",
                            language="Python", font="Monospace")
        self.play(Write(rendered_code))
        self.wait()
        self.play(Uncreate(rendered_code))
'''
        #rendered_code = Code(code=code, tab_width=4, background="window",
        #                    language="Python", font="Monospace")
        #self.play(Write(rendered_code))
        #self.wait()
        #self.play(Uncreate(rendered_code))
        code_styles_list = {0: "autumn", 1: "borland", 2: "bw", 3: "colorful",
                    4: "default", 5: "emacs", 6: "friendly", 7: "fruity",
                    8: "manni", 9: "monokai", 10: "murphy", 11: "native",
                    12: "pastie", 13: "perldoc", 14: "rrt", 15: "tango",
                    16: "trac", 17: "vim", 18: "vs"}
        for number,styles in code_styles_list.items():
            listing = Code(
                code=code,
                tab_width=4,
                background_stroke_width=1,
                background_stroke_color=WHITE,
                insert_line_no=True,
                style=Code.styles_list[number],
                background="window",
                language="python",
                )
            listing.scale(0.8)
            Title1=Text(f"This is code_style {number} name : {styles}",font="consolas",color=BLUE).next_to(listing,1.5*UP)
            ccc=VGroup(Title1,listing)
            D=VGroup()
            D.add(ccc).arrange_in_grid()
            
            self.play(Write(ccc))
            self.wait()
            self.play(FadeOut(ccc))
            self.wait()

        Z = Text("Thanks For Watching").set_color_by_gradient(GREEN,YELLOW)
        self.play(Write(Z))
        self.wait()
        self.play(Uncreate(Z))
        self.wait()
