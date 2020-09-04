from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
from pyautogui import *
import pyautogui
import time
import keyboard

class Client:
    def Jogar(self):
        if pyautogui.locateOnScreen('jogar.png', confidence=0.8) != None:
            jogar = pyautogui.locateOnScreen('jogar.png', confidence=0.8)
            pyautogui.moveTo(jogar)
            mouse.click(Button.left, 1)

    def Coop(self):
        if pyautogui.locateOnScreen('coop.png', confidence=0.8) != None:
            coop = pyautogui.locateOnScreen('coop.png', confidence=0.8)
            pyautogui.moveTo(coop)
            mouse.click(Button.left, 1)
            time.sleep(0.2)

            iniciante = pyautogui.locateOnScreen('iniciante.png', confidence=0.8)
            pyautogui.moveTo(iniciante)
            mouse.click(Button.left, 1)

            confirmar_coop = pyautogui.locateOnScreen('confirmar_coop.png', confidence=0.8)
            pyautogui.moveTo(confirmar_coop)
            mouse.click(Button.left, 1)

    def EncontrarPartida(self):
        if pyautogui.locateOnScreen('encontrar_partida.png', confidence=0.8) != None:
            encontrar_partida = pyautogui.locateOnScreen('encontrar_partida.png', confidence=0.8)
            pyautogui.moveTo(encontrar_partida)
            mouse.click(Button.left, 1)

    def Aceitar(self):
        if pyautogui.locateOnScreen('aceitar.png', confidence=0.8) != None:
            aceitar = pyautogui.locateOnScreen('aceitar.png', confidence=0.8)
            pyautogui.moveTo(aceitar)
            mouse.click(Button.left, 1)

    def JogarNovamente(self):
        if pyautogui.locateOnScreen('jogar_novamente.png', confidence=0.8) != None:
            jogar_novamente = pyautogui.locateOnScreen('jogar_novamente.png', confidence=0.8)
            pyautogui.moveTo(jogar_novamente)
            mouse.click(Button.left, 1)
            time.sleep(1)

    def Honra(self):
        if pyautogui.locateOnScreen('honra.png', confidence=0.8) != None:
            honra = pyautogui.locateOnScreen('honra.png', confidence=0.8)
            pyautogui.moveTo(honra)
            mouse.click(Button.left, 1)
            time.sleep(1)

    def FecharStat(self):
        if pyautogui.locateOnScreen('fechar_stat.png', confidence=0.8) != None:
            fechar_stat = pyautogui.locateOnScreen('fechar_stat.png', confidence=0.8)
            pyautogui.moveTo(fechar_stat)
            mouse.click(Button.left, 1)

    def Ok(self):
        if pyautogui.locateOnScreen('ok.png', confidence=0.8) != None:
            ok = pyautogui.locateOnScreen('ok.png', confidence=0.8)
            pyautogui.moveTo(ok)
            mouse.click(Button.left, 1)

class Selection:
    def Selecao(self):
        if pyautogui.locateOnScreen('select_champ.png', confidence=0.8) != None:
            time.sleep(4)
            pyautogui.moveTo(424, 461)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            pyautogui.moveTo(785, 176)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            pyautogui.moveTo(875, 174)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            pyautogui.moveTo(806, 259)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            pyautogui.moveTo(699, 259)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            pyautogui.moveTo(471, 259)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)

            confirmar = pyautogui.locateOnScreen('confirmar.png', confidence=0.8)
            time.sleep(4)
            pyautogui.moveTo(confirmar)
            time.sleep(4)
            mouse.click(Button.left, 1)
            time.sleep(4)


class Game:
    def Propaganda(self):
        pass

    def Loja(self):
        keyboard.press('p')
        keyboard.release('p')
        pyautogui.moveTo(457, 385)
        time.sleep(0.2)
        mouse.click(Button.right, 1)
        time.sleep(0.2)
        pyautogui.moveTo(360, 385)
        time.sleep(0.2)
        mouse.click(Button.right, 1)
        time.sleep(0.2)
        pyautogui.moveTo(360, 469)
        time.sleep(0.2)
        mouse.click(Button.right, 1)
        time.sleep(0.2)
        pyautogui.moveTo(410, 473)
        time.sleep(0.2)
        mouse.click(Button.right, 1)
        time.sleep(0.2)
        pyautogui.moveTo(452, 473)
        time.sleep(0.2)
        mouse.click(Button.right, 1)
        time.sleep(0.2)
        keyboard.press('p')
        keyboard.release('p')


    def Andar(self):
        direcao = pyautogui.locateOnScreen('ponto.png', confidence=0.8)
        pyautogui.moveTo(direcao)
        keyboard.press('a')
        keyboard.release('a')
        mouse.click(Button.left, 1)
        time.sleep(2.5)


BotC = Client()
BotS = Selection()
BotG = Game()

time.sleep(3)
mouse = Controller()

while True:
    print(pyautogui.position())
    time.sleep(1)
    if pyautogui.locateOnScreen('client.png', confidence=0.8) != None:
        print('In client')
        BotC.Jogar()
        BotC.Coop()
        BotC.EncontrarPartida()
        BotC.Aceitar()
        BotC.JogarNovamente()
        BotC.FecharStat()
        BotC.Ok()

    elif pyautogui.locateOnScreen('erro.png', confidence=0.8) != None:
        erro = pyautogui.locateOnScreen('erro.png', confidence=0.8)
        pyautogui.moveTo(erro)
        mouse.click(Button.left, 1)

    elif pyautogui.locateOnScreen('selection.png', confidence=0.8) != None:
        print('In selection')
        BotS.Selecao()

    elif pyautogui.locateOnScreen('game.png', confidence=0.8) != None:
        print('In game')

        keyboard.press('Space')
        keyboard.press('n')

        BotG.Loja()

        BotG.Andar()
        BotG.Andar()
        BotG.Andar()

        keyboard.press('q')
        keyboard.release('q')

        keyboard.press('Space')
        keyboard.press('n')
        BotG.Andar()
        BotG.Andar()

        keyboard.press('w')
        keyboard.release('w')

        keyboard.press('Space')
        keyboard.press('n')
        BotG.Andar()
        BotG.Andar()

        keyboard.press('e')
        keyboard.release('e')

        keyboard.press('Space')
        keyboard.press('n')
        
        BotG.Andar()
        BotG.Andar()

        keyboard.press('r')
        keyboard.release('r')



    elif pyautogui.locateOnScreen('jogar_novamente.png', confidence=0.8) != None:
        jogar_novamente = pyautogui.locateOnScreen('jogar_novamente.png', confidence=0.8)
        pyautogui.moveTo(jogar_novamente)
        mouse.click(Button.left, 1)
        time.sleep(1)

    elif pyautogui.locateOnScreen('diario.png', confidence=0.8) != None:
        diario = pyautogui.locateOnScreen('diario.png', confidence=0.8)
        pyautogui.moveTo(691,384)
        mouse.click(Button.left, 1)

        ok_diario = pyautogui.locateOnScreen('ok_diario.png', confidence=0.8)
        pyautogui.moveTo(ok_diario)
        mouse.click(Button.left, 1)

    elif pyautogui.locateOnScreen('ok.png', confidence=0.8) != None:
        ok = pyautogui.locateOnScreen('ok.png', confidence=0.8)
        pyautogui.moveTo(ok)
        mouse.click(Button.left, 1)

    elif pyautogui.locateOnScreen('erro.png', confidence=0.8) != None:
        erro = pyautogui.locateOnScreen('erro.png', confidence=0.8)
        pyautogui.moveTo(erro)
        mouse.click(Button.left, 1)

    elif keyboard.is_pressed('ç'):
        quit()

#qa
