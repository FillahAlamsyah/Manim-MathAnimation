#from manimlib.imports import *
from manim import*
class Outro(Scene):
    def construct(self):
        A = Text("Thanks For Watching")
        A.set_color_by_gradient(BLUE,GREEN).scale(1.5)
        self.play(Create(A))
        self.wait()
        self.play(FadeOut(A))
        self.wait()
            
class c(Scene):
    def construct(self):
        #Objek Teks yang akan ditampilkan
        #Text 1
        #Text tersusun atas huruf-huruf yang digabung dalam Class VGroup
        a1=VGroup(Text("F"),    #Huruf pertama
                  Text("I"),    #Huruf Kedua
                  Text("L"),    #Huruf Ketiga
                  Text("L"),    #Huruf Keempat
                  Text("A"),    #Huruf Kelima
                  Text("H")     #Huruf Keenam
                  )
        a1.scale(4).shift(4*UP)   #Mengatur Posisi Text
        a1.arrange(RIGHT) 
        #Text kedua yang tersusun atas beberapa simbol \LaTeX 
        a2=Tex("$\\vec{F}$",
               "$\\sqrt{-1}$",
               "$\\lambda^2$",
               "$\\alpha$",
               "$\\eta$")
        #Pada bagian ini mengatur warna dari Teks Pertama
        a1[1].set_color(PURPLE) #angka di dalam [ ] menunjukkan posisi di variabel a1
        a1[2].set_color(RED)    #dst
        a1[3].set_color(GREEN)
        a1[0].set_color(BLUE)
        a1[4].set_color(BLUE)
        a1[5].set_color(RED)

        #Begitu pula bagian ini
        a2[0].set_color(BLUE)
        a2[1].set_color(RED)
        a2[2].set_color(GREEN)
        a2[3].set_color(PURPLE)
        a2[4].set_color(GREY)
        
        a2.next_to(a1,2*DOWN).scale(2) #Mengatur Posisi a2 terhadap a1
        
        #Membuat animasi
        self.play(Write(a1)) #Animasi Pertama
        #Animasi Kedua
        self.wait(1)
        #Animasi Ketiga
        self.play(TransformFromCopy(a1,a2))
##                  TransformFromCopy(a1[1],a2[1]),
##                  TransformFromCopy(a1[2:3],a2[2]),
##                  TransformFromCopy(a1[4],a2[3]))
        #Animasi Keempat
        self.wait(1)
        #Animasi Kelima
        self.play(FadeOut(a1),ApplyMethod(a2.move_to,ORIGIN))
        #Animasi Keenam
        self.wait(1)
        #Animasi Ketujuh
        self.play(ApplyMethod(a2.scale,1.5))
        #Animasi Kedelapan
        self.wait(1)
        #Animasi Kesembilan
        self.play(FadeOut(a2))
