import keyboard
from time import sleep

print("[i] - Programa iniciado. Comandos:")
print("    [s] -> Ativar atalhos (1 a 6)")
print("    [esc] -> Desativar atalhos atuais")
print("    [q] -> Sair do programa totalmente\n")

def registrar_atalhos():
    # Usamos um dicionário para facilitar a remoção posterior
    atalhos = {
        '1': "Conforme contato na data --------- foi informado óbito. Confirmado com ------.",
        '2': "Conforme contato na data ------------ informa que não necessita mais da consulta. Confirmado com -----.",
        '3': "Conforme contato na data ------------- informa que já realizou a consulta. Confirmado com ------.",
        '4': "Conforme contato paciente aguarda consulta. Confirmado com -----.",
        '5': "Conforme contato paciente aguarda consulta." ,
        '6': "4° Tentativa realizada sem sucesso"
    }
    
    hooks = []
    for tecla, texto in atalhos.items():
        h = keyboard.add_hotkey(tecla, lambda t=texto: keyboard.write(t))
        hooks.append(h)
    return hooks

def main():
    atalhos_ativos = []
    
    while True:
        # Verifica se o usuário quer sair
        if keyboard.is_pressed('q'):
            print('[-] - Encerrando o programa...')
            break

        # Verifica se o usuário quer ativar os atalhos
        if keyboard.is_pressed('s'):
            if not atalhos_ativos:
                print('[+] - Atalhos ATIVADOS (1-6). Pressione [ESC] para pausar.')
                atalhos_ativos = registrar_atalhos()
                # Pequena pausa para não registrar múltiplos cliques
                sleep(0.3)

        # Verifica se o usuário quer desativar os atalhos
        if keyboard.is_pressed('esc'):
            if atalhos_ativos:
                for h in atalhos_ativos:
                    keyboard.remove_hotkey(h)
                atalhos_ativos = []
                print('[-] - Atalhos DESATIVADOS. Aguardando [s] para reativar ou [q] para sair.')
                sleep(0.3)

        sleep(0.1) # Reduz o uso de CPU

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[-] - Ocorreu um erro: {e}")