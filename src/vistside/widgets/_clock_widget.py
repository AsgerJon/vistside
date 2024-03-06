"""ClockWidget provides a clock widget for the main application window"""
#  MIT Licence
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

from datetime import datetime

from vistutils.fields import IntField

from vistside.core import TimerField, Precise
from vistside.widgets import BaseWidget, LCDField


class ClockWidget(BaseWidget):
  """ClockWidget provides a clock widget for the main application window"""

  quartz = TimerField(100, Precise, singleShot=True)
  sevenSegment = LCDField(8, )
  prevTime = IntField(0, )

  @staticmethod
  def timeDict() -> dict[str, int]:
    """Returns a dictionary with the current time"""
    return {
      "hours"  : datetime.now().hour,
      "minutes": datetime.now().minute,
      "seconds": datetime.now().second,
    }

  def showTime(self, ) -> None:
    """Shows the current time"""
    timeDict = self.timeDict()
    h, m, s = timeDict['hours'], timeDict['minutes'], timeDict['seconds']
    if self.prevTime - s:
      self.sevenSegment.display(f'{h:02d}:{m:02d}:{s:02d}')
      self.prevTime = s
