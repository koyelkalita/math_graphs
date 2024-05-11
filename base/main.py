import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QAction, QMessageBox
from mpl_toolkits.mplot3d import Axes3D

class RiemannSheetWindow(QMainWindow):
    def __init__(self, function_name, function):
        super().__init__()
        self.setWindowTitle("Riemann Sheet")
        self.setGeometry(200, 200, 800, 600)
        self.function_name = function_name
        self.function = function
        self.plot_riemann_sheet()

    def plot_riemann_sheet(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y

        W = self.function(Z)

        ax.plot_surface(X, Y, np.real(W), cmap='viridis', edgecolor='none')
        ax.set_title("Riemann Sheet for function: " + self.function_name)
        ax.set_xlabel('Real part')
        ax.set_ylabel('Imaginary part')
        ax.set_zlabel('f(z)')
        plt.show()


class GraphWindow(QMainWindow):
    def __init__(self, function_name, function):
        super().__init__()
        self.setWindowTitle("Graph")
        self.setGeometry(200, 200, 800, 600)
        self.function_name = function_name
        self.function = function
        self.plot_graph()

    def plot_graph(self):
        x = np.linspace(-5, 5, 1000)
        y = self.function(x)
        plt.plot(x, y, color='blue')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title("Graph of function: " + self.function_name)
        plt.grid(True)
        plt.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mathematical Function Viewer")
        self.setGeometry(100, 100, 400, 100)

        self.input_label = QLabel("Enter Function:")
        self.input_text = QLineEdit()
        self.process_button = QPushButton("Process")

        self.input_label1 = QLabel("Enter Function:")
        self.input_text1 = QLineEdit()
        self.process_button1 = QPushButton("Process")

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.process_button)
        #button 2
        layout.addWidget(self.input_label1)
        layout.addWidget(self.input_text1)
        layout.addWidget(self.process_button1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.process_button.clicked.connect(self.process_function)

        self.init_menu()

    def init_menu(self):
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        help_menu = main_menu.addMenu('Help')

        open_file_action = QAction('Open File', self)
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        contribute_action = QAction('Contribute', self)
        contribute_action.triggered.connect(self.contribute)
        help_menu.addAction(contribute_action)

        about_action = QAction('About', self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def open_file(self):
        pass

    def contribute(self):
        QMessageBox.information(self, 'Contribute', 'You can contribute to this project on GitHub.')

    def about(self):
        QMessageBox.about(self, 'About', 'Mathematical Function Viewer\nVersion 1.0\nDeveloped by Md Rasel Mandol')

    def parse_function(self, function_str):
        try:
            function_parts = function_str.split('=')
            function_name = function_parts[0].strip()
            function_expr = function_parts[1].strip()
            return function_name, function_expr
        except Exception as e:
            print("Error parsing function:", e)
            return None, None

    def process_function(self):


        function_str1 = self.input_text1.text()
        function_str = self.input_text.text()
        function_name, function_expr = self.parse_function(function_str)
        function_name1,  function_expr1 = self.parse_function(function_str1)
        if function_expr:
            def function(x):
                z = x + 1j * x
                return eval(function_expr)
            
            riemann_window = RiemannSheetWindow(function_name, function)
            riemann_window.show()

            graph_window = GraphWindow(function_name, function)
            graph_window.show()

        if function_expr1:
            def function(x):
                z = x + 1j * x
                return eval(function_expr1)
            
            riemann_window = RiemannSheetWindow(function_name1, function)
            riemann_window.show()

            graph_window = GraphWindow(function_name, function)
            graph_window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window2  = MainWindow()
    window2.show()
    sys.exit(app.exec_())
