"""FillWidget provides a widget with a fill color"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from vistside.core import BrushField
from vistside.widgets import BaseWidget


class FillWidget(BaseWidget):
  """FillWidget provides a widget with a fill color"""

  fillBrush = BrushField()

  def __init__(self, *args, **kwargs) -> None:
    BaseWidget.__init__(self, *args, **kwargs)
    self.fillBrush = 144, 0, 255, 255
