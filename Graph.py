from manim import*
import numpy as np

class Butterfly(Scene):
    def construct(self):

        #Judul
        J = Title("Butterfly Graph")

        self.play(Write(J))
        self.wait()
        self.play(FadeOut(J))
        
        # Persamaan
        P = Text("Persamaan Polar")
        P.to_edge(UP)
        PP = MathTex(r"r = e^{\sin \theta} - 2 \cos(4\theta)+ \sin^5 \left[ \dfrac{1}{24}\left(2\theta-\pi\right) \right]")
        PP.next_to(P,DOWN)

        PR = Text("Persamaan Parametrik")
        PR.next_to(PP,DOWN)

        PRX = MathTex(r"x = \sin t \left[e^{\cos t}-2\cos \left( 4t \right) + \sin^5 \left(\dfrac{1}{12}t\right) \right]")
        PRY = MathTex(r"y = \cos t \left[e^{\cos t}-2\cos \left( 4t \right) + \sin^5 \left(\dfrac{1}{12}t\right) \right]")
        
        PRX.next_to(PR,DOWN)
        PRY.next_to(PRX,DOWN)

        self.play(Write(P))
        self.play(Write(PP))
        self.play(Write(PR))
        self.play(Write(PRX),Write(PRY))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

        #Plot Grafik
        "Range = [0,24*PI]" #Mengatur Range Grafik
        
        #def func(self, t):
            #return np.array((np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4t)+np.sin((1/12)*t)**5)), np.array((np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4t)+np.sin((1/12)*t)**5))), 0)
        
        #func = ParametricFunction(self.func, t_range = np.array([0, 24*PI]), fill_opacity=0).set_color(RED)
        #self.play(Create(func))
        # self.wait()

        plane = PolarPlane(radius_max=24*PI)
        r = lambda t : np.exp(np.sin(t))-2*np.cos(4*t)+np.sin((1/24)*(2*t-PI))**5
        graph = plane.plot(r,[0,24*PI],color=GREEN)
        VGroup(plane,graph).scale(0.1)
        self.play(Create(plane))
        self.play(Create(graph))
        self.wait(5)
        self.play(Uncreate(graph),Uncreate(plane))

        #Outro
        O = Text("Thanks For Watching")
        O.scale(2)
        self.play(FadeIn(O))
        self.wait()
        self.play(FadeOut(O))
        
       

        







        
