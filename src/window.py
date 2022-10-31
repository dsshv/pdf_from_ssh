from xmlrpc import server
from PyQt5 import QtCore, QtWidgets
from matplotlib.pyplot import connect
from services.ssh_service import Connection

class Ui_MainWindow(object):
    # def __init__(self):
    #     self.add_functions()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 768))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.server_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.server_line_edit.setGeometry(QtCore.QRect(90, 40, 171, 41))
        self.server_line_edit.setObjectName("server_line_edit")

        self.server_label = QtWidgets.QLabel(self.centralwidget)
        self.server_label.setGeometry(QtCore.QRect(40, 40, 51, 41))
        self.server_label.setObjectName("server_label")

        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(280, 40, 71, 41))
        self.username_label.setObjectName("username_label")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(540, 40, 61, 41))
        self.password_label.setObjectName("password_label")

        self.username_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.username_line_edit.setGeometry(QtCore.QRect(350, 40, 171, 41))
        self.username_line_edit.setObjectName("username_line_edit")

        self.password_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.password_line_edit.setGeometry(QtCore.QRect(610, 40, 171, 41))
        self.password_line_edit.setObjectName("password_line_edit")

        self.connect_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_push_button.setGeometry(QtCore.QRect(850, 40, 151, 41))
        self.connect_push_button.setObjectName("connect_push_button")

        self.connected_label = QtWidgets.QLabel(self.centralwidget)
        self.connected_label.setGeometry(QtCore.QRect(40, 90, 321, 41))
        self.connected_label.setObjectName("connected_label")

        self.path_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.path_line_edit.setGeometry(QtCore.QRect(90, 170, 691, 41))
        self.path_line_edit.setObjectName("path_line_edit");
        self.path_line_edit.setEnabled(False)

        self.path_label = QtWidgets.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(40, 170, 51, 41))
        self.path_label.setObjectName("path_label")

        self.goto_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.goto_push_button.setGeometry(QtCore.QRect(850, 170, 151, 41))
        self.goto_push_button.setObjectName("goto_push_button")
        self.goto_push_button.setEnabled(False)

        self.folder_text_browser = QtWidgets.QTextEdit(self.centralwidget)
        self.folder_text_browser.setGeometry(QtCore.QRect(40, 260, 741, 460))
        self.folder_text_browser.setReadOnly(True)
        self.folder_text_browser.setObjectName("folder_text_browser")

        self.folder_label = QtWidgets.QLabel(self.centralwidget)
        self.folder_label.setGeometry(QtCore.QRect(40, 220, 741, 41))
        self.folder_label.setObjectName("folder_label")

        self.extentions_label = QtWidgets.QLabel(self.centralwidget)
        self.extentions_label.setGeometry(QtCore.QRect(860, 220, 181, 41))
        self.extentions_label.setObjectName("extentions_label")

        self.pdf_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.pdf_check_box.setGeometry(QtCore.QRect(850, 270, 121, 22))
        self.pdf_check_box.setObjectName("pdf_check_box")

        self.txt_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.txt_check_box.setGeometry(QtCore.QRect(850, 300, 121, 22))
        self.txt_check_box.setObjectName("txt_check_box")

        self.jpg_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.jpg_check_box.setGeometry(QtCore.QRect(850, 330, 121, 22))
        self.jpg_check_box.setObjectName("jpg_check_box")

        self.png_check_box = QtWidgets.QCheckBox(self.centralwidget)
        self.png_check_box.setGeometry(QtCore.QRect(850, 360, 121, 22))
        self.png_check_box.setObjectName("png_check_box")

        self.generate_push_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_push_button.setGeometry(QtCore.QRect(830, 670, 151, 41))
        self.generate_push_button.setObjectName("generate_push_button")
        self.generate_push_button.setEnabled(False)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connection = 'null'
        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdf_via_ssh"))
        self.server_line_edit.setText(_translate("MainWindow", "195.208.250.3"))
        self.server_label.setText(_translate("MainWindow", "Server:"))
        self.username_label.setText(_translate("MainWindow", "Username:"))
        self.password_label.setText(_translate("MainWindow", "Password:"))
        self.username_line_edit.setText(_translate("MainWindow", "student"))
        self.password_line_edit.setText(_translate("MainWindow", "Xanes2000"))
        self.connect_push_button.setText(_translate("MainWindow", "Connect"))

        self.connected_label.setText(_translate("MainWindow", ""))

        self.path_line_edit.setText(_translate("MainWindow", "~/home/student/"))
        self.path_label.setText(_translate("MainWindow", "Path:"))
        self.goto_push_button.setText(_translate("MainWindow", "Goto!"))
        self.folder_label.setText(_translate("MainWindow", "Files in {}:"))
        self.extentions_label.setText(_translate("MainWindow", "Extentions:"))
        self.pdf_check_box.setText(_translate("MainWindow", "*.pdf"))
        self.txt_check_box.setText(_translate("MainWindow", "*.txt"))
        self.jpg_check_box.setText(_translate("MainWindow", "*.jpg"))
        self.png_check_box.setText(_translate("MainWindow", "*.png"))
        self.generate_push_button.setText(_translate("MainWindow", "Generate PDF"))


    def add_functions(self):
        self.connect_push_button.clicked.connect(lambda: self.ssh_connection())
        self.goto_push_button.clicked.connect(lambda: self.show_path())

    def ssh_connection(self):
        server_connection = Connection(
            self.server_line_edit.text(),
            self.username_line_edit.text(),
            self.password_line_edit.text()
        )
        if (hasattr(server_connection, 'error')):
            print(server_connection.error)
            self.connected_label.setText(f"Error: {server_connection.error}")
            return

        print(server_connection)
        self.connected_label.setText(f"Connected to {server_connection.username}@{server_connection.hostname}")
        self.path_line_edit.setEnabled(True)
        self.goto_push_button.setEnabled(True)
        self.connection = server_connection

    def show_path(self):
        print(self.connection.hostname, self.connection.username, self.connection.password)
        ls = self.connection.exec(f'ls {self.path_line_edit.text()}')
        self.connection.connection.close()
        text = ''
        for record in ls:
            text += f'{record}\n'
        self.folder_text_browser.setText(text)