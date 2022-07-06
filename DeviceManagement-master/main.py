import login_ui
import sys
from PyQt5 import QtWidgets

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = login_ui.log_in()
    gui.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()


    