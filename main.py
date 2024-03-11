"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import os
import sys
from time import sleep

from PySide6.QtWidgets import QApplication
from icecream import ic

from vistside.core._data_roll import DataRoll
from vistside.windows import BaseWindow, LayoutWindow

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world"""
  items = [os, sys, 'hello world']
  for item in items:
    ic(item)


def tester01() -> None:
  """Hello world"""
  app = QApplication()
  main = LayoutWindow()
  main.show()
  app.exec()


def tester02() -> None:
  """Test DataRoll class if correctly rolls."""
  roll = DataRoll()
  for i in range(32):
    roll.append(float(i))
    print(roll)
    sleep(0.1)


if __name__ == '__main__':
  tester01()
