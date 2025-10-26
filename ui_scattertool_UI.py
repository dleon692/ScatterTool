# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scattertool-UIyhBNTE.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QListView, QMainWindow,
    QPushButton, QRadioButton, QScrollArea, QScrollBar,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_ScatterToolUI(object):
    def setupUi(self, ScatterToolUI):
        if not ScatterToolUI.objectName():
            ScatterToolUI.setObjectName(u"ScatterToolUI")
        ScatterToolUI.resize(295, 829)
        self.centralwidget = QWidget(ScatterToolUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAcceptDrops(False)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 263, 1394))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_main = QWidget(self.scrollAreaWidgetContents)
        self.widget_main.setObjectName(u"widget_main")
        sizePolicy.setHeightForWidth(self.widget_main.sizePolicy().hasHeightForWidth())
        self.widget_main.setSizePolicy(sizePolicy)
        self.widget_main.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout_2 = QGridLayout(self.widget_main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scattergroupname = QLabel(self.widget_main)
        self.scattergroupname.setObjectName(u"scattergroupname")
        self.scattergroupname.setAutoFillBackground(False)
        self.scattergroupname.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(60, 60, 60);\n"
"}")
        self.scattergroupname.setFrameShape(QFrame.Shape.Box)
        self.scattergroupname.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.scattergroupname)

        self.colorbox = QFrame(self.widget_main)
        self.colorbox.setObjectName(u"colorbox")
        self.colorbox.setMinimumSize(QSize(20, 20))
        self.colorbox.setMaximumSize(QSize(20, 20))
        self.colorbox.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(45, 45, 45);  /* gris claro */\n"
"    border: 1px solid #A0A0A0;\n"
"}")
        self.colorbox.setFrameShape(QFrame.Shape.StyledPanel)
        self.colorbox.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_3.addWidget(self.colorbox)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.widget_about = QWidget(self.widget_main)
        self.widget_about.setObjectName(u"widget_about")
        self.gridLayout_5 = QGridLayout(self.widget_about)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_version = QLabel(self.widget_about)
        self.label_version.setObjectName(u"label_version")

        self.gridLayout_5.addWidget(self.label_version, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_about, 28, 0, 1, 1)

        self.widget_rotation = QWidget(self.widget_main)
        self.widget_rotation.setObjectName(u"widget_rotation")
        self.gridLayout_3 = QGridLayout(self.widget_rotation)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.spacer_RotX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.spacer_RotX, 0, 1, 1, 1)

        self.label_RosY = QLabel(self.widget_rotation)
        self.label_RosY.setObjectName(u"label_RosY")
        self.label_RosY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.label_RosY, 1, 0, 1, 1)

        self.spin_RyMax = QSpinBox(self.widget_rotation)
        self.spin_RyMax.setObjectName(u"spin_RyMax")
        self.spin_RyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RyMax.setWrapping(False)
        self.spin_RyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RyMax.setMaximum(360)
        self.spin_RyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RyMax.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RyMax, 1, 3, 1, 1)

        self.spacer_RotY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.spacer_RotY, 1, 1, 1, 1)

        self.spin_RyMin = QSpinBox(self.widget_rotation)
        self.spin_RyMin.setObjectName(u"spin_RyMin")
        self.spin_RyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RyMin.setWrapping(False)
        self.spin_RyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RyMin.setMaximum(360)
        self.spin_RyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RyMin.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RyMin, 1, 2, 1, 1)

        self.spin_RxMin = QSpinBox(self.widget_rotation)
        self.spin_RxMin.setObjectName(u"spin_RxMin")
        self.spin_RxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RxMin.setWrapping(False)
        self.spin_RxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RxMin.setMaximum(360)
        self.spin_RxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RxMin.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RxMin, 0, 2, 1, 1)

        self.spin_RxMax = QSpinBox(self.widget_rotation)
        self.spin_RxMax.setObjectName(u"spin_RxMax")
        self.spin_RxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RxMax.setWrapping(False)
        self.spin_RxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RxMax.setMaximum(360)
        self.spin_RxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RxMax.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RxMax, 0, 3, 1, 1)

        self.spin_RzMax = QSpinBox(self.widget_rotation)
        self.spin_RzMax.setObjectName(u"spin_RzMax")
        self.spin_RzMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RzMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RzMax.setWrapping(False)
        self.spin_RzMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RzMax.setMaximum(360)
        self.spin_RzMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RzMax.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RzMax, 2, 3, 1, 1)

        self.label_RosX = QLabel(self.widget_rotation)
        self.label_RosX.setObjectName(u"label_RosX")

        self.gridLayout_3.addWidget(self.label_RosX, 0, 0, 1, 1)

        self.spin_RzMin = QSpinBox(self.widget_rotation)
        self.spin_RzMin.setObjectName(u"spin_RzMin")
        self.spin_RzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RzMin.setWrapping(False)
        self.spin_RzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RzMin.setMaximum(360)
        self.spin_RzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RzMin.setDisplayIntegerBase(10)

        self.gridLayout_3.addWidget(self.spin_RzMin, 2, 2, 1, 1)

        self.spacer_RotZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.spacer_RotZ, 2, 1, 1, 1)

        self.label_RosZ = QLabel(self.widget_rotation)
        self.label_RosZ.setObjectName(u"label_RosZ")
        self.label_RosZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_3.addWidget(self.label_RosZ, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_rotation, 14, 0, 1, 1)

        self.toolButton_color = QToolButton(self.widget_main)
        self.toolButton_color.setObjectName(u"toolButton_color")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_color.sizePolicy().hasHeightForWidth())
        self.toolButton_color.setSizePolicy(sizePolicy1)
        self.toolButton_color.setCheckable(True)
        self.toolButton_color.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_color.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_color, 19, 0, 1, 1)

        self.widget_position = QWidget(self.widget_main)
        self.widget_position.setObjectName(u"widget_position")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_position.sizePolicy().hasHeightForWidth())
        self.widget_position.setSizePolicy(sizePolicy2)
        self.gridLayout = QGridLayout(self.widget_position)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.spin_PzMax = QSpinBox(self.widget_position)
        self.spin_PzMax.setObjectName(u"spin_PzMax")
        self.spin_PzMax.setEnabled(True)
        self.spin_PzMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PzMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PzMax.setAutoFillBackground(False)
        self.spin_PzMax.setWrapping(False)
        self.spin_PzMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PzMax.setMinimum(-999)
        self.spin_PzMax.setMaximum(999)
        self.spin_PzMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PzMax.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PzMax, 2, 3, 1, 1)

        self.spin_PxMin = QSpinBox(self.widget_position)
        self.spin_PxMin.setObjectName(u"spin_PxMin")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spin_PxMin.sizePolicy().hasHeightForWidth())
        self.spin_PxMin.setSizePolicy(sizePolicy3)
        self.spin_PxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PxMin.setWrapping(False)
        self.spin_PxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PxMin.setMinimum(-999)
        self.spin_PxMin.setMaximum(999)
        self.spin_PxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PxMin.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PxMin, 0, 2, 1, 1)

        self.spin_PzMin = QSpinBox(self.widget_position)
        self.spin_PzMin.setObjectName(u"spin_PzMin")
        self.spin_PzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PzMin.setWrapping(False)
        self.spin_PzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PzMin.setMinimum(-999)
        self.spin_PzMin.setMaximum(999)
        self.spin_PzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PzMin.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PzMin, 2, 2, 1, 1)

        self.spin_PyMax = QSpinBox(self.widget_position)
        self.spin_PyMax.setObjectName(u"spin_PyMax")
        self.spin_PyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PyMax.setWrapping(False)
        self.spin_PyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PyMax.setMinimum(-999)
        self.spin_PyMax.setMaximum(999)
        self.spin_PyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PyMax.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PyMax, 1, 3, 1, 1)

        self.label_PosY = QLabel(self.widget_position)
        self.label_PosY.setObjectName(u"label_PosY")
        self.label_PosY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.label_PosY, 1, 0, 1, 1)

        self.spin_PyMin = QSpinBox(self.widget_position)
        self.spin_PyMin.setObjectName(u"spin_PyMin")
        self.spin_PyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PyMin.setWrapping(False)
        self.spin_PyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PyMin.setMinimum(-999)
        self.spin_PyMin.setMaximum(999)
        self.spin_PyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PyMin.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PyMin, 1, 2, 1, 1)

        self.spacer_PosZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.spacer_PosZ, 2, 1, 1, 1)

        self.spacer__PosX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.spacer__PosX, 0, 1, 1, 1)

        self.label_PosX = QLabel(self.widget_position)
        self.label_PosX.setObjectName(u"label_PosX")

        self.gridLayout.addWidget(self.label_PosX, 0, 0, 1, 1)

        self.spacer__PosY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.spacer__PosY, 1, 1, 1, 1)

        self.label_PosZ = QLabel(self.widget_position)
        self.label_PosZ.setObjectName(u"label_PosZ")
        self.label_PosZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.label_PosZ, 2, 0, 1, 1)

        self.spin_PxMax = QSpinBox(self.widget_position)
        self.spin_PxMax.setObjectName(u"spin_PxMax")
        self.spin_PxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PxMax.setWrapping(False)
        self.spin_PxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PxMax.setMinimum(-999)
        self.spin_PxMax.setMaximum(999)
        self.spin_PxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PxMax.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spin_PxMax, 0, 3, 1, 1)


        self.gridLayout_2.addWidget(self.widget_position, 12, 0, 1, 1)

        self.checkBox_proportionalScale = QCheckBox(self.widget_main)
        self.checkBox_proportionalScale.setObjectName(u"checkBox_proportionalScale")

        self.gridLayout_2.addWidget(self.checkBox_proportionalScale, 16, 0, 1, 1)

        self.Button_update = QPushButton(self.widget_main)
        self.Button_update.setObjectName(u"Button_update")

        self.gridLayout_2.addWidget(self.Button_update, 18, 0, 1, 1)

        self.toolButton_display = QToolButton(self.widget_main)
        self.toolButton_display.setObjectName(u"toolButton_display")
        sizePolicy1.setHeightForWidth(self.toolButton_display.sizePolicy().hasHeightForWidth())
        self.toolButton_display.setSizePolicy(sizePolicy1)
        self.toolButton_display.setCheckable(True)
        self.toolButton_display.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_display.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_display, 24, 0, 1, 1)

        self.widget_scale = QWidget(self.widget_main)
        self.widget_scale.setObjectName(u"widget_scale")
        self.gridLayout_4 = QGridLayout(self.widget_scale)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_EscX = QLabel(self.widget_scale)
        self.label_EscX.setObjectName(u"label_EscX")

        self.gridLayout_4.addWidget(self.label_EscX, 0, 0, 1, 1)

        self.spin_SxMax = QSpinBox(self.widget_scale)
        self.spin_SxMax.setObjectName(u"spin_SxMax")
        self.spin_SxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SxMax.setWrapping(False)
        self.spin_SxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SxMax.setMaximum(999)
        self.spin_SxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SxMax.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SxMax, 0, 5, 1, 1)

        self.spin_SyMax = QSpinBox(self.widget_scale)
        self.spin_SyMax.setObjectName(u"spin_SyMax")
        self.spin_SyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SyMax.setWrapping(False)
        self.spin_SyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SyMax.setMaximum(999)
        self.spin_SyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SyMax.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SyMax, 1, 5, 1, 1)

        self.spin_SzMin = QSpinBox(self.widget_scale)
        self.spin_SzMin.setObjectName(u"spin_SzMin")
        self.spin_SzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SzMin.setWrapping(False)
        self.spin_SzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SzMin.setMaximum(999)
        self.spin_SzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SzMin.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SzMin, 2, 4, 1, 1)

        self.spacer_EscX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.spacer_EscX, 0, 3, 1, 1)

        self.spin_SzMax = QSpinBox(self.widget_scale)
        self.spin_SzMax.setObjectName(u"spin_SzMax")
        self.spin_SzMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SzMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SzMax.setWrapping(False)
        self.spin_SzMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SzMax.setMaximum(999)
        self.spin_SzMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SzMax.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SzMax, 2, 5, 1, 1)

        self.label_EscY = QLabel(self.widget_scale)
        self.label_EscY.setObjectName(u"label_EscY")
        self.label_EscY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_4.addWidget(self.label_EscY, 1, 0, 1, 1)

        self.label_EscZ = QLabel(self.widget_scale)
        self.label_EscZ.setObjectName(u"label_EscZ")
        self.label_EscZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_4.addWidget(self.label_EscZ, 2, 0, 1, 1)

        self.spacer_EscY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.spacer_EscY, 1, 3, 1, 1)

        self.spin_SxMin = QSpinBox(self.widget_scale)
        self.spin_SxMin.setObjectName(u"spin_SxMin")
        self.spin_SxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SxMin.setWrapping(False)
        self.spin_SxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SxMin.setMaximum(999)
        self.spin_SxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SxMin.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SxMin, 0, 4, 1, 1)

        self.spacer_EscZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.spacer_EscZ, 2, 3, 1, 1)

        self.spin_SyMin = QSpinBox(self.widget_scale)
        self.spin_SyMin.setObjectName(u"spin_SyMin")
        self.spin_SyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SyMin.setWrapping(False)
        self.spin_SyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SyMin.setMaximum(999)
        self.spin_SyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SyMin.setDisplayIntegerBase(10)

        self.gridLayout_4.addWidget(self.spin_SyMin, 1, 4, 1, 1)


        self.gridLayout_2.addWidget(self.widget_scale, 17, 0, 1, 1)

        self.widget_display = QWidget(self.widget_main)
        self.widget_display.setObjectName(u"widget_display")
        self.verticalLayout_6 = QVBoxLayout(self.widget_display)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_04 = QHBoxLayout()
        self.horizontalLayout_04.setObjectName(u"horizontalLayout_04")
        self.button_box = QRadioButton(self.widget_display)
        self.button_box.setObjectName(u"button_box")

        self.horizontalLayout_04.addWidget(self.button_box)

        self.button_mesh = QRadioButton(self.widget_display)
        self.button_mesh.setObjectName(u"button_mesh")

        self.horizontalLayout_04.addWidget(self.button_mesh)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_04.addItem(self.horizontalSpacer_12)


        self.verticalLayout_6.addLayout(self.horizontalLayout_04)


        self.gridLayout_2.addWidget(self.widget_display, 25, 0, 1, 1)

        self.toolButton_about = QToolButton(self.widget_main)
        self.toolButton_about.setObjectName(u"toolButton_about")
        sizePolicy1.setHeightForWidth(self.toolButton_about.sizePolicy().hasHeightForWidth())
        self.toolButton_about.setSizePolicy(sizePolicy1)
        self.toolButton_about.setCheckable(True)
        self.toolButton_about.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_about.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_about, 27, 0, 1, 1)

        self.toolButton = QToolButton(self.widget_main)
        self.toolButton.setObjectName(u"toolButton")
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton, 7, 0, 1, 1)

        self.toolButton_scale = QToolButton(self.widget_main)
        self.toolButton_scale.setObjectName(u"toolButton_scale")
        sizePolicy1.setHeightForWidth(self.toolButton_scale.sizePolicy().hasHeightForWidth())
        self.toolButton_scale.setSizePolicy(sizePolicy1)
        self.toolButton_scale.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_scale.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_scale, 15, 0, 1, 1)

        self.widget_colorVar = QWidget(self.widget_main)
        self.widget_colorVar.setObjectName(u"widget_colorVar")
        self.verticalLayout_5 = QVBoxLayout(self.widget_colorVar)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_colorvar = QGroupBox(self.widget_colorVar)
        self.groupBox_colorvar.setObjectName(u"groupBox_colorvar")
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_colorvar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.label_variationNum = QLabel(self.groupBox_colorvar)
        self.label_variationNum.setObjectName(u"label_variationNum")

        self.horizontalLayout_4.addWidget(self.label_variationNum)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.spinBox_variatNum = QSpinBox(self.groupBox_colorvar)
        self.spinBox_variatNum.setObjectName(u"spinBox_variatNum")

        self.horizontalLayout_4.addWidget(self.spinBox_variatNum)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.line_2 = QFrame(self.groupBox_colorvar)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_id = QLabel(self.groupBox_colorvar)
        self.label_id.setObjectName(u"label_id")

        self.horizontalLayout_5.addWidget(self.label_id)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)

        self.spinBox_elemtID = QSpinBox(self.groupBox_colorvar)
        self.spinBox_elemtID.setObjectName(u"spinBox_elemtID")
        self.spinBox_elemtID.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.spinBox_elemtID.setMinimum(1)

        self.horizontalLayout_5.addWidget(self.spinBox_elemtID)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.line = QFrame(self.groupBox_colorvar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_9.addWidget(self.line)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.spinBox_hueMin = QSpinBox(self.groupBox_colorvar)
        self.spinBox_hueMin.setObjectName(u"spinBox_hueMin")
        self.spinBox_hueMin.setWrapping(False)
        self.spinBox_hueMin.setFrame(True)
        self.spinBox_hueMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_hueMin.setProperty(u"showGroupSeparator", False)
        self.spinBox_hueMin.setMinimum(-180)
        self.spinBox_hueMin.setMaximum(0)

        self.gridLayout_6.addWidget(self.spinBox_hueMin, 2, 2, 1, 1)

        self.spinBox_briMin = QSpinBox(self.groupBox_colorvar)
        self.spinBox_briMin.setObjectName(u"spinBox_briMin")
        self.spinBox_briMin.setMinimum(-100)
        self.spinBox_briMin.setMaximum(0)

        self.gridLayout_6.addWidget(self.spinBox_briMin, 4, 2, 1, 1)

        self.spinBox_briMax = QSpinBox(self.groupBox_colorvar)
        self.spinBox_briMax.setObjectName(u"spinBox_briMax")
        self.spinBox_briMax.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_briMax, 4, 3, 1, 1)

        self.label_hue = QLabel(self.groupBox_colorvar)
        self.label_hue.setObjectName(u"label_hue")

        self.gridLayout_6.addWidget(self.label_hue, 2, 0, 1, 1)

        self.label_saturation = QLabel(self.groupBox_colorvar)
        self.label_saturation.setObjectName(u"label_saturation")

        self.gridLayout_6.addWidget(self.label_saturation, 3, 0, 1, 1)

        self.spinBox_conMin = QSpinBox(self.groupBox_colorvar)
        self.spinBox_conMin.setObjectName(u"spinBox_conMin")
        self.spinBox_conMin.setMinimum(-100)
        self.spinBox_conMin.setMaximum(0)

        self.gridLayout_6.addWidget(self.spinBox_conMin, 5, 2, 1, 1)

        self.spinBox_satMin = QSpinBox(self.groupBox_colorvar)
        self.spinBox_satMin.setObjectName(u"spinBox_satMin")
        self.spinBox_satMin.setMinimum(-100)
        self.spinBox_satMin.setMaximum(0)

        self.gridLayout_6.addWidget(self.spinBox_satMin, 3, 2, 1, 1)

        self.spinBox_satMax = QSpinBox(self.groupBox_colorvar)
        self.spinBox_satMax.setObjectName(u"spinBox_satMax")
        self.spinBox_satMax.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_satMax, 3, 3, 1, 1)

        self.label_contrast = QLabel(self.groupBox_colorvar)
        self.label_contrast.setObjectName(u"label_contrast")

        self.gridLayout_6.addWidget(self.label_contrast, 5, 0, 1, 1)

        self.spinBox_conMax = QSpinBox(self.groupBox_colorvar)
        self.spinBox_conMax.setObjectName(u"spinBox_conMax")
        self.spinBox_conMax.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinBox_conMax, 5, 3, 1, 1)

        self.spinBox_hueMax = QSpinBox(self.groupBox_colorvar)
        self.spinBox_hueMax.setObjectName(u"spinBox_hueMax")

        self.gridLayout_6.addWidget(self.spinBox_hueMax, 2, 3, 1, 1)

        self.label_bright = QLabel(self.groupBox_colorvar)
        self.label_bright.setObjectName(u"label_bright")

        self.gridLayout_6.addWidget(self.label_bright, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 2, 1, 1, 1)


        self.verticalLayout_9.addLayout(self.gridLayout_6)


        self.verticalLayout_5.addWidget(self.groupBox_colorvar)

        self.pushButton_apply = QPushButton(self.widget_colorVar)
        self.pushButton_apply.setObjectName(u"pushButton_apply")

        self.verticalLayout_5.addWidget(self.pushButton_apply)


        self.gridLayout_2.addWidget(self.widget_colorVar, 22, 0, 1, 1)

        self.groupBox_dmethod = QGroupBox(self.widget_main)
        self.groupBox_dmethod.setObjectName(u"groupBox_dmethod")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_dmethod)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 0, 5, 5)
        self.horizontalLayout_01 = QHBoxLayout()
        self.horizontalLayout_01.setObjectName(u"horizontalLayout_01")
        self.button_surface = QRadioButton(self.groupBox_dmethod)
        self.button_surface.setObjectName(u"button_surface")

        self.horizontalLayout_01.addWidget(self.button_surface)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_01.addItem(self.horizontalSpacer_9)

        self.button_spline = QRadioButton(self.groupBox_dmethod)
        self.button_spline.setObjectName(u"button_spline")

        self.horizontalLayout_01.addWidget(self.button_spline)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_01.addItem(self.horizontalSpacer_10)

        self.button_painter = QRadioButton(self.groupBox_dmethod)
        self.button_painter.setObjectName(u"button_painter")

        self.horizontalLayout_01.addWidget(self.button_painter)


        self.verticalLayout_8.addLayout(self.horizontalLayout_01)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_pickSpline = QPushButton(self.groupBox_dmethod)
        self.button_pickSpline.setObjectName(u"button_pickSpline")

        self.horizontalLayout_9.addWidget(self.button_pickSpline)

        self.button_pickSurface = QPushButton(self.groupBox_dmethod)
        self.button_pickSurface.setObjectName(u"button_pickSurface")

        self.horizontalLayout_9.addWidget(self.button_pickSurface)


        self.verticalLayout_8.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_05 = QHBoxLayout()
        self.horizontalLayout_05.setObjectName(u"horizontalLayout_05")
        self.button_elementCount = QRadioButton(self.groupBox_dmethod)
        self.button_elementCount.setObjectName(u"button_elementCount")
        sizePolicy3.setHeightForWidth(self.button_elementCount.sizePolicy().hasHeightForWidth())
        self.button_elementCount.setSizePolicy(sizePolicy3)

        self.horizontalLayout_05.addWidget(self.button_elementCount)

        self.spin_elementCount = QSpinBox(self.groupBox_dmethod)
        self.spin_elementCount.setObjectName(u"spin_elementCount")
        self.spin_elementCount.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_elementCount.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_elementCount.setWrapping(False)
        self.spin_elementCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_elementCount.setMaximum(100000)
        self.spin_elementCount.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_elementCount.setDisplayIntegerBase(10)

        self.horizontalLayout_05.addWidget(self.spin_elementCount)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_05.addItem(self.horizontalSpacer_8)


        self.verticalLayout_8.addLayout(self.horizontalLayout_05)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.button_distance = QRadioButton(self.groupBox_dmethod)
        self.button_distance.setObjectName(u"button_distance")
        sizePolicy3.setHeightForWidth(self.button_distance.sizePolicy().hasHeightForWidth())
        self.button_distance.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.button_distance)

        self.spin_distance = QSpinBox(self.groupBox_dmethod)
        self.spin_distance.setObjectName(u"spin_distance")
        self.spin_distance.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_distance.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_distance.setWrapping(False)
        self.spin_distance.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_distance.setMaximum(100000)
        self.spin_distance.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_distance.setDisplayIntegerBase(10)

        self.horizontalLayout_2.addWidget(self.spin_distance)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_11)


        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.label_brushSize = QLabel(self.groupBox_dmethod)
        self.label_brushSize.setObjectName(u"label_brushSize")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_brushSize.sizePolicy().hasHeightForWidth())
        self.label_brushSize.setSizePolicy(sizePolicy4)
        self.label_brushSize.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.label_brushSize)

        self.spin_brush = QSpinBox(self.groupBox_dmethod)
        self.spin_brush.setObjectName(u"spin_brush")
        self.spin_brush.setMaximumSize(QSize(16777215, 16777215))
        self.spin_brush.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_brush.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_brush.setWrapping(False)
        self.spin_brush.setFrame(True)
        self.spin_brush.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_brush.setProperty(u"showGroupSeparator", False)
        self.spin_brush.setMaximum(100000)
        self.spin_brush.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_brush.setDisplayIntegerBase(10)

        self.horizontalLayout_6.addWidget(self.spin_brush)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_6)


        self.gridLayout_2.addWidget(self.groupBox_dmethod, 1, 0, 1, 1)

        self.widget_elementTransform = QWidget(self.widget_main)
        self.widget_elementTransform.setObjectName(u"widget_elementTransform")
        self.verticalLayout_4 = QVBoxLayout(self.widget_elementTransform)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_06 = QHBoxLayout()
        self.horizontalLayout_06.setSpacing(6)
        self.horizontalLayout_06.setObjectName(u"horizontalLayout_06")
        self.horizontalLayout_06.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_06.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_random = QCheckBox(self.widget_elementTransform)
        self.checkBox_random.setObjectName(u"checkBox_random")

        self.horizontalLayout_06.addWidget(self.checkBox_random)

        self.button_shuffle = QPushButton(self.widget_elementTransform)
        self.button_shuffle.setObjectName(u"button_shuffle")

        self.horizontalLayout_06.addWidget(self.button_shuffle)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_06.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_06)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.checkBox_collision = QCheckBox(self.widget_elementTransform)
        self.checkBox_collision.setObjectName(u"checkBox_collision")

        self.horizontalLayout_7.addWidget(self.checkBox_collision)

        self.spinBox_colRadius = QSpinBox(self.widget_elementTransform)
        self.spinBox_colRadius.setObjectName(u"spinBox_colRadius")
        self.spinBox_colRadius.setMaximum(1000)

        self.horizontalLayout_7.addWidget(self.spinBox_colRadius)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.groupBox_direction = QGroupBox(self.widget_elementTransform)
        self.groupBox_direction.setObjectName(u"groupBox_direction")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_direction)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 0, 5, 5)
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setVerticalSpacing(0)
        self.horizontalSlider_direction = QSlider(self.groupBox_direction)
        self.horizontalSlider_direction.setObjectName(u"horizontalSlider_direction")
        self.horizontalSlider_direction.setMinimum(-100)
        self.horizontalSlider_direction.setMaximum(100)
        self.horizontalSlider_direction.setSliderPosition(100)
        self.horizontalSlider_direction.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_7.addWidget(self.horizontalSlider_direction, 7, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.label_down = QLabel(self.groupBox_direction)
        self.label_down.setObjectName(u"label_down")

        self.horizontalLayout.addWidget(self.label_down)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_normal = QLabel(self.groupBox_direction)
        self.label_normal.setObjectName(u"label_normal")
        sizePolicy2.setHeightForWidth(self.label_normal.sizePolicy().hasHeightForWidth())
        self.label_normal.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label_normal)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_up = QLabel(self.groupBox_direction)
        self.label_up.setObjectName(u"label_up")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_up.sizePolicy().hasHeightForWidth())
        self.label_up.setSizePolicy(sizePolicy5)
        self.label_up.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_up.setAutoFillBackground(False)
        self.label_up.setScaledContents(False)
        self.label_up.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label_up)


        self.gridLayout_7.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.spinBox_direction = QSpinBox(self.groupBox_direction)
        self.spinBox_direction.setObjectName(u"spinBox_direction")
        self.spinBox_direction.setMinimum(-100)
        self.spinBox_direction.setMaximum(100)

        self.gridLayout_7.addWidget(self.spinBox_direction, 7, 2, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_7)


        self.verticalLayout_4.addWidget(self.groupBox_direction)


        self.gridLayout_2.addWidget(self.widget_elementTransform, 8, 0, 1, 1)

        self.toolButton_distribute = QToolButton(self.widget_main)
        self.toolButton_distribute.setObjectName(u"toolButton_distribute")
        sizePolicy1.setHeightForWidth(self.toolButton_distribute.sizePolicy().hasHeightForWidth())
        self.toolButton_distribute.setSizePolicy(sizePolicy1)
        self.toolButton_distribute.setCheckable(True)
        self.toolButton_distribute.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_distribute.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_distribute, 5, 0, 1, 1)

        self.toolButton_position = QToolButton(self.widget_main)
        self.toolButton_position.setObjectName(u"toolButton_position")
        sizePolicy1.setHeightForWidth(self.toolButton_position.sizePolicy().hasHeightForWidth())
        self.toolButton_position.setSizePolicy(sizePolicy1)
        self.toolButton_position.setCheckable(True)
        self.toolButton_position.setChecked(False)
        self.toolButton_position.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_position.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_position, 10, 0, 1, 1)

        self.toolButton_Rotation = QToolButton(self.widget_main)
        self.toolButton_Rotation.setObjectName(u"toolButton_Rotation")
        sizePolicy1.setHeightForWidth(self.toolButton_Rotation.sizePolicy().hasHeightForWidth())
        self.toolButton_Rotation.setSizePolicy(sizePolicy1)
        self.toolButton_Rotation.setCheckable(True)
        self.toolButton_Rotation.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_Rotation.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout_2.addWidget(self.toolButton_Rotation, 13, 0, 1, 1)

        self.widget_distribute = QWidget(self.widget_main)
        self.widget_distribute.setObjectName(u"widget_distribute")
        self.verticalLayout = QVBoxLayout(self.widget_distribute)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_02 = QHBoxLayout()
        self.horizontalLayout_02.setObjectName(u"horizontalLayout_02")
        self.ListScrollBar = QScrollBar(self.widget_distribute)
        self.ListScrollBar.setObjectName(u"ListScrollBar")
        self.ListScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_02.addWidget(self.ListScrollBar)

        self.ListElements = QListView(self.widget_distribute)
        self.ListElements.setObjectName(u"ListElements")

        self.horizontalLayout_02.addWidget(self.ListElements)


        self.verticalLayout.addLayout(self.horizontalLayout_02)

        self.horizontalLayout_03 = QHBoxLayout()
        self.horizontalLayout_03.setObjectName(u"horizontalLayout_03")
        self.pushButton_addList = QPushButton(self.widget_distribute)
        self.pushButton_addList.setObjectName(u"pushButton_addList")
        sizePolicy1.setHeightForWidth(self.pushButton_addList.sizePolicy().hasHeightForWidth())
        self.pushButton_addList.setSizePolicy(sizePolicy1)

        self.horizontalLayout_03.addWidget(self.pushButton_addList)

        self.pushButton_add = QPushButton(self.widget_distribute)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy1.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy1)

        self.horizontalLayout_03.addWidget(self.pushButton_add)


        self.verticalLayout.addLayout(self.horizontalLayout_03)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_delete = QPushButton(self.widget_distribute)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy1.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButton_delete)

        self.pushButton_replace = QPushButton(self.widget_distribute)
        self.pushButton_replace.setObjectName(u"pushButton_replace")
        sizePolicy1.setHeightForWidth(self.pushButton_replace.sizePolicy().hasHeightForWidth())
        self.pushButton_replace.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.pushButton_replace)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.label_frecuencyPercent = QLabel(self.widget_distribute)
        self.label_frecuencyPercent.setObjectName(u"label_frecuencyPercent")
        sizePolicy2.setHeightForWidth(self.label_frecuencyPercent.sizePolicy().hasHeightForWidth())
        self.label_frecuencyPercent.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.label_frecuencyPercent)

        self.label_percent = QLabel(self.widget_distribute)
        self.label_percent.setObjectName(u"label_percent")

        self.horizontalLayout_8.addWidget(self.label_percent)

        self.spinBox_frecuencyPercent = QSpinBox(self.widget_distribute)
        self.spinBox_frecuencyPercent.setObjectName(u"spinBox_frecuencyPercent")
        self.spinBox_frecuencyPercent.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spinBox_frecuencyPercent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox_frecuencyPercent.setWrapping(False)
        self.spinBox_frecuencyPercent.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_frecuencyPercent.setMaximum(100)
        self.spinBox_frecuencyPercent.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_frecuencyPercent.setDisplayIntegerBase(10)

        self.horizontalLayout_8.addWidget(self.spinBox_frecuencyPercent)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_14)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.gridLayout_2.addWidget(self.widget_distribute, 6, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.label_ViewDisplay = QLabel(self.widget_main)
        self.label_ViewDisplay.setObjectName(u"label_ViewDisplay")

        self.horizontalLayout_11.addWidget(self.label_ViewDisplay)

        self.spinBox_viewDisp = QSpinBox(self.widget_main)
        self.spinBox_viewDisp.setObjectName(u"spinBox_viewDisp")
        self.spinBox_viewDisp.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spinBox_viewDisp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox_viewDisp.setWrapping(False)
        self.spinBox_viewDisp.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_viewDisp.setMaximum(100)
        self.spinBox_viewDisp.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_viewDisp.setDisplayIntegerBase(10)

        self.horizontalLayout_11.addWidget(self.spinBox_viewDisp)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)


        self.gridLayout_2.addLayout(self.horizontalLayout_11, 26, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_main)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        ScatterToolUI.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ScatterToolUI)
        self.statusbar.setObjectName(u"statusbar")
        ScatterToolUI.setStatusBar(self.statusbar)

        self.retranslateUi(ScatterToolUI)

        QMetaObject.connectSlotsByName(ScatterToolUI)
    # setupUi

    def retranslateUi(self, ScatterToolUI):
        ScatterToolUI.setWindowTitle(QCoreApplication.translate("ScatterToolUI", u"MainWindow", None))
        self.scattergroupname.setText("")
        self.label_version.setText(QCoreApplication.translate("ScatterToolUI", u"Scatter Tool Version 0.0.0", None))
        self.label_RosY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_RosX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_RosZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.toolButton_color.setText(QCoreApplication.translate("ScatterToolUI", u"Color Variation", None))
        self.label_PosY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_PosX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_PosZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.checkBox_proportionalScale.setText(QCoreApplication.translate("ScatterToolUI", u"Proportional Scale", None))
        self.Button_update.setText(QCoreApplication.translate("ScatterToolUI", u"Update", None))
        self.toolButton_display.setText(QCoreApplication.translate("ScatterToolUI", u"Display", None))
        self.label_EscX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_EscY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_EscZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.button_box.setText(QCoreApplication.translate("ScatterToolUI", u"Box", None))
        self.button_mesh.setText(QCoreApplication.translate("ScatterToolUI", u"Mesh", None))
        self.toolButton_about.setText(QCoreApplication.translate("ScatterToolUI", u"About", None))
        self.toolButton.setText(QCoreApplication.translate("ScatterToolUI", u"Elements Transform", None))
        self.toolButton_scale.setText(QCoreApplication.translate("ScatterToolUI", u"Scale (0% / 100%)", None))
        self.groupBox_colorvar.setTitle(QCoreApplication.translate("ScatterToolUI", u"Texture / Diffuse Color ", None))
        self.label_variationNum.setText(QCoreApplication.translate("ScatterToolUI", u"Variation Number", None))
        self.label_id.setText(QCoreApplication.translate("ScatterToolUI", u"Element ID", None))
#if QT_CONFIG(tooltip)
        self.label_hue.setToolTip(QCoreApplication.translate("ScatterToolUI", u"Hue Shift (Min -180 / Max 180)", None))
#endif // QT_CONFIG(tooltip)
        self.label_hue.setText(QCoreApplication.translate("ScatterToolUI", u"Hue Shift", None))
#if QT_CONFIG(tooltip)
        self.label_saturation.setToolTip(QCoreApplication.translate("ScatterToolUI", u"Saturation (Min -100 / Max 100)", None))
#endif // QT_CONFIG(tooltip)
        self.label_saturation.setText(QCoreApplication.translate("ScatterToolUI", u"Saturation", None))
#if QT_CONFIG(tooltip)
        self.label_contrast.setToolTip(QCoreApplication.translate("ScatterToolUI", u"Contrast (Min -100 / Max 100)", None))
#endif // QT_CONFIG(tooltip)
        self.label_contrast.setText(QCoreApplication.translate("ScatterToolUI", u"Contrast", None))
#if QT_CONFIG(tooltip)
        self.label_bright.setToolTip(QCoreApplication.translate("ScatterToolUI", u"Brightness (Min -100 / Max 100)", None))
#endif // QT_CONFIG(tooltip)
        self.label_bright.setText(QCoreApplication.translate("ScatterToolUI", u"Brightness", None))
        self.pushButton_apply.setText(QCoreApplication.translate("ScatterToolUI", u"Apply", None))
        self.groupBox_dmethod.setTitle(QCoreApplication.translate("ScatterToolUI", u"Distribution Method", None))
        self.button_surface.setText(QCoreApplication.translate("ScatterToolUI", u"Surface", None))
        self.button_spline.setText(QCoreApplication.translate("ScatterToolUI", u"Spline", None))
        self.button_painter.setText(QCoreApplication.translate("ScatterToolUI", u"Painter", None))
        self.button_pickSpline.setText(QCoreApplication.translate("ScatterToolUI", u"Pick Spline", None))
        self.button_pickSurface.setText(QCoreApplication.translate("ScatterToolUI", u"Pick Surface", None))
        self.button_elementCount.setText(QCoreApplication.translate("ScatterToolUI", u"Element Count", None))
        self.button_distance.setText(QCoreApplication.translate("ScatterToolUI", u"Distance (cm)", None))
        self.label_brushSize.setText(QCoreApplication.translate("ScatterToolUI", u"      Brush Size (cm)", None))
        self.checkBox_random.setText(QCoreApplication.translate("ScatterToolUI", u"Random", None))
        self.button_shuffle.setText(QCoreApplication.translate("ScatterToolUI", u"Shuffle", None))
        self.checkBox_collision.setText(QCoreApplication.translate("ScatterToolUI", u"Collisions Radius (%)", None))
        self.groupBox_direction.setTitle(QCoreApplication.translate("ScatterToolUI", u"Direction", None))
        self.label_down.setText(QCoreApplication.translate("ScatterToolUI", u"Down", None))
        self.label_normal.setText(QCoreApplication.translate("ScatterToolUI", u"Normal", None))
        self.label_up.setText(QCoreApplication.translate("ScatterToolUI", u"Up", None))
        self.toolButton_distribute.setText(QCoreApplication.translate("ScatterToolUI", u"Distribute Elements", None))
        self.toolButton_position.setText(QCoreApplication.translate("ScatterToolUI", u"Position (-999 / 999cm)", None))
        self.toolButton_Rotation.setText(QCoreApplication.translate("ScatterToolUI", u"Rotation (0\u00b0 / 360\u00b0)", None))
        self.pushButton_addList.setText(QCoreApplication.translate("ScatterToolUI", u"Add Selection", None))
        self.pushButton_add.setText(QCoreApplication.translate("ScatterToolUI", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("ScatterToolUI", u"Delete", None))
        self.pushButton_replace.setText(QCoreApplication.translate("ScatterToolUI", u"Replace", None))
        self.label_frecuencyPercent.setText(QCoreApplication.translate("ScatterToolUI", u"Element Frecuency", None))
        self.label_percent.setText(QCoreApplication.translate("ScatterToolUI", u" %", None))
        self.label_ViewDisplay.setText(QCoreApplication.translate("ScatterToolUI", u"Viewport Display %", None))
    # retranslateUi

