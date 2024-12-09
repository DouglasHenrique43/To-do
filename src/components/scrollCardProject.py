# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerxzSHiz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 100)
        Form.setMaximumSize(QSize(360, 100))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bgCardProject = QFrame(Form)
        self.bgCardProject.setObjectName(u"bgCardProject")
        self.bgCardProject.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgCardProject.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bgCardProject)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.left = QFrame(self.bgCardProject)
        self.left.setObjectName(u"left")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left.sizePolicy().hasHeightForWidth())
        self.left.setSizePolicy(sizePolicy)
        self.left.setFrameShape(QFrame.Shape.StyledPanel)
        self.left.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.titleProject = QLabel(self.left)
        self.titleProject.setObjectName(u"titleProject")

        self.verticalLayout.addWidget(self.titleProject)

        self.category = QLabel(self.left)
        self.category.setObjectName(u"category")

        self.verticalLayout.addWidget(self.category)


        self.horizontalLayout_2.addWidget(self.left)

        self.right = QFrame(self.bgCardProject)
        self.right.setObjectName(u"right")
        self.right.setFrameShape(QFrame.Shape.StyledPanel)
        self.right.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.right)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.activeTasks = QLabel(self.right)
        self.activeTasks.setObjectName(u"activeTasks")

        self.horizontalLayout_3.addWidget(self.activeTasks)

        self.moreButton = QPushButton(self.right)
        self.moreButton.setObjectName(u"moreButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.moreButton.sizePolicy().hasHeightForWidth())
        self.moreButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/icons/more-vertical.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.moreButton.setIcon(icon)
        self.moreButton.setIconSize(QSize(18, 25))

        self.horizontalLayout_3.addWidget(self.moreButton)


        self.horizontalLayout_2.addWidget(self.right)


        self.horizontalLayout.addWidget(self.bgCardProject)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleProject.setText("")
        self.category.setText("")
        self.activeTasks.setText("")
        self.moreButton.setText("")
    # retranslateUi

