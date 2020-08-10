import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox)

class MainWindow(QWidget):
	def __init__(self):
		super().__init__()

	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
				QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
			print('Window closed')
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)

	demo = MainWindow()
	demo.show()

	sys.exit(app.exec_())