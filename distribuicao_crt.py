import keyboard
from time import sleep
# falar pra luh de trocar o 'esc' por '9', o nove também ficaria registrado na tela no campo obs o 'esc' ou teclas de função como 'f1', 'f2', etc. não aparecem
print("[i] - Programa iniciado.\nComandos:")
print("    teclas -> descrição")
print("    [0] -> Ativar atalhos (1 a 6)")
print("    [1] -> Tecla para escrever a frase do óbito")
print("    [2] -> Tecla para escrever a frase de não necessita")
print("    [3] -> Tecla para escrever a frase de já realizada")
print("    [4] -> Tecla para escrever a frase de Sim/pct ainda necessita da consulta falada com 3°")
print("    [5] -> Tecla para escrever a frase de Sim/pct ainda necessita da consulta")
print("    [6] -> Tecla para escrever a frase de 4° contato realizado")
print("    [esc] -> Desativar atalhos atuais")
print("    [Enter] -> Sair do programa totalmente\n")

def registrar_atalhos():
    
    atalhos = {
        '1': "Conforme contato na data --------- foi informado óbito. Confirmado com ------.",
        '2': "Conforme contato na data ------------ informa que não necessita mais da consulta. Confirmado com -----.",
        '3': "Conforme contato na data ------------- informa que já realizou a consulta. Confirmado com ------.",
        '4': "Conforme contato paciente aguarda consulta. Confirmado com -----.",
        '5': "Conforme contato paciente aguarda consulta.",
        '6': "4° Tentativa realizada sem sucesso."
    }
    
    hooks = []
    for tecla, texto in atalhos.items():
        h = keyboard.add_hotkey(tecla, lambda t=texto: keyboard.write(t, delay=0.01))
        hooks.append(h)
    return hooks

def main():
    atalhos_ativos = []
    
    while True:
        # sair
        if keyboard.is_pressed('enter'):
            print('[-] - Encerrando o programa...')
            break

        # ativar os atalhos
        if keyboard.is_pressed('0'):
            if not atalhos_ativos:
                print('[+] - Atalhos ATIVADOS (1-6). Pressione [esc] para pausar.')
                atalhos_ativos = registrar_atalhos()
                # Pequena pausa para não registrar múltiplos cliques
                sleep(0.3)

        # desativar os atalhos
        if keyboard.is_pressed('esc'):
            if atalhos_ativos:
                for h in atalhos_ativos:
                    keyboard.remove_hotkey(h)
                atalhos_ativos = []
                print('[-] - Atalhos DESATIVADOS. Aguardando [0] para reativar ou [Enter] para sair.')
                sleep(0.3)

        sleep(0.1) # Reduz o uso de CPU

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[-] - Ocorreu um erro: {e}")
