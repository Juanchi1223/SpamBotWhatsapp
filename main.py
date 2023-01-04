import pyautogui
import webbrowser as web
from time import sleep 
import keyboard

numero = pyautogui.prompt(text='Ingrese el numero', title='BOT SPAMMER 1.0' , default='')

x =  pyautogui.confirm(f'Confirmas que es este el numero que queres spamear \n {numero}', buttons=['SI', 'NO'])

if x == 'NO':
    pass
else:
    web.open(f"https://web.whatsapp.com/send?phone={numero}")
    sleep(10)

    while(True):
        pyautogui.write("CARA DE CHOTA")
        pyautogui.press("enter")
        if keyboard.is_pressed("space"):
            break