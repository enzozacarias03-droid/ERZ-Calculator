from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QKeyEvent
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIDTH
from PySide6.QtCore import Qt, Signal
from useful import isEmpty, isNumDot



class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('>>>it works display.py')
        self.ConfigStyle()
        

    def ConfigStyle(self):
        margins = [TEXT_MARGIN for _ in range(4)]
        
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip() #strip removes spaces in the corners
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete, KEYS.Key_D]
        isEsc = key in [KEYS.Key_Escape, KEYS.Key_C]
        isOperator = key in [KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk, KEYS.Key_P]


        if isEnter :
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            self.delPressed.emit()
            return event.ignore()
        
        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            elif key == KEYS.Key_Plus:
                text = '+'
            elif key == KEYS.Key_Minus:
                text = '-'
            elif key == KEYS.Key_Slash:
                text = '/'
            elif key == KEYS.Key_Asterisk:
                text = "*"

            self.operatorPressed.emit(text)
            return event.ignore()
            
        
        #dont pass here without text

        if isEmpty(text):
            return event.ignore()
        
        if isNumDot(text):
        
            self.inputPressed.emit(text)
            return event.ignore()


        

        