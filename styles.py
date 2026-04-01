import qdarkstyle
import qdarkstyle
from variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR, PRIMARY_COLOR)
from buttons import Button


qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: #fff;
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: #fff;
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: #fff;
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""



def setupTheme(app):
    qss = f"""
        QMainWindow {{
            background-color: #1e1e1e;
        }}
        
        QLineEdit {{
            background-color: #2b2b2b;
            color: white;
            font-size: 32px;
            border: 2px solid #444;
            border-radius: 8px;
            padding: 15px;
        }}
        
        QPushButton {{
            background-color: #3d3d3d;
            color: white;
            font-size: 20px;
            font-weight: bold;
            border: 1px solid #555;
            border-radius: 8px;
            min-height: 60px;
            padding: 10px;
        }}
        
        QPushButton:hover {{
            background-color: #4d4d4d;
        }}
        
        QPushButton:pressed {{
            background-color: #2d2d2d;
        }}
        
        QPushButton[cssClass="specialButton"] {{
            color: #fff;
            background: {PRIMARY_COLOR};
            border-radius: 5px;
        }}
        QPushButton[cssClass="specialButton"]:hover {{
            color: #fff;
            background: {DARKER_PRIMARY_COLOR};
        }}
        QPushButton[cssClass="specialButton"]:pressed {{
            color: #fff;
            background: {DARKEST_PRIMARY_COLOR};
        }}
    """
    
    app.setStyleSheet(qss)