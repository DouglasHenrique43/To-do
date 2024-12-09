# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AppjPhhaf.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1107, 692)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-repeat: no-repeat;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bgApp = QFrame(self.centralwidget)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setFrameShape(QFrame.Shape.StyledPanel)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bgApp)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuBg.sizePolicy().hasHeightForWidth())
        self.leftMenuBg.setSizePolicy(sizePolicy)
        self.leftMenuBg.setMinimumSize(QSize(0, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(12)
        font.setWeight(QFont.Thin)
        font.setItalic(False)
        self.titleLeftApp.setFont(font)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftDescription.setFont(font1)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_13.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setStyleSheet(u"")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.toggleButton.setFont(font2)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/icons/icon_menu.png)")
        self.toggleButton.setIconSize(QSize(20, 20))

        self.verticalLayout_14.addWidget(self.toggleButton)


        self.verticalLayout_2.addWidget(self.toggleBox)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.topMenu)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.homeButton = QPushButton(self.topMenu)
        self.homeButton.setObjectName(u"homeButton")
        sizePolicy1.setHeightForWidth(self.homeButton.sizePolicy().hasHeightForWidth())
        self.homeButton.setSizePolicy(sizePolicy1)
        self.homeButton.setMinimumSize(QSize(0, 45))
        self.homeButton.setFont(font2)
        self.homeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.homeButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.homeButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-home.png);")

        self.verticalLayout_15.addWidget(self.homeButton)

        self.socialButton = QPushButton(self.topMenu)
        self.socialButton.setObjectName(u"socialButton")
        sizePolicy1.setHeightForWidth(self.socialButton.sizePolicy().hasHeightForWidth())
        self.socialButton.setSizePolicy(sizePolicy1)
        self.socialButton.setMinimumSize(QSize(0, 45))
        self.socialButton.setFont(font2)
        self.socialButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.socialButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.socialButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-chart.png);")

        self.verticalLayout_15.addWidget(self.socialButton)

        self.projectButton = QPushButton(self.topMenu)
        self.projectButton.setObjectName(u"projectButton")
        sizePolicy1.setHeightForWidth(self.projectButton.sizePolicy().hasHeightForWidth())
        self.projectButton.setSizePolicy(sizePolicy1)
        self.projectButton.setMinimumSize(QSize(0, 45))
        self.projectButton.setFont(font2)
        self.projectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.projectButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.projectButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-briefcase.png);")

        self.verticalLayout_15.addWidget(self.projectButton)

        self.taskButton = QPushButton(self.topMenu)
        self.taskButton.setObjectName(u"taskButton")
        sizePolicy1.setHeightForWidth(self.taskButton.sizePolicy().hasHeightForWidth())
        self.taskButton.setSizePolicy(sizePolicy1)
        self.taskButton.setMinimumSize(QSize(0, 45))
        self.taskButton.setFont(font2)
        self.taskButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.taskButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.taskButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-clipboard.png);")

        self.verticalLayout_15.addWidget(self.taskButton)

        self.calendarButton = QPushButton(self.topMenu)
        self.calendarButton.setObjectName(u"calendarButton")
        sizePolicy1.setHeightForWidth(self.calendarButton.sizePolicy().hasHeightForWidth())
        self.calendarButton.setSizePolicy(sizePolicy1)
        self.calendarButton.setMinimumSize(QSize(0, 45))
        self.calendarButton.setFont(font2)
        self.calendarButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.calendarButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.calendarButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-browser.png);")

        self.verticalLayout_15.addWidget(self.calendarButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.bottomMenuButtons = QFrame(self.bottomMenu)
        self.bottomMenuButtons.setObjectName(u"bottomMenuButtons")
        self.bottomMenuButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomMenuButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.bottomMenuButtons)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.profileButton = QPushButton(self.bottomMenuButtons)
        self.profileButton.setObjectName(u"profileButton")
        sizePolicy1.setHeightForWidth(self.profileButton.sizePolicy().hasHeightForWidth())
        self.profileButton.setSizePolicy(sizePolicy1)
        self.profileButton.setMinimumSize(QSize(0, 45))
        self.profileButton.setFont(font2)
        self.profileButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.profileButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profileButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-user.png);")

        self.verticalLayout.addWidget(self.profileButton)


        self.verticalLayout_3.addWidget(self.bottomMenuButtons)

        self.settingsButton = QPushButton(self.bottomMenu)
        self.settingsButton.setObjectName(u"settingsButton")
        sizePolicy1.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
        self.settingsButton.setSizePolicy(sizePolicy1)
        self.settingsButton.setMinimumSize(QSize(0, 45))
        self.settingsButton.setFont(font2)
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.settingsButton.setStyleSheet(u"background-image: url(:/icons/icons/cil-settings.png);")

        self.verticalLayout_3.addWidget(self.settingsButton)


        self.verticalLayout_2.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_13.addWidget(self.leftMenuFrame)


        self.horizontalLayout_3.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout_2 = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout_2.setSpacing(0)
        self.extraColumLayout_2.setObjectName(u"extraColumLayout_2")
        self.extraColumLayout_2.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"background-image: url(:/icons/icons/cil-code.png);")
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.extraCloseColumnBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/chevrons-left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(18, 18))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_6.addLayout(self.extraTopLayout)


        self.extraColumLayout_2.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.extraContent)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font2)
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/icons/cil-share-boxed.png);")

        self.verticalLayout_28.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font2)
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/icons/cil-equalizer.png);")

        self.verticalLayout_28.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font2)
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/icons/cil-layers.png);")

        self.verticalLayout_28.addWidget(self.btn_more)


        self.verticalLayout_16.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_29.addWidget(self.textEdit)


        self.verticalLayout_16.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_16.addWidget(self.extraBottom)


        self.extraColumLayout_2.addWidget(self.extraContent)


        self.horizontalLayout_3.addWidget(self.extraLeftBox)

        self.content = QWidget(self.bgApp)
        self.content.setObjectName(u"content")
        self.content.setMinimumSize(QSize(31, 0))
        self.content.setStyleSheet(u"")
        self.horizontalLayout_26 = QHBoxLayout(self.content)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.contentBox = QFrame(self.content)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setStyleSheet(u"")
        self.contentBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.contentBox)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.LeftBox = QFrame(self.contentTopBg)
        self.LeftBox.setObjectName(u"LeftBox")
        self.LeftBox.setFrameShape(QFrame.Shape.StyledPanel)
        self.LeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.LeftBox)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.notificationButton = QPushButton(self.LeftBox)
        self.notificationButton.setObjectName(u"notificationButton")
        self.notificationButton.setMinimumSize(QSize(28, 28))
        self.notificationButton.setMaximumSize(QSize(28, 28))
        self.notificationButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/MaterialSymbolsNotifications.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notificationButton.setIcon(icon1)
        self.notificationButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.notificationButton)

        self.themeButton = QPushButton(self.LeftBox)
        self.themeButton.setObjectName(u"themeButton")
        self.themeButton.setMinimumSize(QSize(28, 28))
        self.themeButton.setMaximumSize(QSize(28, 28))
        self.themeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/BxsPalette.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.themeButton.setIcon(icon2)
        self.themeButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_13.addWidget(self.themeButton)


        self.horizontalLayout_5.addWidget(self.LeftBox, 0, Qt.AlignmentFlag.AlignLeft)

        self.titleRightInfo = QFrame(self.contentTopBg)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleRightInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.titleRightInfo)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")

        self.horizontalLayout_5.addWidget(self.titleRightInfo)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/UiwSetting.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon3)
        self.settingsTopBtn.setIconSize(QSize(14, 14))

        self.horizontalLayout_17.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon4)
        self.minimizeAppBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_17.addWidget(self.minimizeAppBtn)

        self.max_resizeButton = QPushButton(self.rightButtons)
        self.max_resizeButton.setObjectName(u"max_resizeButton")
        self.max_resizeButton.setMinimumSize(QSize(28, 28))
        self.max_resizeButton.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.max_resizeButton.setFont(font3)
        self.max_resizeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/FluentMaximize20Filled.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.max_resizeButton.setIcon(icon5)
        self.max_resizeButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_17.addWidget(self.max_resizeButton)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeAppBtn.setIcon(icon6)
        self.closeAppBtn.setIconSize(QSize(16, 16))

        self.horizontalLayout_17.addWidget(self.closeAppBtn)


        self.horizontalLayout_5.addWidget(self.rightButtons, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_27.addWidget(self.contentTopBg)

        self.contentStacked = QFrame(self.contentBox)
        self.contentStacked.setObjectName(u"contentStacked")
        self.contentStacked.setFrameShape(QFrame.Shape.StyledPanel)
        self.contentStacked.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentStacked)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentStacked)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"background-position: center;\n"
"background-repeat: no-repeat;\n"
"background-image: url(:/images/images/PyDracula_vertical.png);")
        self.stackedWidget.addWidget(self.homePage)
        self.dashboardPage = QWidget()
        self.dashboardPage.setObjectName(u"dashboardPage")
        self.dashboardPage.setStyleSheet(u"")
        self.horizontalLayout_19 = QHBoxLayout(self.dashboardPage)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.mainContentHome = QFrame(self.dashboardPage)
        self.mainContentHome.setObjectName(u"mainContentHome")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mainContentHome.sizePolicy().hasHeightForWidth())
        self.mainContentHome.setSizePolicy(sizePolicy3)
        self.mainContentHome.setStyleSheet(u"#mainContentHome {\n"
"	padding: 30px;\n"
"\n"
"}")
        self.mainContentHome.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainContentHome.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.mainContentHome)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.mainContentHome)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.tasksLabel = QLabel(self.frame_15)
        self.tasksLabel.setObjectName(u"tasksLabel")

        self.verticalLayout_20.addWidget(self.tasksLabel)

        self.tasksArea = QScrollArea(self.frame_15)
        self.tasksArea.setObjectName(u"tasksArea")
        self.tasksArea.setStyleSheet(u"QFrame {\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton {\n"
"	background-color: transparent;\n"
"}")
        self.tasksArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tasksArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 169, 212))
        self.verticalLayout_21 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"#frame_11 {\n"
"    background-color: rgb(255, 96, 99); /* Fundo s\u00f3lido */\n"
"    border-radius: 5px;\n"
"    border: solid 3px rgb(255, 0, 4); /* Borda destacada */\n"
"}\n"
"")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_20.addWidget(self.label_5)

        self.pushButton_5 = QPushButton(self.frame_16)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/MingcuteDownFill.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon7)

        self.horizontalLayout_20.addWidget(self.pushButton_5)


        self.verticalLayout_21.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_21.addWidget(self.label_6)

        self.pushButton_6 = QPushButton(self.frame_17)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon7)

        self.horizontalLayout_21.addWidget(self.pushButton_6)


        self.verticalLayout_21.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_7 = QLabel(self.frame_18)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_22.addWidget(self.label_7)

        self.pushButton_7 = QPushButton(self.frame_18)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon7)

        self.horizontalLayout_22.addWidget(self.pushButton_7)


        self.verticalLayout_21.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_23.addWidget(self.label_8)

        self.pushButton_8 = QPushButton(self.frame_19)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon7)

        self.horizontalLayout_23.addWidget(self.pushButton_8)


        self.verticalLayout_21.addWidget(self.frame_19)

        self.tasksArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_20.addWidget(self.tasksArea)


        self.verticalLayout_19.addWidget(self.frame_15)

        self.frame_20 = QFrame(self.mainContentHome)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy4)
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_19.addWidget(self.frame_20)


        self.horizontalLayout_19.addWidget(self.mainContentHome)

        self.frame_21 = QFrame(self.dashboardPage)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_21)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.OverviewFrame = QFrame(self.frame_21)
        self.OverviewFrame.setObjectName(u"OverviewFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.OverviewFrame.sizePolicy().hasHeightForWidth())
        self.OverviewFrame.setSizePolicy(sizePolicy5)
        self.OverviewFrame.setMaximumSize(QSize(16777215, 16777215))
        self.OverviewFrame.setStyleSheet(u"#OverviewFrame {\n"
"	padding:  20px;\n"
"	border-radius: 6px;\n"
"	background-color: rgba(16, 19, 24, 0.7);\n"
"}\n"
"QFrame {\n"
"	background-color: transparent;\n"
"}")
        self.OverviewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.OverviewFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.OverviewFrame)
        self.verticalLayout_23.setSpacing(9)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.OverviewFrame)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setStyleSheet(u"QPushButton {\n"
"	width: 25px;\n"
"	height: 25px;\n"
"	border-radius: 12%;\n"
"}")
        self.frame_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_24.setSpacing(11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.monthLabel = QLabel(self.frame_22)
        self.monthLabel.setObjectName(u"monthLabel")

        self.horizontalLayout_24.addWidget(self.monthLabel)

        self.dayLabel = QLabel(self.frame_22)
        self.dayLabel.setObjectName(u"dayLabel")

        self.horizontalLayout_24.addWidget(self.dayLabel)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_4)


        self.verticalLayout_23.addWidget(self.frame_22)

        self.canvasCalendar = QFrame(self.OverviewFrame)
        self.canvasCalendar.setObjectName(u"canvasCalendar")
        self.canvasCalendar.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgba(255, 89, 97, 0.5);\n"
"}")
        self.canvasCalendar.setFrameShape(QFrame.Shape.StyledPanel)
        self.canvasCalendar.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_23.addWidget(self.canvasCalendar)


        self.verticalLayout_22.addWidget(self.OverviewFrame)

        self.ActiveLogFrame = QFrame(self.frame_21)
        self.ActiveLogFrame.setObjectName(u"ActiveLogFrame")
        self.ActiveLogFrame.setStyleSheet(u"#ActiveLogFrame {\n"
"	padding: 30px;\n"
"	border-radius: 6px;\n"
"	background-color: rgba(16, 19, 24, 0.7);\n"
"}")
        self.ActiveLogFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ActiveLogFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.ActiveLogFrame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.ActiveLogFrame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"QFrame {\n"
"	background-color: transparent\n"
"}")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_23)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.ActiveLogTitle = QLabel(self.frame_23)
        self.ActiveLogTitle.setObjectName(u"ActiveLogTitle")
        self.ActiveLogTitle.setStyleSheet(u"")
        self.ActiveLogTitle.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.ActiveLogTitle)


        self.verticalLayout_24.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.ActiveLogFrame)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy4.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy4)
        self.frame_24.setStyleSheet(u"QFrame {\n"
"	background-color: transparent\n"
"}")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setStyleSheet(u"")
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_25)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.dataLog = QLabel(self.frame_25)
        self.dataLog.setObjectName(u"dataLog")

        self.verticalLayout_26.addWidget(self.dataLog)


        self.horizontalLayout_25.addWidget(self.frame_25)

        self.logMessage = QFrame(self.frame_24)
        self.logMessage.setObjectName(u"logMessage")
        self.logMessage.setFrameShape(QFrame.Shape.StyledPanel)
        self.logMessage.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_25.addWidget(self.logMessage)


        self.verticalLayout_24.addWidget(self.frame_24)


        self.verticalLayout_22.addWidget(self.ActiveLogFrame)


        self.horizontalLayout_19.addWidget(self.frame_21, 0, Qt.AlignmentFlag.AlignRight)

        self.stackedWidget.addWidget(self.dashboardPage)
        self.socialPage = QWidget()
        self.socialPage.setObjectName(u"socialPage")
        self.verticalLayout_38 = QVBoxLayout(self.socialPage)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_13 = QLabel(self.socialPage)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_38.addWidget(self.label_13)

        self.stackedWidget.addWidget(self.socialPage)
        self.projectPage = QWidget()
        self.projectPage.setObjectName(u"projectPage")
        self.horizontalLayout_4 = QHBoxLayout(self.projectPage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.projectLeftContent = QFrame(self.projectPage)
        self.projectLeftContent.setObjectName(u"projectLeftContent")
        sizePolicy2.setHeightForWidth(self.projectLeftContent.sizePolicy().hasHeightForWidth())
        self.projectLeftContent.setSizePolicy(sizePolicy2)
        self.projectLeftContent.setMaximumSize(QSize(400, 16777215))
        self.projectLeftContent.setStyleSheet(u"")
        self.projectLeftContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectLeftContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.projectLeftContent)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.searchBarFrame = QFrame(self.projectLeftContent)
        self.searchBarFrame.setObjectName(u"searchBarFrame")
        self.searchBarFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.searchBarFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.searchBarFrame)
        self.horizontalLayout_6.setSpacing(7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.searchProjectsButton = QPushButton(self.searchBarFrame)
        self.searchProjectsButton.setObjectName(u"searchProjectsButton")
        self.searchProjectsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchProjectsButton.setStyleSheet(u"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchProjectsButton.setIcon(icon8)
        self.searchProjectsButton.setIconSize(QSize(15, 15))

        self.horizontalLayout_6.addWidget(self.searchProjectsButton)

        self.searchProjectsLineEdit = QLineEdit(self.searchBarFrame)
        self.searchProjectsLineEdit.setObjectName(u"searchProjectsLineEdit")
        sizePolicy1.setHeightForWidth(self.searchProjectsLineEdit.sizePolicy().hasHeightForWidth())
        self.searchProjectsLineEdit.setSizePolicy(sizePolicy1)
        self.searchProjectsLineEdit.setMinimumSize(QSize(0, 23))
        self.searchProjectsLineEdit.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.searchProjectsLineEdit)


        self.verticalLayout_4.addWidget(self.searchBarFrame)

        self.frame_2 = QFrame(self.projectLeftContent)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 148))
        self.frame_2.setBaseSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titleProjectsFrame = QFrame(self.frame_2)
        self.titleProjectsFrame.setObjectName(u"titleProjectsFrame")
        sizePolicy2.setHeightForWidth(self.titleProjectsFrame.sizePolicy().hasHeightForWidth())
        self.titleProjectsFrame.setSizePolicy(sizePolicy2)
        self.titleProjectsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.titleProjectsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.titleProjectsFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(25, 20, 15, 34)
        self.ProjectsTitle = QLabel(self.titleProjectsFrame)
        self.ProjectsTitle.setObjectName(u"ProjectsTitle")

        self.horizontalLayout_7.addWidget(self.ProjectsTitle)

        self.addCategoryProjectButton = QPushButton(self.titleProjectsFrame)
        self.addCategoryProjectButton.setObjectName(u"addCategoryProjectButton")
        self.addCategoryProjectButton.setMinimumSize(QSize(0, 0))
        self.addCategoryProjectButton.setMaximumSize(QSize(40, 40))
        self.addCategoryProjectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/TablerPlus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addCategoryProjectButton.setIcon(icon9)
        self.addCategoryProjectButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.addCategoryProjectButton)

        self.settingsCategoryProjects = QPushButton(self.titleProjectsFrame)
        self.settingsCategoryProjects.setObjectName(u"settingsCategoryProjects")
        self.settingsCategoryProjects.setMinimumSize(QSize(0, 0))
        self.settingsCategoryProjects.setMaximumSize(QSize(20, 40))
        self.settingsCategoryProjects.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/more-vertical.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsCategoryProjects.setIcon(icon10)
        self.settingsCategoryProjects.setIconSize(QSize(16, 16))

        self.horizontalLayout_7.addWidget(self.settingsCategoryProjects)


        self.verticalLayout_5.addWidget(self.titleProjectsFrame)

        self.navProjectsFrame = QFrame(self.frame_2)
        self.navProjectsFrame.setObjectName(u"navProjectsFrame")
        sizePolicy4.setHeightForWidth(self.navProjectsFrame.sizePolicy().hasHeightForWidth())
        self.navProjectsFrame.setSizePolicy(sizePolicy4)
        self.navProjectsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.navProjectsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.navProjectsFrame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.allProjectsButton = QPushButton(self.navProjectsFrame)
        self.allProjectsButton.setObjectName(u"allProjectsButton")
        sizePolicy3.setHeightForWidth(self.allProjectsButton.sizePolicy().hasHeightForWidth())
        self.allProjectsButton.setSizePolicy(sizePolicy3)
        self.allProjectsButton.setMaximumSize(QSize(150, 100))
        self.allProjectsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.allProjectsButton)

        self.openProjectsButton = QPushButton(self.navProjectsFrame)
        self.openProjectsButton.setObjectName(u"openProjectsButton")
        sizePolicy3.setHeightForWidth(self.openProjectsButton.sizePolicy().hasHeightForWidth())
        self.openProjectsButton.setSizePolicy(sizePolicy3)
        self.openProjectsButton.setMaximumSize(QSize(150, 100))
        self.openProjectsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.openProjectsButton)

        self.closedProjectsButton = QPushButton(self.navProjectsFrame)
        self.closedProjectsButton.setObjectName(u"closedProjectsButton")
        sizePolicy3.setHeightForWidth(self.closedProjectsButton.sizePolicy().hasHeightForWidth())
        self.closedProjectsButton.setSizePolicy(sizePolicy3)
        self.closedProjectsButton.setMaximumSize(QSize(150, 100))
        self.closedProjectsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_9.addWidget(self.closedProjectsButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.navProjectsFrame)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.projectScrollArea = QScrollArea(self.projectLeftContent)
        self.projectScrollArea.setObjectName(u"projectScrollArea")
        sizePolicy4.setHeightForWidth(self.projectScrollArea.sizePolicy().hasHeightForWidth())
        self.projectScrollArea.setSizePolicy(sizePolicy4)
        self.projectScrollArea.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        self.projectScrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.projectScrollArea.setWidgetResizable(True)
        self.projectScrollContent = QWidget()
        self.projectScrollContent.setObjectName(u"projectScrollContent")
        self.projectScrollContent.setGeometry(QRect(0, 0, 378, 389))
        self.projectScrollContent.setStyleSheet(u"QLabel {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}")
        self.projectScrollArea.setWidget(self.projectScrollContent)

        self.verticalLayout_4.addWidget(self.projectScrollArea)


        self.horizontalLayout_4.addWidget(self.projectLeftContent)

        self.projectRightContent = QFrame(self.projectPage)
        self.projectRightContent.setObjectName(u"projectRightContent")
        sizePolicy2.setHeightForWidth(self.projectRightContent.sizePolicy().hasHeightForWidth())
        self.projectRightContent.setSizePolicy(sizePolicy2)
        self.projectRightContent.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.projectRightContent.setFrameShape(QFrame.Shape.StyledPanel)
        self.projectRightContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.projectRightContent)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.projectRightContent)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(25, 20, 25, 20)
        self.titleCategoryPage = QLabel(self.frame_3)
        self.titleCategoryPage.setObjectName(u"titleCategoryPage")

        self.verticalLayout_9.addWidget(self.titleCategoryPage)

        self.tasksNumbers = QLabel(self.frame_3)
        self.tasksNumbers.setObjectName(u"tasksNumbers")

        self.verticalLayout_9.addWidget(self.tasksNumbers)


        self.horizontalLayout_8.addWidget(self.frame_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.taskFrame = QFrame(self.frame)
        self.taskFrame.setObjectName(u"taskFrame")
        self.taskFrame.setMinimumSize(QSize(0, 90))
        self.taskFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.taskFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.taskFrame)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(25, 20, 25, 20)
        self.newTaskButton = QPushButton(self.taskFrame)
        self.newTaskButton.setObjectName(u"newTaskButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.newTaskButton.sizePolicy().hasHeightForWidth())
        self.newTaskButton.setSizePolicy(sizePolicy6)
        self.newTaskButton.setMinimumSize(QSize(0, 0))
        self.newTaskButton.setMaximumSize(QSize(120, 40))
        self.newTaskButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.newTaskButton.setIcon(icon9)
        self.newTaskButton.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.newTaskButton)

        self.moreTasksButtons = QPushButton(self.taskFrame)
        self.moreTasksButtons.setObjectName(u"moreTasksButtons")
        self.moreTasksButtons.setMinimumSize(QSize(0, 0))
        self.moreTasksButtons.setMaximumSize(QSize(20, 40))
        self.moreTasksButtons.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.moreTasksButtons.setIcon(icon10)
        self.moreTasksButtons.setIconSize(QSize(16, 16))

        self.horizontalLayout_10.addWidget(self.moreTasksButtons)


        self.horizontalLayout_8.addWidget(self.taskFrame)


        self.verticalLayout_8.addWidget(self.frame)

        self.projectsPagesStacked = QStackedWidget(self.projectRightContent)
        self.projectsPagesStacked.setObjectName(u"projectsPagesStacked")
        self.Register_ProjectPage = QWidget()
        self.Register_ProjectPage.setObjectName(u"Register_ProjectPage")
        self.verticalLayout_10 = QVBoxLayout(self.Register_ProjectPage)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.bgRegisterProject = QWidget(self.Register_ProjectPage)
        self.bgRegisterProject.setObjectName(u"bgRegisterProject")
        self.bgRegisterProject.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.bgRegisterProject)
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, 9)
        self.frame_6 = QFrame(self.bgRegisterProject)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(0, 70))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_7)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.projectNameLabel = QLabel(self.frame_7)
        self.projectNameLabel.setObjectName(u"projectNameLabel")

        self.verticalLayout_31.addWidget(self.projectNameLabel)

        self.projectNameEdit = QLineEdit(self.frame_7)
        self.projectNameEdit.setObjectName(u"projectNameEdit")

        self.verticalLayout_31.addWidget(self.projectNameEdit)


        self.horizontalLayout_11.addWidget(self.frame_7)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.creationDateLabel = QLabel(self.frame_5)
        self.creationDateLabel.setObjectName(u"creationDateLabel")

        self.verticalLayout_11.addWidget(self.creationDateLabel)

        self.creationDateEdit = QLabel(self.frame_5)
        self.creationDateEdit.setObjectName(u"creationDateEdit")
        self.creationDateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.creationDateEdit)


        self.horizontalLayout_11.addWidget(self.frame_5)


        self.verticalLayout_12.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.bgRegisterProject)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_4)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(-1, 0, -1, 0)
        self.descriptionLabel = QLabel(self.frame_4)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout_32.addWidget(self.descriptionLabel)

        self.descriptionTextEdit = QPlainTextEdit(self.frame_4)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        sizePolicy2.setHeightForWidth(self.descriptionTextEdit.sizePolicy().hasHeightForWidth())
        self.descriptionTextEdit.setSizePolicy(sizePolicy2)
        self.descriptionTextEdit.setMaximumSize(QSize(16777215, 55))

        self.verticalLayout_32.addWidget(self.descriptionTextEdit)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.frame_8 = QFrame(self.bgRegisterProject)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_9)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.deadlineLabel = QLabel(self.frame_9)
        self.deadlineLabel.setObjectName(u"deadlineLabel")

        self.verticalLayout_35.addWidget(self.deadlineLabel)

        self.deadlineEdit = QLineEdit(self.frame_9)
        self.deadlineEdit.setObjectName(u"deadlineEdit")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.deadlineEdit.sizePolicy().hasHeightForWidth())
        self.deadlineEdit.setSizePolicy(sizePolicy7)

        self.verticalLayout_35.addWidget(self.deadlineEdit)


        self.horizontalLayout_12.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_10)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.priorityLabel = QLabel(self.frame_10)
        self.priorityLabel.setObjectName(u"priorityLabel")

        self.verticalLayout_34.addWidget(self.priorityLabel)

        self.priorityComboBox = QComboBox(self.frame_10)
        self.priorityComboBox.addItem("")
        self.priorityComboBox.addItem("")
        self.priorityComboBox.addItem("")
        self.priorityComboBox.setObjectName(u"priorityComboBox")
        self.priorityComboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_34.addWidget(self.priorityComboBox)


        self.horizontalLayout_12.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_8)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_11)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.initialStatsLabel = QLabel(self.frame_11)
        self.initialStatsLabel.setObjectName(u"initialStatsLabel")

        self.verticalLayout_33.addWidget(self.initialStatsLabel)

        self.initialStatscomboBox = QComboBox(self.frame_11)
        self.initialStatscomboBox.addItem("")
        self.initialStatscomboBox.addItem("")
        self.initialStatscomboBox.addItem("")
        self.initialStatscomboBox.setObjectName(u"initialStatscomboBox")
        self.initialStatscomboBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_33.addWidget(self.initialStatscomboBox)


        self.horizontalLayout_12.addWidget(self.frame_11)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.bgRegisterProject)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy5.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy5)
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_12)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(-1, 0, -1, 0)
        self.tagsLabel = QLabel(self.frame_12)
        self.tagsLabel.setObjectName(u"tagsLabel")

        self.verticalLayout_36.addWidget(self.tagsLabel)

        self.tagsEdit = QLineEdit(self.frame_12)
        self.tagsEdit.setObjectName(u"tagsEdit")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tagsEdit.sizePolicy().hasHeightForWidth())
        self.tagsEdit.setSizePolicy(sizePolicy8)

        self.verticalLayout_36.addWidget(self.tagsEdit)


        self.verticalLayout_12.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.bgRegisterProject)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_13)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, 0)
        self.frame_27 = QFrame(self.frame_13)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.attachmentsLabel = QLabel(self.frame_27)
        self.attachmentsLabel.setObjectName(u"attachmentsLabel")

        self.horizontalLayout_16.addWidget(self.attachmentsLabel)

        self.attachmentsMessageLabel = QLabel(self.frame_27)
        self.attachmentsMessageLabel.setObjectName(u"attachmentsMessageLabel")
        self.attachmentsMessageLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

        self.horizontalLayout_16.addWidget(self.attachmentsMessageLabel, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_37.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_13)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 9)
        self.addProjectFilesButton = QPushButton(self.frame_28)
        self.addProjectFilesButton.setObjectName(u"addProjectFilesButton")
        self.addProjectFilesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/folder-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addProjectFilesButton.setIcon(icon11)

        self.horizontalLayout_27.addWidget(self.addProjectFilesButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.filterFilesFrame = QFrame(self.frame_28)
        self.filterFilesFrame.setObjectName(u"filterFilesFrame")
        self.filterFilesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.filterFilesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.filterFilesFrame)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.filterButtonIcon = QPushButton(self.filterFilesFrame)
        self.filterButtonIcon.setObjectName(u"filterButtonIcon")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/HugeiconsFilter.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.filterButtonIcon.setIcon(icon12)
        self.filterButtonIcon.setIconSize(QSize(15, 14))

        self.horizontalLayout_28.addWidget(self.filterButtonIcon, 0, Qt.AlignmentFlag.AlignHCenter)

        self.filterFilesEdit = QLineEdit(self.filterFilesFrame)
        self.filterFilesEdit.setObjectName(u"filterFilesEdit")
        sizePolicy7.setHeightForWidth(self.filterFilesEdit.sizePolicy().hasHeightForWidth())
        self.filterFilesEdit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_28.addWidget(self.filterFilesEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.clearFilterProjectButton = QPushButton(self.filterFilesFrame)
        self.clearFilterProjectButton.setObjectName(u"clearFilterProjectButton")
        self.clearFilterProjectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.clearFilterProjectButton.setIcon(icon13)
        self.clearFilterProjectButton.setIconSize(QSize(18, 18))

        self.horizontalLayout_28.addWidget(self.clearFilterProjectButton, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_27.addWidget(self.filterFilesFrame, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_37.addWidget(self.frame_28)

        self.attachmentsFilesFrame = QFrame(self.frame_13)
        self.attachmentsFilesFrame.setObjectName(u"attachmentsFilesFrame")
        sizePolicy4.setHeightForWidth(self.attachmentsFilesFrame.sizePolicy().hasHeightForWidth())
        self.attachmentsFilesFrame.setSizePolicy(sizePolicy4)
        self.attachmentsFilesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.attachmentsFilesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.attachmentsFilesFrame)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.attachmentsList = QListWidget(self.attachmentsFilesFrame)
        self.attachmentsList.setObjectName(u"attachmentsList")
        self.attachmentsList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_39.addWidget(self.attachmentsList)


        self.verticalLayout_37.addWidget(self.attachmentsFilesFrame)

        self.addFilesProjectProgress = QProgressBar(self.frame_13)
        self.addFilesProjectProgress.setObjectName(u"addFilesProjectProgress")
        self.addFilesProjectProgress.setMaximumSize(QSize(16777215, 1))
        self.addFilesProjectProgress.setValue(0)
        self.addFilesProjectProgress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_37.addWidget(self.addFilesProjectProgress)


        self.verticalLayout_12.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.bgRegisterProject)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_14.setSpacing(16)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, 0)
        self.cancelRegisterProjectButton = QPushButton(self.frame_14)
        self.cancelRegisterProjectButton.setObjectName(u"cancelRegisterProjectButton")
        self.cancelRegisterProjectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.cancelRegisterProjectButton)

        self.confirmRegisterProjectButton = QPushButton(self.frame_14)
        self.confirmRegisterProjectButton.setObjectName(u"confirmRegisterProjectButton")
        self.confirmRegisterProjectButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_14.addWidget(self.confirmRegisterProjectButton)


        self.verticalLayout_12.addWidget(self.frame_14, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_10.addWidget(self.bgRegisterProject)

        self.projectsPagesStacked.addWidget(self.Register_ProjectPage)
        self.Projects_HomePage = QWidget()
        self.Projects_HomePage.setObjectName(u"Projects_HomePage")
        self.projectsPagesStacked.addWidget(self.Projects_HomePage)

        self.verticalLayout_8.addWidget(self.projectsPagesStacked)


        self.horizontalLayout_4.addWidget(self.projectRightContent)

        self.stackedWidget.addWidget(self.projectPage)
        self.taskPage = QWidget()
        self.taskPage.setObjectName(u"taskPage")
        self.stackedWidget.addWidget(self.taskPage)
        self.calendarPage = QWidget()
        self.calendarPage.setObjectName(u"calendarPage")
        self.stackedWidget.addWidget(self.calendarPage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.stackedWidget.addWidget(self.profilePage)
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.stackedWidget.addWidget(self.settingsPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        self.extraRightBox = QFrame(self.contentStacked)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.topMenus)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font2)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/icons/cil-envelope-open.png);")

        self.verticalLayout_30.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font2)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/icons/cil-print.png);")

        self.verticalLayout_30.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font2)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/icons/cil-account-logout.png);")

        self.verticalLayout_30.addWidget(self.btn_logout)


        self.verticalLayout_18.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout.addWidget(self.extraRightBox)


        self.verticalLayout_27.addWidget(self.contentStacked)

        self.bottomBar = QFrame(self.contentBox)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(4, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.creditsLabel.setFont(font4)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.creditsLabel)

        self.version_3 = QLabel(self.bottomBar)
        self.version_3.setObjectName(u"version_3")
        self.version_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.version_3)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setStyleSheet(u"background-image: url(:/icons/icons/cil-size-grip.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-attachment: fixed;\n"
"")
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_18.addWidget(self.frame_size_grip)


        self.verticalLayout_27.addWidget(self.bottomBar)


        self.horizontalLayout_26.addWidget(self.contentBox)


        self.horizontalLayout_3.addWidget(self.content)


        self.horizontalLayout_2.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)
        self.projectsPagesStacked.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.socialButton.setText(QCoreApplication.translate("MainWindow", u"Social", None))
        self.projectButton.setText(QCoreApplication.translate("MainWindow", u"Projetos", None))
        self.taskButton.setText(QCoreApplication.translate("MainWindow", u"Tasks", None))
        self.calendarButton.setText(QCoreApplication.translate("MainWindow", u"Calendario", None))
        self.profileButton.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">Este software foi criado com o intuito de armazenar tudo aquilo que voc\u00ea precisa no seu dia a dia para"
                        " sua organiza\u00e7\u00e3o em apenas um lugar.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; color:#bd93f9;\">Created by: Douglas H. S. Martins</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">pyside6-uic App.ui &gt; App_ui.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom"
                        ":12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">pyside6-rcc resource.qrc -o resource_rc.py</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.notificationButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.notificationButton.setText("")
#if QT_CONFIG(tooltip)
        self.themeButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.themeButton.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.max_resizeButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.max_resizeButton.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.tasksLabel.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Trabalho", None))
        self.pushButton_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Projetos", None))
        self.pushButton_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Estudos", None))
        self.pushButton_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Organiza\u00e7\u00e3o geral", None))
        self.pushButton_8.setText("")
        self.monthLabel.setText("")
        self.dayLabel.setText("")
        self.ActiveLogTitle.setText(QCoreApplication.translate("MainWindow", u"Active Log", None))
        self.dataLog.setText(QCoreApplication.translate("MainWindow", u"15/10/2024 12:52:21", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>vamos prosseguir com a ideia de automatizar redes sociais. Eu quero criar uma interface agradavel que me permite selecionar arquivos e textos</p><p>que eu quero que seja postado em determinada rede social.</p><p>As configura\u00e7\u00f5es das redes sociais v\u00e3o ficar nos settings em uma aba especifica.</p><p>Quero poder especificar as redes sociais que ir\u00e3o postar, editar especificamente o que cada uma vai fazer. quero algo parecido com a gui do wanderson </p><p><a href=\"https://www.youtube.com/watch?v=Mjjuw4suOUg\"><span style=\" text-decoration: underline; color:#0078d4;\">BRC - Filters And Link Between Project And Render - #BRCVideo07</span></a></p></body></html>", None))
        self.searchProjectsButton.setText("")
        self.searchProjectsLineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.ProjectsTitle.setText(QCoreApplication.translate("MainWindow", u"Category", None))
        self.addCategoryProjectButton.setText("")
        self.settingsCategoryProjects.setText("")
        self.allProjectsButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.openProjectsButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.closedProjectsButton.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.titleCategoryPage.setText("")
        self.tasksNumbers.setText("")
        self.newTaskButton.setText(QCoreApplication.translate("MainWindow", u"New task", None))
        self.moreTasksButtons.setText("")
        self.projectNameLabel.setText(QCoreApplication.translate("MainWindow", u"Project Name:", None))
        self.projectNameEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter project name...", None))
        self.creationDateLabel.setText(QCoreApplication.translate("MainWindow", u"Creation Date", None))
        self.creationDateEdit.setText("")
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.descriptionTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter projectt description...", None))
        self.deadlineLabel.setText(QCoreApplication.translate("MainWindow", u"Deadline:", None))
        self.deadlineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Expectative of conclusion...", None))
        self.priorityLabel.setText(QCoreApplication.translate("MainWindow", u"Priority:", None))
        self.priorityComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Hight", None))
        self.priorityComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Medium", None))
        self.priorityComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Low", None))

        self.initialStatsLabel.setText(QCoreApplication.translate("MainWindow", u"Initial Status:", None))
        self.initialStatscomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Not Started", None))
        self.initialStatscomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"In Progress", None))
        self.initialStatscomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Completed", None))

        self.tagsLabel.setText(QCoreApplication.translate("MainWindow", u"Tags (comma separeted):", None))
        self.tagsEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g, Develophment, Design, UI Design, Software...", None))
        self.attachmentsLabel.setText(QCoreApplication.translate("MainWindow", u"Attachments:", None))
        self.attachmentsMessageLabel.setText(QCoreApplication.translate("MainWindow", u"Add here all important files to the project", None))
        self.addProjectFilesButton.setText(QCoreApplication.translate("MainWindow", u" Add files to project", None))
        self.filterButtonIcon.setText("")
        self.filterFilesEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filter files", None))
        self.clearFilterProjectButton.setText("")
        self.addFilesProjectProgress.setFormat("")
        self.cancelRegisterProjectButton.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.confirmRegisterProjectButton.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: Douglas H. Soares", None))
        self.version_3.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

