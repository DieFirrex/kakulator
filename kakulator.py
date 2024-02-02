from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QClipboard


app = QApplication([])
window = QWidget()

window.resize(300, 300)
window.move(460, 125)

text = QLineEdit()
text.setStyleSheet("background-color: #f0f0f0; color: #333; font-size: 16px; border: 2px solid #ccc; border-radius: 10px; padding: 8px;")

button1 = QPushButton('1')  
button1.setStyleSheet("background-color: #4CAF50; color: white; font-size: 20px; border-radius: 10px;")  
button2 = QPushButton('2')
button2.setStyleSheet("background-color: #008CBA; color: white; font-size: 20px; border-radius: 10px;")
button3 = QPushButton('3')
button3.setStyleSheet("background-color: #f44336; color: white; font-size: 20px; border-radius: 10px;")
button4 = QPushButton('4')
button4.setStyleSheet("background-color: #FFA500; color: white; font-size: 20px; border-radius: 10px;")
button5 = QPushButton('5')
button5.setStyleSheet("background-color: #9ACD32; color: white; font-size: 20px; border-radius: 10px;")
button6 = QPushButton('6')
button6.setStyleSheet("background-color: #FF69B4; color: white; font-size: 20px; border-radius: 10px;")
button7 = QPushButton('7')
button7.setStyleSheet("background-color: #FFD700; color: white; font-size: 20px; border-radius: 10px;")
button8 = QPushButton('8')
button8.setStyleSheet("background-color: #A52A2A; color: white; font-size: 20px; border-radius: 10px;")
button9 = QPushButton('9')
button9.setStyleSheet("background-color: #8A2BE2; color: white; font-size: 20px; border-radius: 10px;")
button10 = QPushButton('0')
button10.setStyleSheet("background-color: #FF4500; color: white; font-size: 20px; border-radius: 10px;")
button11 = QPushButton('+')
button11.setStyleSheet("background-color: #808080; color: white; font-size: 20px; border-radius: 10px;")
button12 = QPushButton('-')
button12.setStyleSheet("background-color: #708090; color: white; font-size: 20px; border-radius: 10px;")
button13 = QPushButton('*')
button13.setStyleSheet("background-color: #2E8B57; color: white; font-size: 20px; border-radius: 10px;")
button14 = QPushButton('/')
button14.setStyleSheet("background-color: #FF6347; color: white; font-size: 20px; border-radius: 10px;")
button15 = QPushButton('AC')
button15.setStyleSheet("background-color: #808080; color: white; font-size: 20px; border-radius: 10px;")
button16 = QPushButton('=')
button16.setStyleSheet("background-color: #808080; color: white; font-size: 20px; border-radius: 10px;")
button17 = QPushButton('.')
button17.setStyleSheet("background-color: #808080; color: white; font-size: 20px; border-radius: 10px;")
copy = QPushButton('Копіювати')
copy.setStyleSheet("background-color: #808080; color: white; font-size: 20px; border-radius: 10px;")

result = QLabel('Результат:')
result.setStyleSheet("color: #333; font-size: 20px; font-weight: bold;")
text2 = QLineEdit()
text2.setStyleSheet("background-color: #f0f0f0; color: #333; font-size: 18px; border: 2px solid #ccc; border-radius: 10px; padding: 8px;")

def wod_text():
    sender = window.sender()
    text.setText(text.text() + sender.text())

coxran = ''

def opera(op):
    global coxran
    coxran += text.text() + op
    text.clear()

def calcu():
    global coxran
    try:
        result = eval(coxran + text.text())
        text2.setText(str(result))
        coxran = ''
    except Exception as e:
        text2.setText('Помилка: ' + str(e))
    text.clear()

def copy_result():
    result = text2.text()
    clipboard = QApplication.clipboard()
    clipboard.setText(result)

button1.clicked.connect(wod_text)
button1.clicked.connect(wod_text)
button2.clicked.connect(wod_text)
button3.clicked.connect(wod_text)
button4.clicked.connect(wod_text)
button5.clicked.connect(wod_text)
button6.clicked.connect(wod_text)
button7.clicked.connect(wod_text)
button8.clicked.connect(wod_text)
button9.clicked.connect(wod_text)
button10.clicked.connect(wod_text)
button11.clicked.connect(lambda: opera('+'))
button12.clicked.connect(lambda: opera('-'))
button13.clicked.connect(lambda: opera('*'))
button14.clicked.connect(lambda: opera('/'))
button15.clicked.connect(text.clear)
button16.clicked.connect(calcu)
button17.clicked.connect(lambda: text.setText(text.text() + '.'))
copy.clicked.connect(copy_result)

h = QHBoxLayout()
h.addWidget(button1)
h.addWidget(button2)
h.addWidget(button3)
h.addWidget(button11)

h2 = QHBoxLayout()
h2.addWidget(button4)
h2.addWidget(button5)
h2.addWidget(button6)
h2.addWidget(button12)

h3 = QHBoxLayout()
h3.addWidget(button7)
h3.addWidget(button8)
h3.addWidget(button9)
h3.addWidget(button13)

h4 = QHBoxLayout()
h4.addWidget(button10)
h4.addWidget(button14)
h4.addWidget(button15)
h4.addWidget(button16)

h5 = QHBoxLayout()
h5.addWidget(button17)
h5.addWidget(copy)  

h6 = QHBoxLayout()
h6.addWidget(result)
h6.addWidget(text2)

v = QVBoxLayout()
v.addWidget(text)
v.addLayout(h)
v.addLayout(h2)
v.addLayout(h3)
v.addLayout(h4)
v.addLayout(h5)  
v.addLayout(h6)

window.setLayout(v)
window.show()
app.exec_()
