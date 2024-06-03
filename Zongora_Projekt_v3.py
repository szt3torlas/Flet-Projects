import flet as ft
#import time # ki lett véve

def main(page: ft.Page):
    page.title = 'Zongora_Projekt'
    audio1 = ft.Audio(
        src="waiting wav", autoplay=True
    )
    page.overlay.append(audio1)
    page.add(
        ft.Text("This is an app with background audio."),
        ft.ElevatedButton("Stop playing", on_click=lambda _: audio1.pause()),
    )
    def hang(a): # gomb lenyomásakor behívott függvény
        if (a == i.value): #lenyomott billentyű = a zongora billentyű (kép, és szöveg) értékével
            page.update()
            i.bgcolor = 'red' #gombnyomás látszódása, a zongorán a lenyomott billentyűket jelezte volna
            audio1.src = ""
            #time.sleep(0.125)
            i.bgcolor = 'yellow'
            audio1.src = "a" # audio1 leállítása nem létező fájlnévvel
            page.update()
        if (a == u.value):
            page.update()
            ##i.bgcolor='red'
            U.src = ""
            #if (U.src != "a"):
            #   time.sleep(1)
            ##i.bgcolor='yellow'
            U.src = "a"
            page.update()

#### Az érzékelés késik vagy rosszul működik #####

    def on_keyboard(e: ft.KeyboardEvent):
        ##time.sleep(0.125)
        page.add(
            ft.Text(
                f"Key: {e.key}"# Shift: {e.shift}, Control: {e.ctrl}, Alt: {e.alt}, Meta: {e.meta}"
            )
        )
        hang(e.key)

    page.on_keyboard_event = on_keyboard
    page.add(
        ft.Text("Press any key with a combination of CTRL, ALT, SHIFT and META keys...")
    )
    # audiók billentyűnként
    U = ft.Audio(src="a", autoplay=True)
    i = ft.Text("I", bgcolor='yellow')
    u = ft.Text("U", bgcolor='yellow')
    page.add(i, U)

    page.overlay.append(U)

ft.app(target=main)
