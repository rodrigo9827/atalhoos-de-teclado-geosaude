import keyboard
from time import sleep
print("[i] - program started by the user...press [s] to execute or [q] to exit \n")

while True:
    try:
        sleep(0.5)
        if keyboard.is_pressed('q'):
            print('[-] - Exit the program...')
            break
        keyboard.wait('s')
        print('[i] - Program started by the user')
        print('press [esc] key to return and wait to the [s] key')
        h1 = keyboard.add_hotkey('1', lambda: keyboard.write("Conforme contato na data --------- foi informado óbito. Confirmado com ------."))
        h2 = keyboard.add_hotkey('2', lambda: keyboard.write("Conforme contato na data ------------ informa que não necessita mais da consulta. Confirmado com -----."))
        h3 = keyboard.add_hotkey('3', lambda: keyboard.write("Conforme contato na data ------------- informa que já realizou a consulta. Confirmado com ------."))
        h4 = keyboard.add_hotkey('4', lambda: keyboard.write("Conforme contato paciente aguarda consulta. Confirmado com -----."))
        h5 = keyboard.add_hotkey('5', lambda: keyboard.write("4° Tentativa realizada sem sucesso"))

        keyboard.wait('esc')

        keyboard.remove_hotkey(h1)
        keyboard.remove_hotkey(h2)
        keyboard.remove_hotkey(h3)
        keyboard.remove_hotkey(h4)
        keyboard.remove_hotkey(h5)

        print("\n[-] - Shortcuts disabled, wait for the [s] key to continue")
        sleep(0.5)
        
        keyboard.wait('s')
        continue

    
    except Exception as e:
        print(f"[-] - any error ocorred {e}")
