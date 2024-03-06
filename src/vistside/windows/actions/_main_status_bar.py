"""MainStatusBar provides the status bar for the main application window. """
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtWidgets import QStatusBar, QMainWindow, QLabel
from icecream import ic

from vistside.core import parseParent


class MainStatusBar(QStatusBar):
  """MainStatusBar provides the status bar for the main application
  window. """

  def __init__(self, *args, **kwargs) -> None:
    parent = parseParent(*args)
    QStatusBar.__init__(self, parent)

  def show(self) -> None:
    """Hook to print to stdout"""
    ic(self)
    QStatusBar.show(self, )

  @classmethod
  def getDefault(cls, mainWindow: QMainWindow) -> MainStatusBar:
    """Returns the default MainStatusBar"""
    ic()
    statusBar = cls(mainWindow)
    statusBar.addPermanentWidget(QLabel('LOL'))
    return statusBar
