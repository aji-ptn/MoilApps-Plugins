from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from enum import Enum


class Direction(Enum):
    Left = 0
    Right = 1
    Up = 2
    Down = 3


class Joystick(QLabel):
    def __init__(self, MainWindow):
        super(Joystick, self).__init__()
        self.parent = MainWindow
        self.setMinimumSize(100, 100)
        self.movingOffset = QPointF(0, 0)
        self.grabCenter = False
        self.__maxDistance = 50

    def paintEvent(self, event):
        painter = QPainter(self)
        bounds = QRectF(-self.__maxDistance, -self.__maxDistance, self.__maxDistance * 2,
                        self.__maxDistance * 2).translated(self._center())
        painter.drawEllipse(bounds)
        painter.setBrush(Qt.black)
        painter.drawEllipse(self._centerEllipse())

    def _centerEllipse(self):
        if self.grabCenter:
            return QRectF(-20, -20, 40, 40).translated(self.movingOffset)
        return QRectF(-20, -20, 40, 40).translated(self._center())

    def _center(self):
        return QPointF(10, 10)

    def _boundJoystick(self, point):
        limitLine = QLineF(self._center(), point)
        if limitLine.length() > self.__maxDistance:
            limitLine.setLength(self.__maxDistance)
        return limitLine.p2()

    def joystickDirection(self):
        if not self.grabCenter:
            return 0
        normVector = QLineF(self._center(), self.movingOffset)
        currentDistance = normVector.length()
        angle = normVector.angle()
        # print(normVector)
        # print(angle)
        # print(currentDistance)

        distance = min(currentDistance / self.__maxDistance, 1.0)
        if 45 <= angle < 135:
            return Direction.Up, distance
        elif 135 <= angle < 225:
            return Direction.Left, distance
        elif 225 <= angle < 315:
            return Direction.Down, distance
        return Direction.Right, distance

    def mousePressEvent(self, ev):
        self.grabCenter = self._centerEllipse().contains(ev.pos())
        return super().mousePressEvent(ev)

    def mouseReleaseEvent(self, event):
        self.grabCenter = False
        self.movingOffset = QPointF(0, 0)
        self.update()

    def mouseMoveEvent(self, event):
        if self.parent.image is not None:
            if self.grabCenter:
                self.movingOffset = self._boundJoystick(event.pos())
                self.update()
            pos_x = -(((self.width() - 40) - event.x()) - 100)
            pos_y = -(190 - event.y())
            ratio_x = round(self.parent.w/100)
            ratio_y = round(self.parent.h/100)
            delta_x = pos_x * ratio_x
            delta_y = pos_y * ratio_y

            if 0 <= pos_x <= 100 and 0 <= pos_y <= 100:
                self.parent.anypoint.alpha, self.parent.anypoint.beta = self.parent.moildev.get_alpha_beta(
                    delta_x, delta_y, self.parent.anypoint.anypointState)
                self.parent.anypoint.process_to_anypoint()

                print(pos_x * ratio_x)
                print(pos_y * ratio_y)
            else:
                pass
