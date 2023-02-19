import tkinter as tk
from   tkinter import *
from   tkinter import ttk
from   PIL import Image, ImageTk
from   subcode.Zavity import *
from   subcode.srouby_a_matice import *
from   subcode.Normy import *
from   subcode.pera import *
from   subcode.kv import *
from   subcode.cepy import *
from   subcode.nosniky import *

def mainMenu():
    cls()
    print("Main.py mainMenu")
    root.title("Interaktivní strojnické tabulky")
    root.minsize(1000,800)
    lbl =  ttk.Label (root, text="Interaktivní strojnické tabulky", padding=2).grid(column=0, row=0)
    btn =  ttk.Button(root, text="Zavřít", command=root.destroy, width=30).grid(column=0, row=10)
    btn2 = ttk.Button(root, text="Závity", command=zavity, width=30).grid(column=0, row=1)
    btn3 = ttk.Button(root, text="Vyhledávač norem", command=normy, width=30).grid(column=0, row=2)
    btn4 = ttk.Button(root, text="Šrouby a matice", command=srouby_a_matice, width=30).grid(column=0, row=3)
    btn5 = ttk.Button(root, text="Přiřazení pera k hřídeli", command=pera, width=30).grid(column=0, row=4)
    btn6 = ttk.Button(root, text="Přiřazení závlačky k čepu", command=cepy, width=30).grid(column=0, row=5)
    btn7 = ttk.Button(root, text="Výpočet kvadratických průřezů", command=kv, width=30).grid(column=0, row=6)
    btn8 = ttk.Button(root, text="Výpočet nosníků", command=nosniky, width=30).grid(column=0, row=7)
    btn9 = ttk.Button(root, text="Historie výstupů", command=outputFile, width=30).grid(column=0, row=8)
    print("all windows:", root.winfo_children())


def cls():
    print("Main.py cls")
    for frame in root.winfo_children():
        frame.destroy()

def export(ex):
    print("Main.py export")
    with open("export.txt", "w") as f:
        f.write(f"{ex}\n")


def zavity():
    print("Main.py zavity")
    cls()
    lbl = ttk.Label(text="Zavity").grid(column=1, row=0)
    D = tk.DoubleVar()
    lbl2 = ttk.Label(root, text="D:").grid(column=0, row=1)
    lbl3 = ttk.Label(root, text="P:").grid(column=0, row=2)
    ent = ttk.Entry(root, textvariable=D, width=16).grid(column=1, row=1)
    lbl4 = ttk.Label(text= "M\nd1 = \nd2 = \nd3 = ").place(y= 50, x= 120)
    img = ImageTk.PhotoImage(Image.open(f"imgs/zavity_img.jpg"))
    image = Label(root, image= img)
    image.photo = img
    image.place(x=220, y=50)
    def d_assign():
        zavity()
        print(D.get())
        p_allowed = p_assigment(D.get())
        print(p_allowed)
        if D.get() not in d_list:
            lbl4 = ttk.Label(text= "Neplatný\nprůměr\nzávitu",).place(y= 50, x= 120)
            export("Neplatný\nprůměr\nzávitu")
            pass
        else:
            row = 1
            for p in p_allowed:
                def confirm_z(P = p):
                    print("confirm")
                    export(thread_print(D.get(), P))
                    lbl4 = ttk.Label(text= thread_print(D.get(), P)).place(y= 50, x= 120)
                row = row + 1
                ttk.Button(text=p, command=confirm_z, width=15).grid(column=1, row= row)
    btn2 = ttk.Button(text= "Potvrdit", command=d_assign, width=15).grid(column=2, row=1)
    btn3 = ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=2, row=0)


def normy():
    print("Main.py Vyhledávač norem")
    root.minsize(1000,800)
    cls()
    norm = tk.StringVar()
    lbl = ttk.Label(text="Vyhledávač norem").grid(column=1, row=0)
    lbl2 = ttk.Label(text="Např. 01 0130").grid(column=1, row=1)
    ent = ttk.Entry(root, textvariable=norm, width=30).grid(column=1, row=2)
    lbl3 = Text(root, height=40)
    lbl3.place(y=80, x=0)
    def confirm_n():
        normy()
        print("confirm")
        lbl3 = Text(root, height=40)
        lbl3.place(y=80, x=0)
        lbl3.insert(INSERT, norm_print(find_num(norm.get())))
        export(norm_print(find_num(norm.get())))
    btn = ttk.Button(root, text= "Potvrdit", command= confirm_n, width=15).grid(column=2, row=1)
    btn2 = ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=2, row=0)


def srouby_a_matice():
    print("Main.py srouby a matice")
    cls()
    lbl = ttk.Label(text="Srouby a matice").grid(column=0, row=0)
    def srouby():
        print("Main.py srouby")
        cls()
        lbl = ttk.Label(text="Srouby").grid(column=1, row=0)
        D = tk.DoubleVar()
        lbl2 = ttk.Label(text="M:").grid(column=0, row=1)
        lbl3 = ttk.Label(text="l:").grid(column=0, row=2)
        ent = ttk.Entry(root, textvariable= D).grid(column=1, row=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/Srouby.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=320, y=0)
        img2 = ImageTk.PhotoImage(Image.open(f"imgs/Srouby2.jpg"))
        image2 = Label(root, image= img2)
        image2.photo = img2
        image2.place(x=320, y=170)
        def confirm_s_2():
            srouby()
            print("confirm")
            sroub = sroub_assign(D.get(), "l")
            row = 1
            if sroub != None:
                l_possible = sroub[2]
                for l in l_possible:
                    def confirm_l(L = l):
                        print("confirm")
                        sroub[2] = L
                        lbl4 = ttk.Label(text= f"M {sroub[0]}\nk = {sroub[1]}mm \nl = {sroub[2]}mm \nsmax = {sroub[3]}mm").place(y= 75, x= 140)
                        export(f"M {sroub[0]}\nk = {sroub[1]}mm \nl = {sroub[2]}mm \nsmax = {sroub[3]}mm")
                    row = row + 1
                    ttk.Button(text=l, command=confirm_l, width=15).grid(column=1, row= row)
            else:
                lbl4 = ttk.Label(text= "Neplatný\nprůměr\nšroubu",).place(y= 75, x= 140)
                export("Neplatný\nprůměr\nšroubu")
                pass
        def confirm_s_1():
            srouby()
            print("confirm")
            sroub = sroub_assign(D.get(), "s")
            row = 1
            if sroub != None:
                l_possible = sroub[2]
                for l in l_possible:
                    def confirm_l(L = l):
                        print("confirm")
                        sroub[2] = L
                        lbl4 = ttk.Label(text= f"M {sroub[0]}\nk = {sroub[1]}mm \nl = {sroub[2]}mm \nsmax = {sroub[3]}mm").place(y= 75, x= 140)
                        export(f"M {sroub[0]}\nk = {sroub[1]}mm \nl = {sroub[2]}mm \nsmax = {sroub[3]}mm")
                    row = row + 1
                    ttk.Button(text=l, command=confirm_l, width=15).grid(column=1, row= row)
            else:
                lbl4 = ttk.Label(text= "Neplatný\nprůměr\nšroubu\n ",).place(y= 75, x= 140)
                export("Neplatný\nprůměr\nšroubu")
                pass
        btn = ttk.Button(text= "Potvrdit - kratší závit", command=confirm_s_1, width=25).grid(column=2, row=1)
        btn2 = ttk.Button(text= "Potvrdit - závit až k hlavě", command=confirm_s_2, width=25).grid(column=2, row=2)
        btn3 = ttk.Button(text="Zpět", command=srouby_a_matice, width=25).grid(column=2, row=0)
    def matice():
        print("Main.py matice")
        cls()
        lbl = ttk.Label(text="Matice").grid(column=1, row=0)
        D = tk.DoubleVar()
        lbl2 = ttk.Label(text="M:").grid(column=0, row=1)
        ent = ttk.Entry(root, textvariable= D).grid(column=1, row=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/matice.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=320, y=0)
        img2 = ImageTk.PhotoImage(Image.open(f"imgs/matice2.jpg"))
        image2 = Label(root, image= img2)
        image2.photo = img2
        image2.place(x=320, y=170)
        def confirm_m1():
            matice()
            print("confirm")
            mat = matice_assign(D.get(), 1)
            print(mat)
            row = 1
            if mat != None:
                lbl4 = ttk.Label(text= f"M {mat[0]}\nda = {mat[1]}mm \nmmin = {mat[2]}mm \nmmax = {mat[3]}mm\ns = {mat[4]}\ne = {mat[5]}").place(y= 75, x= 140)
                export(f"M {mat[0]}\nda = {mat[1]}mm \nmmin = {mat[2]}mm \nmmax = {mat[3]}mm\ns = {mat[4]}\ne = {mat[5]}")
            else:
                lbl4 = ttk.Label(text= "Neplatný\nprůměr\nzávitu\n ",).place(y= 75, x= 140)
                export("Neplatný\nprůměr\nzávitu")
                pass
        def confirm_m2():
            matice()
            print("confirm")
            mat = matice_assign(D.get(), 2)
            print(mat)
            row = 1
            if matice != None:
                lbl4 = ttk.Label(text= f"M {mat[0]}\nda = {mat[1]}mm \nmmin = {mat[2]}mm \nmmax = {mat[3]}mm\ns = {mat[4]}\ne = {mat[5]}").place(y= 75, x= 140)
                export(f"M {mat[0]}\nda = {mat[1]}mm \nmmin = {mat[2]}mm \nmmax = {mat[3]}mm\ns = {mat[4]}\ne = {mat[5]}")
            else:
                lbl4 = ttk.Label(text= "Neplatný\nprůměr\nzávitu\n ",).place(y= 75, x= 140)
                export("Neplatný\nprůměr\nzávitu")
                pass
        btn = ttk.Button(text= "Potvrdit - typ 1", command=confirm_m1, width=25).grid(column=2, row=1)
        btn2 = ttk.Button(text= "Potvrdit - matice nízké", command=confirm_m2, width=25).grid(column=2, row=2)

        btn3 = ttk.Button(text="Zpět", command=srouby_a_matice, width=25).grid(column=2, row=0)
    btn = ttk.Button(text="Šrouby", command=srouby, width=25).grid(column=0, row=1)
    btn2 = ttk.Button(text="Matice", command=matice, width=25).grid(column=0, row=2)
    btn3 = ttk.Button(text="Zpět", command=mainMenu, width=25).grid(column=0, row=3)



def pera():
    print("Main.py pera")
    cls()
    lbl = ttk.Label(text="Přiřazení pera k hřídeli").grid(column=0, row=0)
    lbl2 = ttk.Label(text="Průměr hřídele: ").grid(column=0, row=1)
    img = ImageTk.PhotoImage(Image.open(f"imgs/pera_img.jpg"))
    image = Label(root, image= img)
    image.photo = img
    image.grid(column=3, row=3)
    D = tk.DoubleVar()
    ent = ttk.Entry(root, textvariable= D).grid(column=0, row=2)
    def confirm_D():
        pera()
        print("confirm")
        pero = find_parm(D.get())
        export(pero)
        lbl3 = ttk.Label(text= pero).grid(column=0, row= 3)
    btn = ttk.Button(text= "Potvrdit", command=confirm_D, width=15).grid(column=2, row=2)
    btn2 = ttk.Button(text= "Zpět", command=mainMenu, width=15).grid(column=2, row=0)

j = float()

def setj(value):
    global j
    j = value
    print (j)


def kv():
    cls()
    print("Main.py kv")
    lbl = ttk.Label(text="Výpočet kvadratických průřezů").grid(row = 0, column=0)


    def square_UI():
        cls()
        ttk.Label(text=fncsstr[0] + "[mm]").grid(row=0, column=1)
        a = tk.DoubleVar()
        ttk.Label(text= "a: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= a).grid(row=1, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv1.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            square_UI()
            print("confirm")
            answer = square(a.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=15, y=55)
        ttk.Button(text= "Uložit pro výpočet nosníku", command=lambda *args: setj())
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def hollow_square_UI():
        cls()
        ttk.Label(text=fncsstr[1] + "[mm]").grid(row=0, column=1)
        H = tk.DoubleVar()
        h = tk.DoubleVar()
        ttk.Label(text= "H: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= H).grid(row=1, column=1)
        ttk.Label(text= "h: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= h).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv2.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            hollow_square_UI()
            print("confirm")
            answer = hollow_square(H.get(), h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)    


    def rotated_square_UI():
        cls()
        ttk.Label(text=fncsstr[2] + "[mm]").grid(row=0, column=1)
        a = tk.DoubleVar()
        ttk.Label(text= "a: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= a).grid(row=1, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv3.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            rotated_square_UI()
            print("confirm")
            answer = rotated_square(a.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def rotated_hollow_square_UI():
        cls()
        ttk.Label(text=fncsstr[3] + "[mm]").grid(row=0, column=1)
        H = tk.DoubleVar()
        h = tk.DoubleVar()
        ttk.Label(text= "H: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= H).grid(row=1, column=1)
        ttk.Label(text= "h: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= h).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv4.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            rotated_hollow_square_UI()
            print("confirm")
            answer = rotated_hollow_square(H.get(),h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def rectangle_UI():
        cls()
        ttk.Label(text=fncsstr[4] + "[mm]").grid(row=0, column=1)
        b = tk.DoubleVar()
        h = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= b).grid(row=1, column=1)
        ttk.Label(text= "h: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= h).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv5.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            rectangle_UI()
            print("confirm")
            answer = rectangle(b.get(),h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def triangle_UI():
        cls()
        ttk.Label(text=fncsstr[5] + "[mm]").grid(row=0, column=1)
        b = tk.DoubleVar()
        h = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= b).grid(row=1, column=1)
        ttk.Label(text= "h: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= h).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv6.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            triangle_UI()
            print("confirm")
            answer = triangle(b.get(),h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def hex_UI():
        cls()
        ttk.Label(text=fncsstr[6] + "[mm]").grid(row=0, column=1)
        e = tk.DoubleVar()
        s = tk.DoubleVar()
        ttk.Label(text= "e: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= e).grid(row=1, column=1)
        ttk.Label(text= "s: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= s).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv7.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            hex_UI()
            print("confirm")
            answer = hex(e.get(),s.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def trapezoid_UI():
        cls()
        ttk.Label(text=fncsstr[7] + "[mm]").grid(row=0, column=1)
        b = tk.DoubleVar()
        b1 = tk.DoubleVar()
        h = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= b).grid(row=1, column=1)
        ttk.Label(text= "b1: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= b1).grid(row=2, column=1)
        ttk.Label(text= "h: ").grid(row=3, column=0)
        ttk.Entry(root, textvariable= h).grid(row=3, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv8.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            trapezoid_UI()
            print("confirm")
            answer = trapezoid(b.get(),b1.get(),h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def circle_UI():
        cls()
        ttk.Label(text=fncsstr[8] + "[mm]").grid(row=0, column=1)
        d = tk.DoubleVar()
        ttk.Label(text= "d: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= d).grid(row=1, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv9.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            circle_UI()
            print("confirm")
            answer = circle(d.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def hollow_circle_UI():
        cls()
        ttk.Label(text=fncsstr[9] + "[mm]").grid(row=0, column=1)
        d = tk.DoubleVar()
        ttk.Label(text= "d: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= d).grid(row=2, column=1)
        D = tk.DoubleVar()
        ttk.Label(text= "D: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= D).grid(row=1, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv10.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            hollow_circle_UI()
            print("confirm")
            answer = hollow_circle(D.get(), d.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def elipse_UI():
        cls()
        ttk.Label(text=fncsstr[10] + "[mm]").grid(row=0, column=1)
        b = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= b).grid(row=1, column=1)
        h = tk.DoubleVar()
        ttk.Label(text= "h: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= h).grid(row=2, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv11.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            elipse_UI()
            print("confirm")
            answer = elipse(b.get(), h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=75)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def TUL_UI():
        cls()
        ttk.Label(text=fncsstr[11] + "[mm]").grid(row=0, column=1)
        a = tk.DoubleVar()
        ttk.Label(text= "a: ").grid(row=1, column=0)
        ttk.Entry(root, textvariable= a).grid(row=1, column=1)
        H = tk.DoubleVar()
        ttk.Label(text= "H: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= H).grid(row=2, column=1)
        t = tk.DoubleVar()
        ttk.Label(text= "t: ").grid(row=3, column=0)
        ttk.Entry(root, textvariable= t).grid(row=3, column=1)
        B = tk.DoubleVar()
        ttk.Label(text= "B: ").grid(row=4, column=0)
        ttk.Entry(root, textvariable= B).grid(row=4, column=1)
        h = tk.DoubleVar()
        ttk.Label(text= "h: ").grid(row=5, column=0)
        ttk.Entry(root, textvariable= h).grid(row=5, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv12.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            TUL_UI()
            print("confirm")
            answer = TUL(a.get(), H.get(), t.get(), B.get(), h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=140)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def H_UI():
        cls()
        ttk.Label(text=fncsstr[12] + "[mm]").grid(row=0, column=1)
        H = tk.DoubleVar()
        ttk.Label(text= "H: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= H).grid(row=2, column=1)
        h = tk.DoubleVar()
        ttk.Label(text= "h: ").grid(row=3, column=0)
        ttk.Entry(root, textvariable= h).grid(row=3, column=1)
        B = tk.DoubleVar()
        ttk.Label(text= "B: ").grid(row=4, column=0)
        ttk.Entry(root, textvariable= B).grid(row=4, column=1)
        b = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=5, column=0)
        ttk.Entry(root, textvariable= b).grid(row=5, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv13.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            H_UI()
            print("confirm")
            answer = H_profile(B.get(), b.get(), H.get(), h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=140)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    def I_UI():
        cls()
        ttk.Label(text=fncsstr[13] + "[mm]").grid(row=0, column=1)
        H = tk.DoubleVar()
        ttk.Label(text= "H: ").grid(row=2, column=0)
        ttk.Entry(root, textvariable= H).grid(row=2, column=1)
        h = tk.DoubleVar()
        ttk.Label(text= "h: ").grid(row=3, column=0)
        ttk.Entry(root, textvariable= h).grid(row=3, column=1)
        B = tk.DoubleVar()
        ttk.Label(text= "B: ").grid(row=4, column=0)
        ttk.Entry(root, textvariable= B).grid(row=4, column=1)
        b = tk.DoubleVar()
        ttk.Label(text= "b: ").grid(row=5, column=0)
        ttk.Entry(root, textvariable= b).grid(row=5, column=1)
        img = ImageTk.PhotoImage(Image.open(f"imgs/kv14.jpg"))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=240, y=0)
        def confirm():
            I_UI()
            print("confirm")
            answer = I_profile(B.get(), b.get(), H.get(), h.get())
            export(answer[1])
            setj(answer[0])
            lbl3 = ttk.Label(text= answer[1] + "\n\nHodnota Jx byla uložena pro\npřípadné výpočty nosníku").place(x=20, y=140)
        ttk.Button(text= "Potvrdit", command= confirm, width=10).grid(column=8, row=1)
        ttk.Button(text= "Zpět", command= kv, width=10).grid(column=8, row=0)


    ttk.Button(text= fncsstr[0 ], command= square_UI, width=40).grid(column=0, row=1)
    ttk.Button(text= fncsstr[1 ], command= hollow_square_UI, width=40).grid(column=0, row=2)
    ttk.Button(text= fncsstr[2 ], command= rotated_square_UI, width=40).grid(column=0, row=3)
    ttk.Button(text= fncsstr[3 ], command= rotated_hollow_square_UI, width=40).grid(column=0, row=4)
    ttk.Button(text= fncsstr[4 ], command= rectangle_UI, width=40).grid(column=0, row=5)
    ttk.Button(text= fncsstr[5 ], command= triangle_UI, width=40).grid(column=0, row=6)
    ttk.Button(text= fncsstr[6 ], command= hex_UI, width=40).grid(column=0, row=7)
    ttk.Button(text= fncsstr[7 ], command= trapezoid_UI, width=40).grid(column=0, row=8)
    ttk.Button(text= fncsstr[8 ], command= circle_UI, width=40).grid(column=0, row=9)
    ttk.Button(text= fncsstr[9 ], command= hollow_circle_UI, width=40).grid(column=0, row=10)
    ttk.Button(text= fncsstr[10], command= elipse_UI, width=40).grid(column=0, row=11)
    ttk.Button(text= fncsstr[11], command= TUL_UI, width=40).grid(column=0, row=12)
    ttk.Button(text= fncsstr[12], command= H_UI, width=40).grid(column=0, row=13)
    ttk.Button(text= fncsstr[13], command= I_UI, width=40).grid(column=0, row=14)
    ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=2, row=0)

def cepy():
    print("Main.py cepy")
    cls()
    lbl = ttk.Label(text="Přiřazení závlačky k čepu").grid(column=0, row=0)
    lbl2 = ttk.Label(text="Průměr čepu: ").grid(column=0, row=1)
    img = ImageTk.PhotoImage(Image.open(f"imgs/zavlacky_img.jpg"))
    image = Label(root, image= img)
    image.photo = img
    image.grid(column=3, row=3)
    D = tk.DoubleVar()
    ent = ttk.Entry(root, textvariable= D).grid(column=0, row=2)
    def confirm_D():
        cepy()
        print("confirm")
        zavlacka = assign_zavlacka(D.get())
        export(zavlacka)
        lbl3 = ttk.Label(text= zavlacka).grid(column=0, row= 3)
    btn = ttk.Button(text= "Potvrdit", command=confirm_D, width=15).grid(column=2, row=2)
    btn2 = ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=2, row=0)

def nosniky():
    print("Main.py nosniky")
    cls()
    lbl = ttk.Label(text="Výpočty nosníků").grid(column=0, row=0)
    inp = tk.DoubleVar()


    def UI(inp):
        cls()
        F  =  tk.DoubleVar()
        l  =  tk.DoubleVar()
        E  =  tk.DoubleVar()
        J  =  tk.DoubleVar()
        q  =  tk.DoubleVar()
        Q  =  tk.DoubleVar()
        M  =  tk.DoubleVar()
        Mb =  tk.DoubleVar()
        Ma =  tk.DoubleVar()
        a  =  tk.DoubleVar()
        b  =  tk.DoubleVar()
        c  =  tk.DoubleVar()
        cases = {
            1    : [["F: ", "l: ", "E: ", "J: "],                       [F, l, E, J]            , ["N"  , "mm", "MPa", "mm4"                    ], f"imgs/Nosnik1.jpg"  , "Vetknutý nosík s jednotou silou na konci"                                      ],
            2    : [["F: ", "l: ", "E: ", "J: "],                       [F, l, E, J]            , ["N"  , "mm", "MPa", "mm4"                    ], f"imgs/Nosnik2.jpg"  , "Vetknutý nosík s jednotou silou na uprostřed"                                  ],
            3    : [["q: ", "Q: ", "l: ", "E: ", "J: "],                [q, Q, l, E, J]         , ["N/m", "N" , "mm" , "MPa", "mm4"             ], f"imgs/Nosnik3.jpg"  , "Vetknutý nosík se konstantním spojitým zatížením"                              ],
            4    : [["M: ", "l: ", "E: ", "J: "],                       [M, l, E, J]            , ["Nm" , "mm", "MPa", "mm4"                    ], f"imgs/Nosnik4.jpg"  , "Vetknutý nosík zatížený ohybovým momentem"                                     ],
            5    : [["q: ", "l: ", "E: ", "J: "],                       [q, l, E, J]            , ["N/m", "mm", "MPa", "mm4"                    ], f"imgs/Nosnik5.jpg"  , "Vetknutý nosík se lineárním spojitým zatížením"                                ],
            6    : [["F: ", "l: ", "E: ", "J: "],                       [F, l, E, J]            , ["N"  , "mm", "MPa", "mm4"                    ], f"imgs/Nosnik6.jpg"  , "Nosník na dvou podporách se silou uprostřed"                                   ],
            7    : [["F: ", "a: ", "b: ", "c: ", "l: ", "E: ", "J: "],  [F, a, b, c,  l, E, J]  , ["N"  , "mm", "mm" , "mm" , "mm", "MPa", "mm4"], f"imgs/Nosnik7.jpg"  , "Nosník na dvou podporách se silou obecně"                                      ],
            8    : [["F: ", "a: ", "l: ", "E: ", "J: "],                [F, a, l, E, J]         , ["N"  , "mm", "mm" , "MPa", "mm4"             ], f"imgs/Nosnik8.jpg"  , "Nosník na dvou podporách se silou na převislém konci"                          ],
            9    : [["F: ", "a: ", "l: ", "E: ", "J: "],                [F, a, l, E, J]         , ["N"  , "mm", "mm" , "MPa", "mm4"             ], f"imgs/Nosnik9.jpg"  , "Nosník na dvou podporách se dvěma zatěžujícími silami"                         ],
            10   : [["F: ", "a: ", "l: ", "E: ", "J: "],                [F, a, l, E, J]         , ["N"  , "mm", "mm" , "MPa", "mm4"             ], f"imgs/Nosnik10.jpg" , "Nosník na dvou podporách se dvěma zatěžujícími silami na převislých koncích"   ],
            11   : [["q: ", "Q: ", "l: ", "E: ", "J: "],                [q, Q, l, E, J]         , ["N/m", "N" , "mm" , "MPa", "mm4"             ], f"imgs/Nosnik11.jpg" , "Nosník na dvou podporách s konstantním spojitým zatížením"                     ],
            12   : [["q: ", "l: ", "E: ", "J: "],                       [q, l, E, J]            , ["N/m", "mm", "MPa", "mm4"                    ], f"imgs/Nosnik12.jpg" , "Nosník na dvou podporách s lineárním spojitým zatížením"                       ],
            13   : [["q: ", "a: ", "l: ", "E: ", "J: "],                [q, a, l, E, J]         , ["N/m", "mm", "mm" , "MPa", "mm4"             ], f"imgs/Nosnik13.jpg" , "Nosník na dvou podporách s převislími koncemi a spojitým zatížením"            ],
            14   : [["Ma: ","Mb: ", "l: ", "E: ", "J: "],               [Ma, Mb, l, E, J]       , ["Nm" , "Nm", "mm" , "MPa", "mm4"             ], f"imgs/Nosnik14.jpg" , "Nosník na dvou podporách zatížený dvěma ohybovými momenty"                     ],
        }
        lbl = ttk.Label(text= cases[inp][4]).place(x=180, y=0)
        img = ImageTk.PhotoImage(Image.open(cases[inp][3]))
        image = Label(root, image= img)
        image.photo = img
        image.place(x=180, y=20)
        x = 3
        for i in cases[inp][0]:
            ttk.Label(text= i).grid(row=x, column=0)
            x += 1
        x = 3
        for i in cases[inp][1]:
            ttk.Entry(root, textvariable= i).grid(row=x, column=1)
            x += 1
        x = 3
        for i in cases[inp][2]:
            ttk.Label(root, text= i).grid(row=x, column=2)
            x += 1

        def confirm():
            cls()
            UI(inp)
            try:
                nos = nosnik(inp, F = F.get(), l = l.get(), E = (E.get()*10**6), J = J.get(), q = q.get(), Q = Q.get(), M= M.get(), Ma = Ma.get(), Mb = Mb.get(), a = a.get(), b = b.get(), c = c.get())
                output = nosnik.vypocet(nos)
                export(output)
                lbl3 = tk.Label(text= output).place(y=200, x=0)
            except ZeroDivisionError:
                print(j)
                nos = nosnik(inp, F = F.get(), l = l.get(), E = (E.get()*10**6), J = j, q = q.get(), Q = Q.get(), M= M.get(), Ma = Ma.get(), Mb = Mb.get(), a = a.get(), b = b.get(), c = c.get())
                output = nosnik.vypocet(nos)
                export(output)
                lbl3 = tk.Label(text= output + "\nJx nebylo zadáno, počítá se s posledním výpočtem kvadratického průřezu").place(y=200, x=0)



        btn = ttk.Button(text= "Potvrdit", command=confirm, width=15).grid(column=1, row=10)
        btn2 = ttk.Button(text="Zpět", command=nosniky, width=15).grid(column=1, row=11)


    def setcase(value):
        global inp
        inp = value
        UI(inp)

    btn = ttk.Button(text="Vetknutý nosík s jednotou silou na konci"                                   , command=lambda *args: setcase(1),  width=70 ).grid(column=0, row=1 )
    btn = ttk.Button(text="Vetknutý nosík s jednotou silou na uprostřed"                               , command=lambda *args: setcase(2),  width=70 ).grid(column=0, row=2 )
    btn = ttk.Button(text="Vetknutý nosík se konstantním spojitým zatížením"                           , command=lambda *args: setcase(3),  width=70 ).grid(column=0, row=3 )
    btn = ttk.Button(text="Vetknutý nosík zatížený ohybovým momentem"                                  , command=lambda *args: setcase(4),  width=70 ).grid(column=0, row=4 )
    btn = ttk.Button(text="Vetknutý nosík se lineárním spojitým zatížením"                             , command=lambda *args: setcase(5),  width=70 ).grid(column=0, row=5 )
    btn = ttk.Button(text="Nosník na dvou podporách se silou uprostřed"                                , command=lambda *args: setcase(6),  width=70 ).grid(column=0, row=6 )
    btn = ttk.Button(text="Nosník na dvou podporách se silou obecně"                                   , command=lambda *args: setcase(7),  width=70 ).grid(column=0, row=7 )
    btn = ttk.Button(text="Nosník na dvou podporách se silou na převislém konci"                       , command=lambda *args: setcase(8),  width=70 ).grid(column=0, row=8 )
    btn = ttk.Button(text="Nosník na dvou podporách se dvěma zatěžujícími silami"                      , command=lambda *args: setcase(9),  width=70 ).grid(column=0, row=9 )
    btn = ttk.Button(text="Nosník na dvou podporách se dvěma zatěžujícími silami na převislých koncích", command=lambda *args: setcase(10),  width=70).grid(column=0, row=10)
    btn = ttk.Button(text="Nosník na dvou podporách s konstantním spojitým zatížením"                  , command=lambda *args: setcase(11),  width=70).grid(column=0, row=11)
    btn = ttk.Button(text="Nosník na dvou podporách s lineárním spojitým zatížením"                    , command=lambda *args: setcase(12),  width=70).grid(column=0, row=12)
    btn = ttk.Button(text="Nosník na dvou podporách s převislími koncemi a spojitým zatížením"         , command=lambda *args: setcase(13),  width=70).grid(column=0, row=13)
    btn = ttk.Button(text="Nosník na dvou podporách zatížený dvěma ohybovými momenty"                  , command=lambda *args: setcase(14),  width=70).grid(column=0, row=14)
    btn = ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=2, row=0)


def outputFile():
        cls()
        lbl = ttk.Label(text="Historie výstupů").grid(column=0, row=0)
        with open("export.txt", "r+") as f:
            text = f.read()
        txt = Text(root, height=40)
        txt.place(y=80, x=0)
        txt.insert(INSERT, text)
        def clearexport():
            f = open('export.txt', 'r+')
            f.truncate(0)
            outputFile()
        btn = ttk.Button(text="Vymazat výstupy", command=clearexport, width=15).grid(column=0, row=2)
        btn2 = ttk.Button(text="Zpět", command=mainMenu, width=15).grid(column=0, row=1)


root = Tk()
mainMenu()
root.mainloop()