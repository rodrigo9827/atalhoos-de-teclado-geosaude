# Atalhos de Teclado — GeoSaúde

Programa de automação para inserção de frases padronizadas de atendimento,
desenvolvido para uso interno na plataforma GeoSaúde.

---

## Atenção antes de usar

- Após extrair o arquivo ZIP na pasta **Downloads**, mova o arquivo **`start.bat`** para a **Área de Trabalho**.
- Após inserir uma frase, pressione **Enter** para encerrar o programa e evitar que ele escreva em campos indesejados.

---

## Teclas disponíveis

| Tecla   | Ação |
|---------|------|
| `0`     | Ativar os atalhos de 1 a 6 |
| `1`     | Escrever a frase de óbito |
| `2`     | Escrever a frase de não necessita |
| `3`     | Escrever a frase de já realizou |
| `4`     | Escrever a frase de Sim / paciente ainda necessita da consulta (falado com 3°) |
| `5`     | Escrever a frase de Sim / paciente ainda necessita da consulta |
| `6`     | Escrever a frase de 4° contato realizado |
| `Esc`   | Desativar os atalhos e aguardar novo `0` para reativar |
| `Enter` | Sair e encerrar o programa completamente |

---

## Como funciona (para revisão de segurança)

- **Não se conecta à internet** em nenhum momento.
- **Não grava teclas digitadas** em arquivo ou memória.
- **Não coleta nem envia nenhum dado** — funciona 100% localmente.
- Atua apenas enquanto está em execução, escrevendo somente as 6 frases fixas definidas no código-fonte.
- O código-fonte completo está disponível neste repositório para inspeção.

---

## Como instalar

1. Baixe o arquivo ZIP na aba [Releases](../../releases) deste repositório.
2. Extraia o conteúdo na pasta **Downloads**.
3. Mova o arquivo **`start.bat`** para a **Área de Trabalho**.
4. Clique duas vezes no `start.bat` para iniciar.