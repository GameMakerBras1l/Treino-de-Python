# Primeiro dos 4 projetos feito nesse mini curço
# A primeira aula é sobre automação de tarefas

# pip install nome da biblioteca
#  o comando acima é para instalar uma nova biblioteca

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5
# Configuração para intervalo de tempo entre os comandos do pyautogui

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(site)

pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=756, y=412)
pyautogui.write("fulano@gmail.com")

pyautogui.press("tab")
pyautogui.write("Senha")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

tabela = pandas.read_csv("produtos.csv")

time.sleep(3)

print(tabela.head())

for linha in tabela.index:
    pyautogui.click(x=801, y=286)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)

    pyautogui.press("tab")
    custo =  str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

