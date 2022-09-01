# -*- coding: utf-8 -*-
from PyQt5.Qt import *
from qlhelper_UI import Ui_Program
import hahhelper
import glob
import sys, os
import logging
import webbrowser


class MainWindow(QMainWindow, Ui_Program):
    def __init__(self):
        """Program initialization"""
        super(MainWindow, self).__init__()
        self.ui = Ui_Program()
        self.ui.setupUi(self)
        self.setWindowTitle("Haven and Hearth quality helper")
        self.setWindowIcon(QIcon('icon.ico'))
        self.ui.items.setWidgetResizable(True)
        self.add_clickables_from_list([elem for elem in glob.glob(r'items data\*.json')])
        self.ui.searchBtn.clicked.connect(lambda: self.sort_clickables_by_search())
        self.ui.addBtn.clicked.connect(lambda: self.update_clickables())
        self.ui.qualCountBtn.clicked.connect(lambda: self.count_and_set_result())
        self.ui.delBtn.hide()  # This button don't have any use rn
        self.VW_objs = []
        self.lastClickable = None
        """Logger"""
        logging.basicConfig(filename="Errors.log")

    def count_and_set_result(self):
        """Count result and set to quality label"""
        try:
            vars = self.get_vars_from_vw()
            self.lastClickable.variables = vars[0]
            self.lastClickable.stats = vars[1]
            self.ui.qualityLabel.setText(str(self.lastClickable.count_result()))
        except Exception:
            self.write_log()

    def get_vars_from_vw(self):
        variables = {}
        stats = {}
        for vw in self.VW_objs:
            if vw.qllabel.text() == 'quality':
                variables[vw.name.text()] = int(vw.enter.text())
            elif vw.qllabel.text() == 'stat':
                stats[vw.name.text()] = int(vw.enter.text())
        return variables, stats

    def update_clickables(self):
        """Updates clickables from path"""
        try:
            self.clear_clickable_layout()
            self.add_clickables_from_list([elem for elem in glob.glob(r'items data\*.json')])
        except Exception:
            self.write_log()

    def write_log(self):
        """Writes error log to log file"""
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logging.error(f"{exc_type}, {fname}, {exc_tb.tb_lineno}")

    def sort_clickables_by_search(self):
        """Sorts clickables by search where first clickable search.text"""
        try:
            if len(self.ui.searchBar.text()) > 0:
                elems = [elem for elem in glob.glob(r'items data\*.json')]
                if "all" in self.ui.searchBar.text().lower():
                    self.clear_clickable_layout()
                    self.add_clickables_from_list(elems)
                else:
                    self.clear_clickable_layout()
                    add_elems = []
                    for elem in elems:
                        if self.ui.searchBar.text().lower() in elem.lower():
                            add_elems.append(elem)
                    if len(add_elems) > 0:
                        self.add_clickables_from_list(add_elems)
        except Exception:
            self.write_log()

    def add_clickables_from_list(self, clickables, first_index=0):
        """Add clickables where top is first by index"""
        try:
            first_elem = clickables[first_index]
            elems = self.del_elem(clickables, first_elem)
            parsed = hahhelper.ItemsParser(first_elem)
            self.add_clickable_widget(parsed)
            for elem in elems:
                parsed = hahhelper.ItemsParser(elem)
                self.add_clickable_widget(parsed)
        except Exception:
            self.write_log()

    def del_elem(self, elems, elem):
        """Delete elem from elements list"""
        try:
            if len(elems) > 0:
                for x in elems:
                    if x == elem:
                        del elems[elems.index(x)]
                        return elems
        except Exception:
            self.write_log()

    def set_name_and_img(self, name):
        """Set name and img to wiki widget"""
        try:
            self.ui.namelbl.setText(str(name))
            self.ui.imglbl.setPixmap(self.img_from_name(name).scaled(121, 121))
        except Exception:
            self.write_log()

    def wiki_opener(self, wiki):
        """opens URL in browser"""
        try:
            webbrowser.open(wiki)
        except Exception:
            self.write_log()

    def widget_event(self, widget):
        """Adds widget, wiki widget and sets last clickable widget data"""
        try:
            self.VW_objs.clear()
            self.lastClickable = widget.data
            self.add_widgets_by_parsed(widget.data)
            self.set_name_and_img(widget.data.name)
            self.ui.wikiBtn.disconnect()
            self.ui.wikiBtn.clicked.connect(lambda: self.wiki_opener(widget.data.wiki))
        except Exception:
            self.write_log()

    def add_clickable_widget(self, parsed):
        """Adds item widget to scrollarea"""
        try:
            widget = hahhelper.CW(parsed)
            widget.name.setText(parsed.name)  # Item name
            widget.clickable_widget.mousePressEvent = lambda event: self.widget_event(widget)
            widget.icnlabel.setPixmap(self.img_from_name(parsed.name).scaled(51, 51))  # Item icon (Must be in items data .png file named like json)
            self.ui.verticalLayout.addWidget(widget.clickable_widget)  # Adds widget to scrollarea
            self.ui.items.show()  # Refreshes scrollarea
        except Exception:
            self.write_log()

    def img_from_name(self, name):
        """Makes QPixmap object from item filename"""
        try:
            name = name.strip('.json')
            return QPixmap.fromImage(QImage(f'items data/{name}.png'))
        except Exception:
            self.write_log()

    def add_variable_widget(self, variable, _type):
        """Adds variable widget to scrollarea"""
        try:
            widget = hahhelper.VW()
            widget._type = _type
            widget.qllabel.setText(_type)
            widget.name.setText(variable[0])
            widget.enter.setText(str(variable[1]))
            self.VW_objs.append(widget)
            self.ui.verticalLayout_2.addWidget(widget.variables_widget)  # Adds widget to scrollarea
            self.ui.items.show()  # Refreshes scrollarea
        except Exception:
            self.write_log()

    def add_widgets_by_parsed(self, parsed):
        """Adds all variable widgets to scrollarea from parsed"""
        try:
            self.clear_variable_layout()  # clear previous widgets
            for elem in parsed.variables:
                self.add_variable_widget((elem, parsed.variables.get(elem)), 'quality')
            for elem in parsed.stats:
                self.add_variable_widget((elem, parsed.stats.get(elem)), 'stat')
        except Exception:
            self.write_log()

    def clear_variable_layout(self):
        """Clears variable widget variables scrollarea"""
        try:
            for i in reversed(range(self.ui.verticalLayout_2.count())):
                if self.ui.verticalLayout_2.count() > 0:
                    self.ui.verticalLayout_2.itemAt(i).widget().setParent(None)
                else:
                    pass
        except Exception:
            self.write_log()

    def clear_clickable_layout(self):
        """Clears clickable widget variables scrollarea"""
        try:
            for i in reversed(range(self.ui.verticalLayout.count())):
                if self.ui.verticalLayout.count() > 0:
                    self.ui.verticalLayout.itemAt(i).widget().setParent(None)
                else:
                    pass
        except Exception:
            self.write_log()