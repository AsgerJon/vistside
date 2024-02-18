"""Main Tester Script"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations
import os
import sys

from icecream import ic

ic.configureOutput(includeContext=True)


def tester00() -> None:
  """Hello world"""
  items = [os, sys, 'hello world']
  for item in items:
    ic(item)


if __name__ == '__main__':
  tester00()
