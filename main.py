"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import os
import sys

from PySide6.QtWidgets import QApplication
from icecream import ic

from vistside.windows import BaseWindow

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world"""
  items = [os, sys, 'hello world']
  for item in items:
    ic(item)


def tester01() -> None:
  """Hello world"""
  app = QApplication()
  main = BaseWindow()
  main.show()
  app.exec()


if __name__ == '__main__':
  tester01()
