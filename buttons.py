from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from useful import isNumDot, isEmpty, isValidNum, converToNumber
from display import Display
import math

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()


    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setItalic(True)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 85)
        
        


class ButtonsGrid(QGridLayout):
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow',
                  *args,**kwargs) -> None:
        super().__init__(*args, **kwargs)
 
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2','3','+'],
            ['N', '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'your calculat'
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    

    def _makeGrid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)


                if button_text not in '0123456789.':
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
 
                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._insertToDisplay,button.text())
                self._connectButtonClicked(button, slot)
              

    def _connectButtonClicked(self, button, slot):
          button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        text = button.text()

        if text == 'C':
            self._connectButtonClicked(button, self._clear)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNum)

        if text == 'D':
            self._connectButtonClicked(button, self.display.backspace) 

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                     self._makeSlot(self._configLeftOp, button.text())
            )
         

        if text == '=':
            self._connectButtonClicked(button, self._eq)

         
         
         
         
    @Slot()            
    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(checked):
            func( *args,** kwargs)
        return realSlot
    
    @Slot()
    def _invertNum(self):
        displayText = self.display.text()

        if not isValidNum(displayText):
            return
        
        number = converToNumber(displayText) * - 1
        self.display.setText(str(number))

      


    @Slot()
    def _insertToDisplay(self, text):
        newDisplay = self.display.text() + text

        if not isValidNum(newDisplay):
            return
        
        self.display.insert(text)
        self.display.setFocus()
        

    @Slot()
    def _clear(self):
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()
    
    @Slot()
    def _configLeftOp(self, text):
        displayText = self.display.text() # numero left
        self.display.clear() #limpa o display
        self.display.setFocus()
        
        #Se a pessoa clicou no operador sem
        #configurar qualquer numero
        if not isValidNum(displayText) and self._left is None:
            self._showError('You did not type a number')
            return
        
        #Se houver algo no numero da esquerda
        #nao se faz nada, so aguardamos numero d direita
        if self._left is None:
            self._left = converToNumber(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'
    
    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNum(displayText) or self._left is None:
            self._showError('Incomplete calculation: You did not type the other number')
            return
        
        self._right = converToNumber(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, (int , float)):
                result = math.pow(self._left, self._right)
                result = converToNumber(str(result))
            else:
                result = eval(self.equation)
                
            #eval avalia uma string cmo codigo python
        except ZeroDivisionError:
            self._showError('You are dividing by zero')
        except OverflowError:
            self._showError('This calculation cannot be done due to the lenght')
        
        self.display.clear()
        self.info.setText(f'{self.equation } = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
         self._left = None

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()


    def _makeDialogue(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox



    def _showError(self, text):
        msgBox = self._makeDialogue(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialogue(text)
        msgBox.setInformativeText('Trademark, all rights are reserved to Zac Technologies a subsidiary of Zac Group')
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()

       


        



  
