import pyautogui

pyautogui.press('win')
pyautogui.sleep(0.5)
pyautogui.write('Edge', interval = 0.1)
pyautogui.press('enter')
pyautogui.sleep(2)

pyautogui.write('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval = 0.1)
pyautogui.press('enter')
pyautogui.hotkey('win', 'up')

pyautogui.hotkey('printscreen')
pyautogui.sleep(2)
pyautogui.mouseDown(10,10)
pyautogui.sleep(0.5)
pyautogui.moveTo(1900, 1050)
pyautogui.sleep(2)
pyautogui.mouseUp()
