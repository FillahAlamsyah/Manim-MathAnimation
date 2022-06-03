#from manim import*
from manimlib import*
CONFIG = {
    "camera_class": ThreeDCamera,
}

class SurfaceExample(Scene):
    def construct(self):
        # Set perspective

        '''
https://translate.google.com/translate?hl=id&sl=auto&tl=id&u=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F398605290&prev=search
https://zhuanlan.zhihu.com/p/398605290
'''
        #day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg"
        #night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"
        day_texture = ".\Whole_world_-_land_and_oceans.jpg "
        
        #Bidang/Surface
        '''
Kelas Surface adalah kelas turunan dari Mobject,
yang secara langsung menghasilkan permukaan persegi
tiga dimensi dengan parameter berikut:

parameter	menjelaskan
u_range	tuple, kisaran arah sumbu u, defaultnya adalah (0,1)
v_range	tuple, rentang sumbu v, defaultnya adalah (0,1)
resolution	tuple, resolusi patch, defaultnya adalah (101.101)
color	str, warna tambalannya, defaultnya adalah ABU-ABU
opacity	float, transparansi patch, defaultnya adalah 1.0
gloss	float, reflektifitas patch, defaultnya adalah 0,3
shadow	float, bayangan tambalan, defaultnya adalah 0,4
epsilon	float, nomor yang digunakan untuk menghasilkan elemen mikro dari tambalan, standarnya adalah 1e-5
Jangan lakukan apa pun untuk menghasilkan tambalan:
'''
        #Permukaan = Surface()
        
        #Bidang dengan Parameter
        '''
Mari kita coba parameter yang diberikan di atas:
(Saya tidak tertarik dengan reflektifitas dan bayangan,
dan perbedaannya tidak besar)
'''
        Permukaan1 = Surface(
            u_range=(-2, 2),
            v_range=(-2, 2),
            resolution=(100, 100),
            color=BLUE,
            opacity=0.8,
            gloss=0.3,
            shadow=0.4,
            epsilon=1
        )
        
        #Fungsi Parametrik
        '''
ParametrikPermukaan
Kelas ini merupakan kelas turunan dari Surface.
Sesuai dengan namanya,
perannya adalah untuk menghasilkan permukaan parametrik
tiga dimensi.
Oleh karena itu, dibandingkan dengan Surface,
ParametricSurface juga perlu melewati pemetaan (objek fungsi)
untuk menggambarkan persamaan parametrik dari permukaan
yang akan dibangun
Perhatikan bahwa pemetaan ini harus berupa pemetaan
dari larik dua dimensi ke larik tiga dimensi.

Dengan asumsi bahwa
ketiga sumbu koordinat sistem koordinat tiga dimensi
yang kita gunakan adalah x, y, z,
maka pemetaan ini perlu dilalui dalam x dan y,
dan outputnya adalah
persamaan parametrik
u(x,y),v(x,y),w(x,y)

Kemudian ketika permukaan dibuat,
sekelompok pasangan titik (x, y)
akan diperoleh sesuai dengan
produk luar u_range dan v_range.
Pasangan titik ini kemudian dilemparkan
ke dalam pemetaan yang baru saja dilewati,
dan sekelompok tiga dimensi pasangan titik dapat diperoleh.
, Kemudian diperoleh urutan titik pengambilan sampel
yang menggambarkan benda tiga dimensi.
Selanjutnya langsung berdasarkan algoritme
interpolasi yang relevan dan algoritme rendering
yang disajikan di layar Anda.

Mari kita berikan beberapa contoh:

Contoh1:
Dalam domain yang D=(-1,1)x(-1,1)
ditunjukkan pada fungsi f(x,y) = x^2 + y^2
Pertama, kita harus mengubah fungsi ini menjadi
persamaan parametrik,
karena parameternya adalah dua dimensi domain,
yaitu x dan y,
persamaan parametriknya
x = x
y = y
z = x^2 +y^2
jadi kita perlu menulis fungsi pemetaan sebagai:
'''

        #Contoh Paraboloid
        def ParametricSurface_map(x, y):
            return [
                x,
                y,
                x * x + y * y
            ]
        #Ekspresi Lambda
        f = lambda x, y : [x, y, x * x, y * y]
        #Contoh Langsung
        paraboloid = ParametricSurface(
            uv_func=lambda u, v : [u, v, u * u + v * v],
            u_range=(-1, 1),
            v_range=(-1, 1)
        )
        
        #Contoh Ellipsoid
        '''
persamaan parameter ellipsoid standar:
x = a sin \theta cos \phi
y = b sin \theta sin \phi
z = c cos \theta
dengan \theta = 0,\PI dan \Phi = 0,2\PI
'''

        a, b, c = (1.5, 1, 1)
        EllipsoidSimple = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI),
            v_range=(0, 2 * PI)
        )
        
        #SGRoup
        '''
Meskipun kita belum berbicara tentang VGroup,
kami telah menyebutkan sedikit sebelumnya,
sehingga Anda dapat dengan mudah mengetahui satu hal:
fungsi VGroup adalah untuk mengikat sekelompok objek VMobject
bersama-sama.
Jadi Anda bisa menebak apa itu SGroup.
Dia hanya mengikat sekelompok Permukaan menjadi satu.
Kelas ini akan digunakan untuk konstruksi banyak bentuk
tiga dimensi lain yang umum digunakan di masa depan,
jadi saya tidak akan mengulanginya di sini.

Parameternya adalah sejumlah Permukaan.
'''
        #TexturedSurface
        '''
Permukaan Bertekstur
TexturedSurface adalah kelas turunan dari Surface.
Setelah Anda mendengar namanya,
Anda akan tahu untuk apa itu digunakan.
Jika Anda membuat objek Surface,
maka Anda dapat menempelkan gambar ke Surface Anda
melalui kelas ini.
Coba sekarang! TexturedSurface memiliki dua parameter:
uv_surface	Permukaan, objek permukaan tiga dimensi
gambar_file	str, jalur gambar tekstur
'''
        a, b, c = (2, 2, 1)
        ellipsoidal = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI / 2),
            v_range=(0, 2 * PI)
        )

        texture_surface = TexturedSurface(
            uv_surface=ellipsoidal,
            image_file= day_texture
        )
        #self.add(texture_surface)

        #SurfaceMesh
        '''
PermukaanMesh
Seperti namanya,
SurfaceMesh adalah untuk menyatukan permukaantiga dimensi,
yang juga sangat sederhana untuk diterapkan,
hanya perlu membagi mesh sesuai dengan
sistem koordinat parameter.
Hanya ada satu parameter yang diperlukan untuk SurfaceMesh,
yang mewakili objek permukaan tiga dimensi
yang Anda perlukan untuk di-mesh.
Mari kita ambil permukaan ellipsoidal
sekarang sebagai contoh
'''
        a, b, c = (2, 2, 1)
        ellipsoidal1 = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI / 2),
            v_range=(0, 2 * PI)
        )

        mesh = SurfaceMesh(
            uv_surface=ellipsoidal1
        )
        
        #self.add(mesh)
        #Objects = [Permukaan,Permukaan1,paraboloid,
                   #EllipsoidSimple,ellipsoidal,
                   #]
        #Bola
        '''
Sphere adalah kelas turunan dari Surface,
yang digunakan untuk menghasilkan bola,
dan metode implementasinya persis sama dengan contoh kita
sebelumnya.
Persamaan parametrik dalam kode sumber adalah:
x = r cos u sin v
y = r sin u sin v
z = -r cos v
radius	Jari-jari bola, standarnya adalah 1
u_range	tuple, rentang nilai u, defaultnya adalah [0,2π]
v_range	tuple, rentang nilai v, defaultnya adalah [0,π]
'''
        Bola = Sphere(
            radius=1.25,
            #color=PINK
        )

        #self.add(sphere)

        #Donat
        '''
Torus digunakan untuk menghasilkan permukaan toroidal,
meskipun saya lebih suka menyebutnya bentuk donat,
persamaan parametrik dalam kode sumber adalah:
x = (r1-r2 cos v) cos u
y = (r1-r2 cos v) sin u
z = - sin u
Parameter opsional adalah:

parameter	menjelaskan
u_range	tuple, rentang nilai u, defaultnya adalah [0,2π]
v_range	tuple, rentang nilai v, defaultnya adalah [0,2π]
r1	Jari-jari lingkaran luar, standarnya adalah 3
r2	Jari-jari lingkaran dalam, defaultnya adalah 1
contoh:
'''
        Donat = Torus(r1=1, r2=0.5)
        
        #self.add(torus)


        #Silinder/Tabung
        '''
Silinder adalah kelas turunan dari Permukaan,
digunakan untuk menghasilkan permukaan silinder.
Persamaan parametrik dalam kode sumber adalah:
x = cos u
y = sin u
z = v
Parameter opsional:

parameter	menjelaskan
height	Ketinggian permukaan silinder, standarnya adalah 2
radius	Jari-jari bagian bawah permukaan silinder, standarnya adalah 1
axis	Arah sumbu permukaan silinder. Standarnya adalah np.array([0,0,1])
u_range	tuple, rentang nilai u, defaultnya adalah [0,2π]
v_range	tuple, rentang nilai v, defaultnya adalah [-1,1]
contoh:
'''
        Tabung = Cylinder(
            height=2,
            radius=1
        )
        
        #self.add(cylinder)

        #Garis3D
        '''
Garis3D
Line3D adalah turunan dari kelas Cylinder.
Dapat dilihat dari kode sumber bahwa,
selain mengubah ukuran resolusi,
Line3D adalah permukaan silinder yang sangat sempit,
dan parameternya adalah sebagai berikut:
parameter	menjelaskan
start	Objek ndarray tiga dimensi, parameter yang diperlukan, mewakili titik awal segmen garis
end	Objek ndarray tiga dimensi, parameter yang diperlukan, mewakili titik akhir segmen garis
width	float, digunakan untuk menggambarkan ketebalan segmen garis, standarnya adalah 0,05
contoh:
'''
        Garis3D = Line3D(
            start=np.array([0, 0, 0]),
            end=np.array([3, 3, 3])
        )
        #start_tex = TexText("起点:$(0,0,0)$")
        #end_tex = TexText("终点$(3,3,3)$")
        #start_tex.next_to(np.array([0,0,0]))
        #end_tex.next_to(np.array([3,3,3]))
        #self.add(line, start_tex, end_tex)

        #Disk3D
        #Disk/Cakram/Piringan
        '''
Disk3D
Disk3D adalah kelas turunan dari Surface.
Digunakan untuk menghasilkan patch melingkar.
Persamaan parameternya adalah:

x = u cos v
y = u sin v
z = 0

Parameter opsional adalah:

parameter	menjelaskan
radius	Jari-jari lingkaran
u_range	tuple, rentang nilai u, defaultnya adalah [0,1]
v_range	tuple, rentang nilai v, defaultnya adalah [0,2π]
Contohnya adalah sebagai berikut:
'''
        Cakram = Disk3D(
            radius=1
        )

        #self.add(disk)
        '''
Tentu saja, kecuali menggunakan persamaan parametrik di atas,
dalam tiga dimensi,
parameter berikut dapat digunakan untuk menghasilkan
persamaan potongan bulat,
pendekatannya sangat sederhana,
sehingga persamaan ellipsoidal yang
dihasilkan di atas kita
a = b, c = 0
pada baris.
Contohnya adalah sebagai berikut:
'''
        a, b, c = (1, 1, 0)
        Cakram1 = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI / 2),
            v_range=(0, 2 * PI)
        )

        #self.add(disk)
        '''
Hasilnya hampir sama persis.
Bahkan, kita bisa melihat perbedaan antara kedua metode ini
melalui SurfaceMesh:
'''
        Kaset = Disk3D(radius=1)

        a, b, c = (1, 1, 0)
        my_disk = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI / 2),
            v_range=(0, 2 * PI)
        )

        kaset = SurfaceMesh(Kaset, color=BLUE_B)
        #my_disk = SurfaceMesh(my_disk, color=BLUE_B)

        #caption1 = Tex(r"\begin{cases}x=u\cos v\\y=u\sin v\\z=0\end{cases}")
        #caption2 = Tex(r"\begin{cases}x=\sin u \cos v\\y=\sin u\sin v\\z=0\end{cases}")
        
        #kaset.next_to(my_disk)
        #caption1.next_to(kaset, direction=OUT * 2)
        #caption2.next_to(my_disk, direction=OUT * 2)

        #self.add(disk, my_disk, caption1, caption2)
        '''
Dan, bagaimana saya bisa mengatakannya,
yang pertama memiliki keuntungan,
yaitu, biarkan saja, apa gunanya?
Anda akan tahu setelah membaca kode di bawah ini.
Gambar album yang saya gambar tangan adalah sebagai berikut:
'''

        a, b, c = (2, 2, 0)
        kaset1 = ParametricSurface(
            uv_func=lambda u, v : [
                a * np.sin(u) * np.cos(v),
                b * np.sin(u) * np.sin(v),
                c * np.cos(u)
            ],
            u_range=(0, PI / 2),
            v_range=(0, 2 * PI)
        )

        Cakram = TexturedSurface(
            uv_surface=kaset1,
            image_file= day_texture
        )

        #self.play(ShowCreation(Cakram), run_time=3)
        #self.wait()

        #Kotak3D
        '''
Kotak3D
Square3D adalah kelas turunan dari Surface.
Digunakan untuk menghasilkan patch persegi.
Parameter opsional tambahan hanya satu side_length,
yang mewakili panjang sisi.
Contohnya adalah sebagai berikut:
'''
        
        Kotak3D = Square3D(
            side_length=4,
            color=BLUE
        )

        #Kubus
        '''
Cube adalah kelas turunan dari SGroup,
digunakan untuk menghasilkan sebuah kubus,
implementasi internal adalah
untuk menghasilkan enam Square3D yang persis sama,
kemudian menyesuaikan arah dan posisi,
dan kemudian membuang semuanya ke dalam wadah SGroup.
Parameter opsional utama adalah:

parameter	menjelaskan
color	Warna, defaultnya adalah BIRU
opacity	Transparansi, defaultnya adalah 1
gloss	Reflektansi, standarnya adalah 0,5
side_length	Panjang sisi, defaultnya adalah 2
Contoh:
(Saya pikir skema warna default sangat indah)
'''
        Kubus = Cube(side_length=4)

        #Prisma/Balok
        '''
Kubus Prisma adalah kelas turunan,
meskipun namanya adalah prisma,
tetapi pada kenyataannya,
dapat menghasilkan menyesuaikan panjang dan lebar dari balok
( Cuboid ),
parameter opsional adalah daftar dimensi,
atas nama panjang dan lebar,
contohnya adalah sebagai berikut:
'''
        Balok = Prism(
            dimensions=[5,4,3]
        )
        frame = self.camera.frame
        frame.set_euler_angles(
            #theta=30 * DEGREES,
            phi=70 * DEGREES,
        )
                
        
        Objects = [Bola.shift(5*LEFT),
                   #Permukaan1,
                   #paraboloid,
                   #EllipsoidSimple,
                   ellipsoidal.shift(1.625*LEFT),
                   Donat.shift(2*RIGHT),
                   Tabung.shift(5*RIGHT),#Garis3D,
                   #Cakram,
                   #Kaset,
                   #Kotak3D,
                   #Kubus,
                   #Balok
                   ]
        #or Perm in Objects:
            #for i in range(len(Objects)):
        A1= TexturedSurface(uv_surface= Bola ,image_file= day_texture)
        A2 = TexturedSurface(uv_surface= ellipsoidal ,image_file= day_texture)
        A3 = TexturedSurface(uv_surface= Donat ,image_file= day_texture)
        A4 = TexturedSurface(uv_surface= Tabung ,image_file= day_texture)
            
        B = Text("Aneka Varian Bumi ",font="consolas",color=BLUE)#.scale(0.75)
        B.to_edge(UP).fix_in_frame( )
        #self.wait()

        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))
        
        self.add(B)
        self.play(ShowCreation(SGroup(A1,A2,A3,A4)),run_time=5)
        self.play(#frame.animate.increment_phi(-10 * DEGREES),
            frame.animate.increment_theta(-20 * DEGREES),
            run_time=25
            )
        #self.wait()
        #self.play(Uncreate(A),Uncreate(B))
        #self.wait()
                #print(i)
            
                
