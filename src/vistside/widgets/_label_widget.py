"""LabelWidget provides a widget for displaying labels. This is intended
for short names or descriptions rather than longer text."""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from PySide6.QtCore import QRect
from PySide6.QtGui import QColor, QPaintEvent, QPainter

from vistside.core import FontField, PenField, Black, SolidLine, \
  FontPenField, Yellow, WordWrap
from vistside.core import BrushField, Orange, SolidFill
from vistside.widgets import FillWidget
from vistutils.fields import TextField


class LabelWidget(FillWidget):
  """LabelWidget provides a widget for displaying labels. This is intended
  for short names or descriptions rather than longer text."""

  innerText = TextField('Label')
  textFont = FontField('Courier', 18)
  fillBrush = BrushField(Yellow, SolidFill)
  borderPen = PenField(QColor(144, 144, 255, 255), 2, SolidLine)

  def __init__(self, *args, **kwargs) -> None:
    """Initializes the LabelWidget."""
    FillWidget.__init__(self, *args, **kwargs)

  def paintEvent(self, event: QPaintEvent) -> None:
    """Paints the widget."""
    painter = QPainter()
    painter.begin(self)
    viewRect = painter.viewport()
    borderRect = viewRect.marginsRemoved(self.borderPen.width() * 2)
    borderRect.moveCenter(viewRect.center())
    textSpace = borderRect.marginsRemoved(4)
    painter.setRenderHint(QPainter.Antialiasing)
    #  fill background
    painter.setPen(self.emptyPen)
    painter.setBrush(self.fillBrush)
    painter.drawRect(viewRect)
    # # # # # # # # # # # # # # # # #
    #  draw border
    painter.setPen(self.borderPen)
    painter.setBrush(self.emptyBrush)
    painter.drawRect(borderRect)
    # # # # # # # # # # # # # # # # #
    #  Calculate required size for text
    painter.setFont(self.textFont)
    painter.setPen(self.textPen)
    textSize = painter.boundingRect(
      textSpace, WordWrap, self.innerText).size()
    textRect = QRect(textSpace.topLeft(), textSize)

    painter.setPen(self.emptyPen)
    painter.setBrush(self.fillBrush)
    painter.drawRoundedRect(self.rect(), 4, 4, )
    painter.setPen(self.borderPen)
    painter.setBrush(self.emptyBrush)
    painter.drawRoundedRect(self.rect(), 4, 4, )
    painter.setFont(self.textFont)
    painter.end()
