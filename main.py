import sys
from main_window import MainWindow #To import from other modules
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button
from buttons import ButtonsGrid


    
if __name__ == '__main__':
    #Creates the app
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow() #For the window
    # snake_case
    #PascalCase
    #CamelCase

    #Definining Icon
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

   
    #Executes everything
    window.adjustFixedSize()
    window.show()
    app.exec() 