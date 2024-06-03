import flet as ft
import random


def main(page: ft.Page):
    page.title = 'Quiz_Projekt'
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = '#0ad7bf'
    page.horizontal_alignment = "center"
    page.window_width = 600
    page.window_height = 600
    page.window_resizable = False
    page.update()

    def tovabb(e):
        pontszam = 0
        ###cannot_access_local_variable_oldalszam_where_it_is_not_associated_with_a_value
        ###cannot_access_local_variable_pontszam_where_it_is_not_associated_with_a_value
        if (adalotf.value == "Ada Lovelace"):
            pontszam += 1
        else:
            adalotf.error_text = "A helyes válasz: Ada Lovelace"
        if (kevintf.value == "Hacker" or kevintf.value == "hacker"):
            pontszam += 1
        else:
            kevintf.error_text = "A helyes válasz: Hacker/hacker"
        if (charlradio.value == "Mechatronika, matematika, filozófia"):
            pontszam += 1
        else:
            charltext.value+="A\n helyes válasz: Mechatronika, matematika, filozófia"
            charltext.color='red'
        if (macradio.value == "Rhapsody Developer Release"):
            pontszam += 1
        else:
            mactext.value += "\nA helyes válasz: Rhapsody Developer Release"
            mactext.color='red'
        if (it.value == "Igaz"):
            pontszam += 1
        else:
            itcont.error_text="A helyes válasz: Igaz"
        if (wm.value == "Hamis"):
            pontszam+=1
        else:
            wmcont.error_text="A helyes válasz: Hamis"

        if (prgch3.value == True or prgch5.value == True or prgch6.value == True):
            pontszam += 1
        if (prgch3.value == True and prgch6.value == True and prgch5.value == True):
            pontszam += 1
        else:
            progq.value += "\nA helyes válaszok: Alan Turing, J. Presper Eckert, John Mauchly"
            progq.color='red'
            progq.size=15

        if (prch3.value == True or prch2.value == True or prch6.value == True):
            pontszam += 1
        if (prch3.value == True and prch6.value == True and prch2.value == True):
            pontszam += 1
        else:
            prlanok.value += "\nA helyes válaszok: APL, Pascal, Basic"
            prlanok.color='red'
            prlanok.size=15

        ertektext = ft.Text("Az elért pontszám:\n", color='yellow', size=20)
        ertek = ft.Text(f"\t\t{pontszam}/10\n", color='red', size=30)

        ertekcont = ft.Column(controls=[ertektext, ertek])

        page.remove(b1)

        page.add(ertekcont, b1)

    adalok = ft.Container(content=ft.Image(src="https://dynaimage.cdn.cnn.com/cnn/w_768,h_1024,c_scale/https%3A%2F%2Fdynaimage.cdn.cnn.com%2Fcnn%2Fx_376%2Cy_12%2Cw_527%2Ch_704%2Cc_crop%2Fhttps%253A%252F%252Fstamp.static.cnn.io%252F5bab86cf4db3d70020c01c3e%252Fada2.jpg",
    border_radius=20, height=256, width=192, fit=ft.ImageFit.CONTAIN))
    adalotf = ft.TextField(label="Ki látható a képen?", color='#846a00', width=200, bgcolor='#51ba00')
    adalocontainer = ft.Column(controls=[adalok, adalotf])

    kevinimg= ft.Container(content=ft.Image(src="https://i.ytimg.com/vi/0wUVyoPw7Rs/oar2.jpg?sqp=-oaymwEYCJUDENAFSFqQAgHyq4qpAwcIARUAAIhC&rs=AOn4CLDl5Is6Xv0Qxma7rAfsa43Ymdzz_Q"),
    height=256, width=192, bgcolor='black')
    kevintf = ft.TextField(label="Mi volt ő?", color='white', bgcolor='#51ba00', width=200)
    kevincontainer = ft.Column(controls=[kevinimg, kevintf])

    prlanok = ft.Text(value="Melyik nyelveket nem használják már?", size=20)
    prch1 = ft.Checkbox(label="C++", value=False)
    prch2 = ft.Checkbox(label="APL", value=False)
    prch3 = ft.Checkbox(label="Basic", value=False)
    prch4 = ft.Checkbox(label="Lua", value=False)
    prch5 = ft.Checkbox(label="Q", value=False)
    prch6 = ft.Checkbox(label="Pascal", value=False)
    prch7 = ft.Checkbox(label="Dart", value=False)

    prlanchecks1 = ft.Row(controls=[prch1, prch2, prch3, prch4], width=250)
    prlanchecks2 = ft.Row(controls=[prch5, prch6, prch7], width=250)
    prcontainer = ft.Column(controls=[prlanok, prlanchecks1, prlanchecks2])

    progq = ft.Text(value="Kik számítottak a korai\nszámítástechnika úttörőinek?", size=20)
    prgch1 = ft.Checkbox(label="Philip Don Estridge", value=False)
    prgch2 = ft.Checkbox(label="Charles Cabbage", value=False)
    prgch3 = ft.Checkbox(label="Alan Turing", value=False)
    prgch4 = ft.Checkbox(label="Jack Kilby", value=False)
    prgch5 = ft.Checkbox(label="John Mauchly", value=False)
    prgch6 = ft.Checkbox(label="J. Presper Eckert", value=False)
    prgch7 = ft.Checkbox(label="Ted Hoff", value=False)

    progozok1 = ft.Row(controls=[prgch1, prgch2], width=300)
    progozok2 = ft.Row(controls=[prgch3, prgch4, prgch5], width=300)
    progozok3 = ft.Row(controls=[prgch6, prgch7], width=300)
    progozcontainer = ft.Column(controls=[progq, progozok1, progozok2, progozok3])

    charltext = ft.Text("Mely területeken tevékenykedett Charles Babbage?", color='black')
    charlradio = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Matematika, fizika", label="Matematika, fizika"),
        ft.Radio(value="Fizika, filozófia", label="Fizika, filozófia"),
        ft.Radio(value="Mechatronika, matematika, filozófia", label="Mechatronika, matematika, filozófia"),
        ft.Radio(value="Matematika, filozófia, fizika", label="Matematika, filozófia, fizika")]))
    charlcont = ft.Column(controls=[charltext, charlradio])

    mactext = ft.Text("Melyik MacOS verzió a legkorábbi?", color='black')
    macradio = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Mac OS X Server 1.0", label="Mac OS X Server 1.0"),
        ft.Radio(value="Mac OS X Public Beta", label="Mac OS X Public Beta"),
        ft.Radio(value="Rhapsody Developer Release", label="Rhapsody Developer Release"),
        ft.Radio(value="Mac OS X Developer Preview", label="Mac OS X Developer Preview")]))
    maccont = ft.Column(alignment=ft.alignment.center, controls=[mactext, macradio])

    wmtext = ft.Text("A Windows előbb jelent, meg mint a MacOS.")
    wm = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option("Hamis"),
            ft.dropdown.Option("Igaz"),
        ],
        label="", autofocus=True, hint_text="Igaz vagy Hamis")
    wmcont = ft.Column(alignment=ft.alignment.center,controls=[wmtext, wm])

    ittext = ft.Text("Az 'információs technika' (IT) kifejezés\nelőszőr egy folyóiratban jelent meg.")
    it = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option("Hamis"),
            ft.dropdown.Option("Igaz"),
        ],
        label="", autofocus=True, hint_text="Igaz vagy Hamis")
    itcont = ft.Column(controls=[ittext, it])


    fokeret =ft.Column(controls=[adalocontainer, kevincontainer, prcontainer, progozcontainer, charlcont, maccont, wmcont, itcont])
    randomok = []
    while(len(randomok) != len(fokeret.controls)):
        r = random.randint(0, len(fokeret.controls) - 1)
        if r not in randomok:
            randomok.append(r)

    randomkeret= ft.Column(controls=[])
    for i in randomok:
        randomkeret.controls.append(fokeret.controls[i])

    b1 = ft.ElevatedButton(text="Ellenőrzés", on_click=tovabb, color='blue')

    page.add(randomkeret, b1)
    page.update()



    page.update()

ft.app(target=main)