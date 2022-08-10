# -*- coding: utf-8 -*-
import tkinter as tk
from PyQt5.Qt import *
from ffffqlhelperUI import Ui_Program
# from tkinter import filedialog
import hahhelper
import glob


class MainWindow(QMainWindow, Ui_Program):
    def __init__(self):
        """Конструктор программы"""
        super(MainWindow, self).__init__()
        self.ui = Ui_Program()
        self.ui.setupUi(self)
        self.ui.items.setWidgetResizable(True)
        """Интерфейс"""
        #r'D:\Python Projects\python-hah-qlhelper\items data\Unfired TreePot.json'
        for elem in glob.glob(r'D:\Python Projects\python-hah-qlhelper\items data\*.json'):
            print(elem)
            parsed = hahhelper.ItemsParser(elem)
            self.add_clickable_widget(parsed)
            #for j in parsed.variables:
                #self.add_variable_widget((j, parsed.variables.get(j)), 'quality')

        #for i in range(5):
            #self.add_clickable_widget(parsed)
            #wid = hahhelper.CW()
            # wid2.name.setText('test')
            # wid2.qllabel.setText('stat')
            # img = QImage('resources/Laddies_Cap.png')
            # icon = QPixmap.fromImage(img)
            # wid.icnlabel.setPixmap(icon)
            # wid.name.setText(f"SampleText:index{i}")
            # wid.clickable_widget.mousePressEvent = lambda event: print('worked!')
            # self.ui.verticalLayout.addWidget(wid.clickable_widget)
            # self.ui.verticalLayout_2.addWidget(wid2.variables_widget)
            # self.ui.items.show()

    def add_clickable_widget(self, parsed):
        """Adds item widget to scrollarea"""
        widget = hahhelper.CW()
        widget.name.setText(parsed.name)  # Item name
        widget.clickable_widget.mousePressEvent = lambda event: print('worked!')
        widget.icnlabel.setPixmap(self.img_from_name(parsed.name))  # Item icon (Must be in items data .png file named like json)
        self.ui.verticalLayout.addWidget(widget.clickable_widget)  # Adds widget to scrollarea
        self.ui.items.show()  # Refreshes scrollarea

    def img_from_name(self, name):
        """Makes QPixmap object from item filename"""
        name = name.strip('.json')
        return QPixmap.fromImage(QImage(f'items data/{name}.png'))

    def add_variable_widget(self, variable, _type):
        """Adds variable widget to scrollarea"""
        widget = hahhelper.VW()
        widget.qllabel.setText(_type)
        widget.name.setText(variable[0])
        widget.enter.setText(str(variable[1]))
        self.ui.verticalLayout_2.addWidget(widget.variables_widget)  # Adds widget to scrollarea
        self.ui.items.show()  # Refreshes scrollarea



        # """Объект класса Tkinter для работы с filedialog"""
        # tkobject = tk.Tk()
        # tkobject.withdraw()
        # """Кнопки"""

    #     self.ui.browse.clicked.connect(lambda: self.browse())
    #     self.ui.save.clicked.connect(lambda: self.save_to())
    #     self.ui.convert.clicked.connect(lambda: self.make_gif())
    #     self.ui.localization.clicked.connect(lambda: self.switch())
    #     """Ползунки"""
    #     self.ui.frame_slider.setMinimum(1)
    #     self.ui.frame_slider.setMaximum(40)
    #     self.ui.frame_slider.valueChanged.connect(lambda: self.ui.frame_count.setText(str(self.ui.frame_slider.value()*10)))
    #     self.ui.compr_label.setMaximum(10)
    #     self.ui.compr_label.valueChanged.connect(lambda: self.ui.cmp_count.setText(str(self.ui.compr_label.value())))
    #     """Многозадачность"""
    #     self.process_thread = Thread()
    #     self.process_thread.finished.connect(self._finished)
    #
    def add_widget(self, x):
        pass
    # def browse(self):
    #     """Открыть filedialog для видео"""
    #     try:
    #         self.process_thread.video_path = filedialog.askopenfilename()
    #         self.ui.filePath.setText(self.process_thread.video_path)
    #         print(self.process_thread.video_path)
    #     except:
    #         self.ui.statusLabel.setText(self.errorMsg)
    #
    # def save_to(self):
    #     """Открыть filedialog для сохранения"""
    #     try:
    #         self.process_thread.save_path = filedialog.askdirectory()
    #         self.ui.savePath.setText(self.process_thread.save_path)
    #         print(self.process_thread.save_path)
    #     except:
    #         self.ui.statusLabel.setText(self.errorMsg)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
