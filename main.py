# -*- coding: utf-8 -*-
import tkinter as tk
from PyQt5.Qt import *
from ffffqlhelperUI import Ui_Program
# from tkinter import filedialog
import hahhelper


class MainWindow(QMainWindow, Ui_Program):
    def __init__(self):
        """Конструктор программы"""
        super(MainWindow, self).__init__()
        self.ui = Ui_Program()
        self.ui.setupUi(self)
        self.ui.items.setWidgetResizable(True)
        """Интерфейс"""
        for i in range(5):
            wid = hahhelper.CW()
            wid2 = hahhelper.VW()
            wid2.name.setText('test')
            wid2.qllabel.setText('stat')
            img = QImage('resources/Laddies_Cap.png')
            icon = QPixmap.fromImage(img)
            wid.icnlabel.setPixmap(icon)
            wid.name.setText(f"SampleText:index{i}")
            wid.clickable_widget.mousePressEvent = lambda event: print('worked!')
            self.ui.verticalLayout.addWidget(wid.clickable_widget)
            self.ui.verticalLayout_2.addWidget(wid2.variables_widget)
            self.ui.items.show()
        """Объект класса Tkinter для работы с filedialog"""
        tkobject = tk.Tk()
        tkobject.withdraw()
        """Кнопки"""
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

