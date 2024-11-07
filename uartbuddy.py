from m5stack import *
from m5ui import *
from uiflow import *
import time


setScreenColor(0x333232)


contador = None
rolagem = None
log = None



title0 = M5Title(title="Title", x=3, fgcolor=0xFFFFFF, bgcolor=0xff3400)
label0 = M5TextBox(256, 224, "115200", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(170, 224, "TX", lcd.FONT_Default, 0xFFFFFF, rotate=0)

from numbers import Number



def buttonB_wasPressed():
  global contador, rolagem, log, uart2
  uart2.write('help'+"\r\n")
  label1.setColor(0xff6600)
  wait(1)
  label1.setColor(0xffffff)
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonC_wasPressed():
  global contador, rolagem, log, uart2
  if contador==1:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(9600, bits=8, parity=None, stop=1)
    contador = (contador if isinstance(contador, Number) else 0) + 1
    label0.setText('9600')
  elif contador==2:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(115200, bits=8, parity=None, stop=1)
    contador = (contador if isinstance(contador, Number) else 0) + 1
    label0.setText('115200')
  elif contador==3:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(230400, bits=8, parity=None, stop=1)
    contador = (contador if isinstance(contador, Number) else 0) + 1
    label0.setText('230400')
  elif contador==4:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(256000, bits=8, parity=None, stop=1)
    contador = (contador if isinstance(contador, Number) else 0) + 1
    label0.setText('256000')
  elif contador==5:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(512000, bits=8, parity=None, stop=1)
    contador = (contador if isinstance(contador, Number) else 0) + 1
    label0.setText('512000')
  elif contador==6:
    uart2 = machine.UART(2, tx=17, rx=16)
    uart2.init(921600, bits=8, parity=None, stop=1)
    contador = 1
    label0.setText('921600')
  else:
    pass
  pass
btnC.wasPressed(buttonC_wasPressed)


contador = 1
rolagem = 20
log = 'hello'
title0.setTitle(str((str('UART Buddy - bat lvl: ') + str(((str((power.getBatteryLevel())) + str('%')))))))
uart2 = machine.UART(2, tx=17, rx=16)
uart2.init(115200, bits=8, parity=None, stop=1)
while True:
  if uart2.any():
    log = (uart2.read()).decode()
    lcd.print(log, 0, rolagem, 0xffffff, rotate=0)
    with open('/sd/logUART.txt', 'w+') as fs:
      fs.write(str(log))
      fs.write('-')
    rolagem = (rolagem if isinstance(rolagem, Number) else 0) + 75
  if rolagem >= 200:
    rolagem = 20
    lcd.clear()
    lcd.fill(0x333333)
    title0.setBgColor(0xcc0000)
    title0.setTitle(str((str('UART Buddy - bat lvl: ') + str(((str((power.getBatteryLevel())) + str('%')))))))
  wait_ms(2)
