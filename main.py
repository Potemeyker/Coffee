import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QFormLayout, QLabel, QLineEdit, QPushButton
import sqlite3


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None):
        super(AddEditCoffeeForm, self).__init__(parent)
        loadUi('addEditCoffeeForm.ui', self)
        self.setWindowTitle('Add/Edit Coffee')

        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        name = self.name_input.text()
        roast_level = self.roast_input.text()
        grind = self.grind_input.text()
        taste_description = self.taste_input.text()
        price = float(self.price_input.text())
        volume = int(self.volume_input.text())

        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO coffee (name, roast_level, grind, taste_description, price, package_volume) "
                       "VALUES (?, ?, ?, ?, ?, ?)", (name, roast_level, grind, taste_description, price, volume))

        connection.commit()
        connection.close()
        self.accept()


class CoffeeApp(QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        loadUi('main.ui', self)
        self.load_data()

        self.addButton.clicked.connect(self.open_add_edit_form)

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        data = cursor.fetchall()
        connection.close()

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)

    def open_add_edit_form(self):
        form = AddEditCoffeeForm(self)
        if form.exec_() == QDialog.Accepted:
            self.load_data()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CoffeeApp()
    main_window.show()
    sys.exit(app.exec_())
