import pyautogui as gui
opcao = gui.confirm('Escolha uma opção: ', buttons =['Excel', 'Word', 'Chrome'])
gui.hotkey('win', 'r')
gui.sleep(1)
exe=opcao
if exe=='Word':
    exe='Winword'
gui.typewrite(exe+'.exe')
gui.press('Enter')
gui.sleep(2)
gui.click(x=284, y=185)
gui.sleep(2)
gui.typewrite(f' {opcao} foi aberto automáticamante')
#print(gui.position())