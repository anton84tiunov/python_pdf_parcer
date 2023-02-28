import sys
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QPushButton

class someClass(QObject):
    
    someSignal = Signal()

    def __init__(self):
        super(someClass, self).__init__()
        
        self.someSignal.connect(self.print_msg)
        try:
            self.someSignal.emit()
        except Exception as e:
            print("__init__:")
            print(e)

    @Slot()			
    def print_msg(self):
        print("lalalu")
			

if __name__ == "__main__":
    app = QApplication(sys.argv)
		
    sc = someClass()
    button = QPushButton(text="Press me if you want to close the server")
    button.resize(640, 480)    
    button.setFont(QFont("Arial", 20, QFont.Bold))
    button.clicked.connect(button.close)
    button.show()

    sys.exit(app.exec_())
