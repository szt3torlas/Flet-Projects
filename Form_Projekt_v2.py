import flet as ft


def main(page: ft.Page):
    page.title = 'Form_Projekt'
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor='yellow'
    page.window_width = 600
    page.window_height = 600

    def button_clicked(e):
        hibatlan = True
        vankedv = False
        checkbox = "Kedvelt nyelvek:"
        fzbz = "Fizz vagy Buzz?\n - "
        lvn = "\nIgen vagy nem?\n - "
        if (len(user.value) == 0):
            user.error_text = "Üresen hagyta a mezőt!"
            hibatlan = False
        if (len(email.value) == 0):
            email.error_text = "Üresen hagyta a mezőt!"
            hibatlan = False
        if (len(psw.value) < 8):
            psw.error_text = "A jelszónak legalább 8 karakter hosszúnak kell lennie!"
            hibatlan = False
        if (radio.value == "Fizz" or radio.value == "Buzz" or radio.value == "FizzBuzz"):
            fzbz += radio.value
        else:
            fzbz = ""

        if (dd.value == "Igen" or dd.value == "Nem"):
            lvn += dd.value
        else:
            lvn = ""


        if (ch1.value):
            checkbox += "\n - " + ch1.label
            vankedv = True
        if (ch2.value):
            checkbox += "\n - " + ch2.label
            vankedv = True
        if (ch3.value):
            checkbox += "\n - " + ch3.label
            vankedv = True
        if (ch4.value):
            checkbox += "\n - " + ch4.label
            vankedv = True
        if (ch5.value):
            checkbox += "\n - " + ch5.label
            vankedv = True
        if (ch6.value):
            checkbox += "\n - " + ch6.label
            vankedv = True
        if (ch7.value):
            checkbox += "\n - " + ch7.label
            vankedv = True

        if (not(vankedv)):
            checkbox = "A felsorolt nyelvek közül egy sem kedvelt"

        if (hibatlan):
            t1.value = f"A felhasználó adatai:\n - Név: {user.value}\n - E-mail: {email.value}"
            t1.value += "\n" + checkbox + "\n" + fzbz + lvn
        else:
            t1.value = "Valahol hibás adatot adott meg"
        page.update()
    def count_characters(e):
        psw.counter_text = f'{len(psw.value)} symbols typed'
        page.update()


    t1 = ft.Text(color='white')
    cont1 = ft.Container(t1, width=350, bgcolor='black', padding=20)
    user = ft.TextField(label="Neve", hint_text="Adja meg a teljes nevét", icon=ft.icons.EMOJI_EMOTIONS, width=500, error_text="", bgcolor='green', color='white', cursor_color='yellow')
    email = ft.TextField(label="Email-címe", suffix_text=".com", prefix_icon=ft.icons.FORMAT_SIZE, helper_text="You can type only one color", width=500, bgcolor='green', color='white', cursor_color='yellow')
    psw = ft.TextField(label="Adja meg a jelszavát", password=True, can_reveal_password=True, width=500, error_text="", counter_text="0 symbols typed", on_change=count_characters, bgcolor='green', color='white', cursor_color='yellow')
    b1 = ft.ElevatedButton(text="Submit", on_click=button_clicked)###keret.append(),
    checktext = ft.Text("|Kedvelt programozási nyelvek:", color='white', bgcolor='blue')
    ch1 = ft.Checkbox(label="C#", value=False)
    ch2 = ft.Checkbox(label="Dart", value=False)
    ch3 = ft.Checkbox(label="Python", value=False)
    ch4 = ft.Checkbox(label="Javascript", value=False)
    ch5 = ft.Checkbox(label="Pascal", value=False)
    ch6 = ft.Checkbox(label="Java", value=False)
    ch7 = ft.Checkbox(label="Ada", value=False)
    raditext = ft.Text("|Fizz vagy Buzz", color='white', bgcolor='blue')
    radio = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="Fizz", label="Fizz"),
        ft.Radio(value="Buzz", label="Buzz"),
        ft.Radio(value="FizzBuzz", label="FizzBuzz")]))
    dd = ft.Dropdown(
        width=250,
        options=[
            ft.dropdown.Option("Igen"),
            ft.dropdown.Option("Nem"),
        ],
    label="Igen vagy Nem?", autofocus=True, hint_text="Igen vagy Nem?")
#label_position=ft.LabelPosition.LEFT
    page.add(user, email, psw,checktext, ch1, ch2, ch3, ch4, ch5, ch6, ch7, raditext, radio, dd, ft.Divider(), b1, cont1)
    """
    col = ft.Column(controls=[user, email, psw,checktext, ch1, ch2, ch3, ch4, ch5, ch6, ch7, raditext, radio, dd, ft.Divider(), b1, cont1])
    page.add(col)

"""
    page.update()

ft.app(target=main)