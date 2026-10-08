# SW
from pyscript import document, display


def output(event):

    Nickname = document.getElementById("Countries")
    Nickname_Value = str(Nickname.value)

    display(f'{Nickname_Value}', target='result', append=False)