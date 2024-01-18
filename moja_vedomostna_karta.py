from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup
from random import *
class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.resize(800, 400)
main_win.setWindowTitle('Vedomostná karta')

main_win.total = 0
main_win.score = 0

questionl = QLabel('')
button = QPushButton('Start')



btnans1 = QRadioButton('')
btnans2 = QRadioButton('')
btnans3 = QRadioButton('')
btnans4 = QRadioButton('')


group = QButtonGroup()
group.addButton(btnans1)
group.addButton(btnans2)
group.addButton(btnans3)
group.addButton(btnans4)


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()


col1.addWidget(btnans1, Qt.AlignLeft)
col1.addWidget(btnans3, Qt.AlignLeft)

col2.addWidget(btnans2, Qt.AlignLeft)
col2.addWidget(btnans4, Qt.AlignLeft)

row.addLayout(col1)
row.addLayout(col2)
row.setSpacing(50)

groupBox = QGroupBox('Odpovede')
groupBox.setLayout(row)

ansbox = QGroupBox('Vysledky')
result = QLabel('Spravne')
ans = QLabel(btnans1.text())
row3 = QHBoxLayout()
row4 = QHBoxLayout()
col = QVBoxLayout()
row3.addWidget(result, Qt.AlignLeft)
row4.addWidget(ans, Qt.AlignRight)
col.addLayout(row3)
col.addLayout(row4)
ansbox.setLayout(col)


mainLayout = QVBoxLayout()
mainLayout.addWidget(questionl, Qt.AlignCenter)
mainLayout.addWidget(groupBox, Qt.AlignCenter)
mainLayout.addWidget(ansbox, Qt.AlignCenter)
mainLayout.addWidget(button, Qt.AlignCenter)

ansbox.hide()
groupBox.hide()

def show_result():
    groupBox.hide()
    ansbox.show()
    button.setText('Dalsia otazka')


def show_question():
    groupBox.show()
    ansbox.hide()
    button.setText('Vyhodnot')
    group.setExclusive(False)
    btnans1.setChecked(False)
    btnans2.setChecked(False)
    btnans3.setChecked(False)
    btnans4.setChecked(False)
    group.setExclusive(True)


def start_test():
    if button.text() == 'Vyhodnot':
        show_result()
        check()
    else:
        show_question()
        next_question()
btns = [btnans1, btnans2, btnans3, btnans4]
def ask(q: Question):
    questionl.setText(q.question)

    shuffle(btns)
    btns[0].setText(q.right)
    btns[1].setText(q.wrong1)
    btns[2].setText(q.wrong2)
    btns[3].setText(q.wrong3)

question_list=[
    Question('0!', '1', '0', '2', '3'),
    Question('1!', '1', '0', '2', '3'),
    Question('2!', '2', '1', '0', '3'),
    Question('3!', '6', '2', '1', '12'),
    Question('4!', '24', '12', '36', '6'),
    Question('5!', '120', '25', '125', '50'),
    Question('6!', '720', '360', '1000', '666'),
    Question('7!', '5040', '4900', '7090', '14000'),
    Question('8!', '40320', '80640', '20160', '16130'),
    Question('9!', '362880', '181440', '90720', '30240'),
    Question('10!', '3628800', '7257600', '4838400', '9676800')]


def check():
    if btns[0].isChecked():
        show_corect('Spravne')
        main_win.score+=1
    else:
        show_corect('Nespravne')

def show_corect(cor):
    result.setText(cor)
    ansbox.show()
    groupBox.hide()
    button.setText('Dalsia otazka')
def stats():
    print('Statistika')
    print('Spravne:    ' + str(main_win.score))
    print('Spolu:   ' + str(main_win.total))
    print('Uspesnost:   ' + str((main_win.score/main_win.total)*100) + '%')
cur_question = 0
done=[]
def next_question():
    cur_question=randint(0,len(question_list)-1)
    if cur_question in done:
        if len(done)==len(question_list):
            app.quit() 
            stats()           
        else:
            next_question()
    else:
        main_win.total+=1
        ask(question_list[cur_question])
        done.append(cur_question)
    

button.clicked.connect(start_test)
main_win.setLayout(mainLayout)
main_win.show()
app.exec_()