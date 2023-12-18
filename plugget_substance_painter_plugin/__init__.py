import os
import substance_painter.ui
from PySide2 import QtWidgets, QtCore, QtGui


substance_ui_elements = []
widget = None


def show_widget():
    import plugget_qt
    global widget
    widget = plugget_qt.PluggetWidget()
    parent = substance_painter.ui.get_main_window()
    dock_widget = substance_painter.ui.add_dock_widget(widget)
    dock_widget.show()


def start_plugin():
    action = QtWidgets.QAction("Plugget", triggered=show_widget)
    substance_painter.ui.add_action(substance_painter.ui.ApplicationMenu.Window, action)
    substance_ui_elements.append(action)


def close_plugin():
    # Remove all widgets that have been added to the UI
    for widget in substance_ui_elements:
        substance_painter.ui.delete_ui_element(widget)
    substance_ui_elements.clear()


if __name__ == "__main__":
    start_plugin()
