# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QLineEdit

app = QApplication([])
window = QWidget()
window.setWindowTitle('Умные заметки')
window.resize(800, 600)

button1 = QPushButton('Создать заметку')
button2 = QPushButton('Удалить заметку')
button3 = QPushButton('Добавить в заметку')
button4 = QPushButton('Отменить заметку')
button5 = QPushButton('Искать заметку по тегу')
button6 = QPushButton('Сохранить заметку')
label1 = QLabel('Список заметок')
label2 = QLabel('Список тегов')

vige1 = QTextEdit()
vige2 = QListWidget()
vige3 = QListWidget()
vige4 = QLineEdit()

layout_main = QHBoxLayout()

layout_main.addWidget(vige1)
layoutH1 = QVBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layout_main.addLayout(layoutH1)
layoutH1.addWidget(label1)
layoutH1.addWidget(vige2)
layoutH1.addLayout(layoutH2)
layoutH2.addWidget(button1)
layoutH2.addWidget(button2)
layoutH1.addWidget(button6)
layoutH1.addWidget(label2)
layoutH1.addWidget(vige3)
layoutH1.addWidget(vige4)
layoutH1.addLayout(layoutH3)
layoutH3.addWidget(button3)
layoutH3.addWidget(button4)
layoutH1.addWidget(button5)



window.setLayout(layout_main)
window.show()
app.exec_() 