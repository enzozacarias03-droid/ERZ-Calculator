import sys
from main_window import MainWindow #Para importar doutros modulos
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button
from buttons import ButtonsGrid

"""
def temp_label(text):
    label1 = QLabel(text) #QLabel e para meter texto
    label1.setStyleSheet('font-size: 90px')
    return label1
"""
    
if __name__ == '__main__':
    #Cria a app
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow() #para a janela
    # snake_case
    #PascalCase
    #CamelCase

    #Definir Icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
   

    #Info
    info = Info('Your Account')
    window.addWidgetToVLayout(info)
  
    #Display
    display = Display()
    window.addWidgetToVLayout(display)

    #Grid
    buttonsGrid = ButtonsGrid(display, info, window )
    window.v_layout.addLayout(buttonsGrid)


    #Button
    #button = Button('Button text')
    """""
    buttonsGrid.addWidget(Button('0'), 0, 0) #os numeros                                     #sao o espaco
    buttonsGrid.addWidget(Button('1'), 0 , 1)#sao o lugar
    buttonsGrid.addWidget(Button('2'), 0 , 2)#na calc
    buttonsGrid.addWidget(Button('3'), 1 , 0, 1, 3)
                    #(row, colum, rowspan, columnspan)
""" 
   
    #   Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec() 