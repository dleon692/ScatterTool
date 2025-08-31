# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'scattertool-UIGlZHSk.ui'
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
from PySide2.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QFrame,
    QHBoxLayout, QLabel, QLayout, QListView,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QScrollBar, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_ScatterToolUI(object):
    def setupUi(self, ScatterToolUI):
        if not ScatterToolUI.objectName():
            ScatterToolUI.setObjectName(u"ScatterToolUI")
        ScatterToolUI.resize(438, 940)
        self.centralwidget = QWidget(ScatterToolUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_8 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 0, 438, 871))
        self.GeneralVertLayout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.GeneralVertLayout.setSpacing(5)
        self.GeneralVertLayout.setObjectName(u"GeneralVertLayout")
        self.GeneralVertLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.GeneralVertLayout.setContentsMargins(10, 10, 10, 10)
        self.label_dmethod = QLabel(self.verticalLayoutWidget_8)
        self.label_dmethod.setObjectName(u"label_dmethod")

        self.GeneralVertLayout.addWidget(self.label_dmethod)

        self.line_Method = QFrame(self.verticalLayoutWidget_8)
        self.line_Method.setObjectName(u"line_Method")
        self.line_Method.setFrameShape(QFrame.Shape.HLine)
        self.line_Method.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Method)

        self.horizontalLayout_01 = QHBoxLayout()
        self.horizontalLayout_01.setObjectName(u"horizontalLayout_01")
        self.button_spline = QRadioButton(self.verticalLayoutWidget_8)
        self.button_spline.setObjectName(u"button_spline")

        self.horizontalLayout_01.addWidget(self.button_spline)

        self.button_surface = QRadioButton(self.verticalLayoutWidget_8)
        self.button_surface.setObjectName(u"button_surface")

        self.horizontalLayout_01.addWidget(self.button_surface)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_01)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button_pickSpline = QPushButton(self.verticalLayoutWidget_8)
        self.button_pickSpline.setObjectName(u"button_pickSpline")

        self.horizontalLayout_9.addWidget(self.button_pickSpline)

        self.button_pickSurface = QPushButton(self.verticalLayoutWidget_8)
        self.button_pickSurface.setObjectName(u"button_pickSurface")

        self.horizontalLayout_9.addWidget(self.button_pickSurface)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_9)

        self.label_delements = QLabel(self.verticalLayoutWidget_8)
        self.label_delements.setObjectName(u"label_delements")

        self.GeneralVertLayout.addWidget(self.label_delements)

        self.line_Element = QFrame(self.verticalLayoutWidget_8)
        self.line_Element.setObjectName(u"line_Element")
        self.line_Element.setFrameShape(QFrame.Shape.HLine)
        self.line_Element.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Element)

        self.horizontalLayout_02 = QHBoxLayout()
        self.horizontalLayout_02.setObjectName(u"horizontalLayout_02")
        self.ListScrollBar = QScrollBar(self.verticalLayoutWidget_8)
        self.ListScrollBar.setObjectName(u"ListScrollBar")
        self.ListScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_02.addWidget(self.ListScrollBar)

        self.ListElements = QListView(self.verticalLayoutWidget_8)
        self.ListElements.setObjectName(u"ListElements")

        self.horizontalLayout_02.addWidget(self.ListElements)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_02)

        self.horizontalLayout_03 = QHBoxLayout()
        self.horizontalLayout_03.setObjectName(u"horizontalLayout_03")
        self.pushButton_addList = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_addList.setObjectName(u"pushButton_addList")

        self.horizontalLayout_03.addWidget(self.pushButton_addList)

        self.pushButton_add = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.horizontalLayout_03.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.horizontalLayout_03.addWidget(self.pushButton_delete)

        self.pushButton_replace = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_replace.setObjectName(u"pushButton_replace")

        self.horizontalLayout_03.addWidget(self.pushButton_replace)

        self.label_percent = QLabel(self.verticalLayoutWidget_8)
        self.label_percent.setObjectName(u"label_percent")

        self.horizontalLayout_03.addWidget(self.label_percent)

        self.spinBox_frecuencyPercent = QSpinBox(self.verticalLayoutWidget_8)
        self.spinBox_frecuencyPercent.setObjectName(u"spinBox_frecuencyPercent")
        self.spinBox_frecuencyPercent.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spinBox_frecuencyPercent.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox_frecuencyPercent.setWrapping(False)
        self.spinBox_frecuencyPercent.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_frecuencyPercent.setMaximum(100)
        self.spinBox_frecuencyPercent.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_frecuencyPercent.setDisplayIntegerBase(10)

        self.horizontalLayout_03.addWidget(self.spinBox_frecuencyPercent)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_03)

        self.label_display = QLabel(self.verticalLayoutWidget_8)
        self.label_display.setObjectName(u"label_display")

        self.GeneralVertLayout.addWidget(self.label_display)

        self.line_Display = QFrame(self.verticalLayoutWidget_8)
        self.line_Display.setObjectName(u"line_Display")
        self.line_Display.setFrameShape(QFrame.Shape.HLine)
        self.line_Display.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Display)

        self.horizontalLayout_04 = QHBoxLayout()
        self.horizontalLayout_04.setObjectName(u"horizontalLayout_04")
        self.button_box = QRadioButton(self.verticalLayoutWidget_8)
        self.button_box.setObjectName(u"button_box")

        self.horizontalLayout_04.addWidget(self.button_box)

        self.button_mesh = QRadioButton(self.verticalLayoutWidget_8)
        self.button_mesh.setObjectName(u"button_mesh")

        self.horizontalLayout_04.addWidget(self.button_mesh)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_04)

        self.horizontalLayout_05 = QHBoxLayout()
        self.horizontalLayout_05.setObjectName(u"horizontalLayout_05")
        self.label_elementCount = QLabel(self.verticalLayoutWidget_8)
        self.label_elementCount.setObjectName(u"label_elementCount")

        self.horizontalLayout_05.addWidget(self.label_elementCount)

        self.spin_elementCount = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_elementCount.setObjectName(u"spin_elementCount")
        self.spin_elementCount.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_elementCount.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_elementCount.setWrapping(False)
        self.spin_elementCount.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_elementCount.setMaximum(100000)
        self.spin_elementCount.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_elementCount.setDisplayIntegerBase(10)

        self.horizontalLayout_05.addWidget(self.spin_elementCount)

        self.label_ViewDisplay = QLabel(self.verticalLayoutWidget_8)
        self.label_ViewDisplay.setObjectName(u"label_ViewDisplay")

        self.horizontalLayout_05.addWidget(self.label_ViewDisplay)

        self.spinBox_viewDisp = QSpinBox(self.verticalLayoutWidget_8)
        self.spinBox_viewDisp.setObjectName(u"spinBox_viewDisp")
        self.spinBox_viewDisp.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spinBox_viewDisp.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spinBox_viewDisp.setWrapping(False)
        self.spinBox_viewDisp.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox_viewDisp.setMaximum(100)
        self.spinBox_viewDisp.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spinBox_viewDisp.setDisplayIntegerBase(10)

        self.horizontalLayout_05.addWidget(self.spinBox_viewDisp)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_05)

        self.label_elemTransf = QLabel(self.verticalLayoutWidget_8)
        self.label_elemTransf.setObjectName(u"label_elemTransf")

        self.GeneralVertLayout.addWidget(self.label_elemTransf)

        self.line_Transform = QFrame(self.verticalLayoutWidget_8)
        self.line_Transform.setObjectName(u"line_Transform")
        self.line_Transform.setFrameShape(QFrame.Shape.HLine)
        self.line_Transform.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Transform)

        self.horizontalLayout_06 = QHBoxLayout()
        self.horizontalLayout_06.setObjectName(u"horizontalLayout_06")
        self.checkBox_random = QCheckBox(self.verticalLayoutWidget_8)
        self.checkBox_random.setObjectName(u"checkBox_random")

        self.horizontalLayout_06.addWidget(self.checkBox_random)

        self.button_seed = QPushButton(self.verticalLayoutWidget_8)
        self.button_seed.setObjectName(u"button_seed")

        self.horizontalLayout_06.addWidget(self.button_seed)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_06)

        self.label_position = QLabel(self.verticalLayoutWidget_8)
        self.label_position.setObjectName(u"label_position")

        self.GeneralVertLayout.addWidget(self.label_position)

        self.line_Posit = QFrame(self.verticalLayoutWidget_8)
        self.line_Posit.setObjectName(u"line_Posit")
        self.line_Posit.setFrameShape(QFrame.Shape.HLine)
        self.line_Posit.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Posit)

        self.horizontalLayout_07 = QHBoxLayout()
        self.horizontalLayout_07.setObjectName(u"horizontalLayout_07")
        self.label_PosX = QLabel(self.verticalLayoutWidget_8)
        self.label_PosX.setObjectName(u"label_PosX")

        self.horizontalLayout_07.addWidget(self.label_PosX)

        self.spacer__PosX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_07.addItem(self.spacer__PosX)

        self.spin_PxMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PxMin.setObjectName(u"spin_PxMin")
        self.spin_PxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PxMin.setWrapping(False)
        self.spin_PxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PxMin.setMaximum(999)
        self.spin_PxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PxMin.setDisplayIntegerBase(10)

        self.horizontalLayout_07.addWidget(self.spin_PxMin)

        self.spin_PxMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PxMax.setObjectName(u"spin_PxMax")
        self.spin_PxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PxMax.setWrapping(False)
        self.spin_PxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PxMax.setMaximum(999)
        self.spin_PxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PxMax.setDisplayIntegerBase(10)

        self.horizontalLayout_07.addWidget(self.spin_PxMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_07)

        self.horizontalLayout_08 = QHBoxLayout()
        self.horizontalLayout_08.setObjectName(u"horizontalLayout_08")
        self.label_PosY = QLabel(self.verticalLayoutWidget_8)
        self.label_PosY.setObjectName(u"label_PosY")
        self.label_PosY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_08.addWidget(self.label_PosY)

        self.spacer__PosY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_08.addItem(self.spacer__PosY)

        self.spin_PyMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PyMin.setObjectName(u"spin_PyMin")
        self.spin_PyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PyMin.setWrapping(False)
        self.spin_PyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PyMin.setMaximum(999)
        self.spin_PyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PyMin.setDisplayIntegerBase(10)

        self.horizontalLayout_08.addWidget(self.spin_PyMin)

        self.spin_PyMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PyMax.setObjectName(u"spin_PyMax")
        self.spin_PyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PyMax.setWrapping(False)
        self.spin_PyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PyMax.setMaximum(999)
        self.spin_PyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PyMax.setDisplayIntegerBase(10)

        self.horizontalLayout_08.addWidget(self.spin_PyMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_08)

        self.horizontalLayout_09 = QHBoxLayout()
        self.horizontalLayout_09.setObjectName(u"horizontalLayout_09")
        self.label_PosZ = QLabel(self.verticalLayoutWidget_8)
        self.label_PosZ.setObjectName(u"label_PosZ")
        self.label_PosZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_09.addWidget(self.label_PosZ)

        self.spacer_PosZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_09.addItem(self.spacer_PosZ)

        self.spin_PzMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PzMin.setObjectName(u"spin_PzMin")
        self.spin_PzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PzMin.setWrapping(False)
        self.spin_PzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PzMin.setMaximum(999)
        self.spin_PzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PzMin.setDisplayIntegerBase(10)

        self.horizontalLayout_09.addWidget(self.spin_PzMin)

        self.spin_PzMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_PzMax.setObjectName(u"spin_PzMax")
        self.spin_PzMax.setEnabled(True)
        self.spin_PzMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_PzMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_PzMax.setAutoFillBackground(False)
        self.spin_PzMax.setWrapping(False)
        self.spin_PzMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_PzMax.setMaximum(999)
        self.spin_PzMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_PzMax.setDisplayIntegerBase(10)

        self.horizontalLayout_09.addWidget(self.spin_PzMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_09)

        self.label_rotation = QLabel(self.verticalLayoutWidget_8)
        self.label_rotation.setObjectName(u"label_rotation")

        self.GeneralVertLayout.addWidget(self.label_rotation)

        self.line_Rot = QFrame(self.verticalLayoutWidget_8)
        self.line_Rot.setObjectName(u"line_Rot")
        self.line_Rot.setFrameShape(QFrame.Shape.HLine)
        self.line_Rot.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Rot)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_RosX = QLabel(self.verticalLayoutWidget_8)
        self.label_RosX.setObjectName(u"label_RosX")

        self.horizontalLayout_10.addWidget(self.label_RosX)

        self.spacer_RotX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.spacer_RotX)

        self.spin_RxMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RxMin.setObjectName(u"spin_RxMin")
        self.spin_RxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RxMin.setWrapping(False)
        self.spin_RxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RxMin.setMaximum(360)
        self.spin_RxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RxMin.setDisplayIntegerBase(10)

        self.horizontalLayout_10.addWidget(self.spin_RxMin)

        self.spin_RxMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RxMax.setObjectName(u"spin_RxMax")
        self.spin_RxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RxMax.setWrapping(False)
        self.spin_RxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RxMax.setMaximum(360)
        self.spin_RxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RxMax.setDisplayIntegerBase(10)

        self.horizontalLayout_10.addWidget(self.spin_RxMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_RosY = QLabel(self.verticalLayoutWidget_8)
        self.label_RosY.setObjectName(u"label_RosY")
        self.label_RosY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_11.addWidget(self.label_RosY)

        self.spacer_RotY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.spacer_RotY)

        self.spin_RyMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RyMin.setObjectName(u"spin_RyMin")
        self.spin_RyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RyMin.setWrapping(False)
        self.spin_RyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RyMin.setMaximum(360)
        self.spin_RyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RyMin.setDisplayIntegerBase(10)

        self.horizontalLayout_11.addWidget(self.spin_RyMin)

        self.spin_RyMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RyMax.setObjectName(u"spin_RyMax")
        self.spin_RyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RyMax.setWrapping(False)
        self.spin_RyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RyMax.setMaximum(360)
        self.spin_RyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RyMax.setDisplayIntegerBase(10)

        self.horizontalLayout_11.addWidget(self.spin_RyMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_RosZ = QLabel(self.verticalLayoutWidget_8)
        self.label_RosZ.setObjectName(u"label_RosZ")
        self.label_RosZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_12.addWidget(self.label_RosZ)

        self.spacer_RotZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.spacer_RotZ)

        self.spin_RzMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RzMin.setObjectName(u"spin_RzMin")
        self.spin_RzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RzMin.setWrapping(False)
        self.spin_RzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RzMin.setMaximum(360)
        self.spin_RzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RzMin.setDisplayIntegerBase(10)

        self.horizontalLayout_12.addWidget(self.spin_RzMin)

        self.spin_RzMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_RzMax.setObjectName(u"spin_RzMax")
        self.spin_RzMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_RzMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_RzMax.setWrapping(False)
        self.spin_RzMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_RzMax.setMaximum(360)
        self.spin_RzMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_RzMax.setDisplayIntegerBase(10)

        self.horizontalLayout_12.addWidget(self.spin_RzMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_12)

        self.label_scale = QLabel(self.verticalLayoutWidget_8)
        self.label_scale.setObjectName(u"label_scale")

        self.GeneralVertLayout.addWidget(self.label_scale)

        self.line_Scale = QFrame(self.verticalLayoutWidget_8)
        self.line_Scale.setObjectName(u"line_Scale")
        self.line_Scale.setFrameShape(QFrame.Shape.HLine)
        self.line_Scale.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_Scale)

        self.checkBox_proportionalScale = QCheckBox(self.verticalLayoutWidget_8)
        self.checkBox_proportionalScale.setObjectName(u"checkBox_proportionalScale")

        self.GeneralVertLayout.addWidget(self.checkBox_proportionalScale)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_EscX = QLabel(self.verticalLayoutWidget_8)
        self.label_EscX.setObjectName(u"label_EscX")

        self.horizontalLayout_13.addWidget(self.label_EscX)

        self.spacer_EscX = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.spacer_EscX)

        self.spin_SxMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SxMin.setObjectName(u"spin_SxMin")
        self.spin_SxMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SxMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SxMin.setWrapping(False)
        self.spin_SxMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SxMin.setMaximum(999)
        self.spin_SxMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SxMin.setDisplayIntegerBase(10)

        self.horizontalLayout_13.addWidget(self.spin_SxMin)

        self.spin_SxMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SxMax.setObjectName(u"spin_SxMax")
        self.spin_SxMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SxMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SxMax.setWrapping(False)
        self.spin_SxMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SxMax.setMaximum(999)
        self.spin_SxMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SxMax.setDisplayIntegerBase(10)

        self.horizontalLayout_13.addWidget(self.spin_SxMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_EscY = QLabel(self.verticalLayoutWidget_8)
        self.label_EscY.setObjectName(u"label_EscY")
        self.label_EscY.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_14.addWidget(self.label_EscY)

        self.spacer_EscY = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.spacer_EscY)

        self.spin_SyMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SyMin.setObjectName(u"spin_SyMin")
        self.spin_SyMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SyMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SyMin.setWrapping(False)
        self.spin_SyMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SyMin.setMaximum(999)
        self.spin_SyMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SyMin.setDisplayIntegerBase(10)

        self.horizontalLayout_14.addWidget(self.spin_SyMin)

        self.spin_SyMax = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SyMax.setObjectName(u"spin_SyMax")
        self.spin_SyMax.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SyMax.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SyMax.setWrapping(False)
        self.spin_SyMax.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SyMax.setMaximum(999)
        self.spin_SyMax.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SyMax.setDisplayIntegerBase(10)

        self.horizontalLayout_14.addWidget(self.spin_SyMax)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_EscZ = QLabel(self.verticalLayoutWidget_8)
        self.label_EscZ.setObjectName(u"label_EscZ")
        self.label_EscZ.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout_15.addWidget(self.label_EscZ)

        self.spacer_EscZ = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.spacer_EscZ)

        self.spin_SzMin = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SzMin.setObjectName(u"spin_SzMin")
        self.spin_SzMin.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SzMin.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SzMin.setWrapping(False)
        self.spin_SzMin.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SzMin.setMaximum(999)
        self.spin_SzMin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SzMin.setDisplayIntegerBase(10)

        self.horizontalLayout_15.addWidget(self.spin_SzMin)

        self.spin_SxMax_2 = QSpinBox(self.verticalLayoutWidget_8)
        self.spin_SxMax_2.setObjectName(u"spin_SxMax_2")
        self.spin_SxMax_2.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.spin_SxMax_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.spin_SxMax_2.setWrapping(False)
        self.spin_SxMax_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spin_SxMax_2.setMaximum(999)
        self.spin_SxMax_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.spin_SxMax_2.setDisplayIntegerBase(10)

        self.horizontalLayout_15.addWidget(self.spin_SxMax_2)


        self.GeneralVertLayout.addLayout(self.horizontalLayout_15)

        self.Button_update = QPushButton(self.verticalLayoutWidget_8)
        self.Button_update.setObjectName(u"Button_update")

        self.GeneralVertLayout.addWidget(self.Button_update)

        self.label_about = QLabel(self.verticalLayoutWidget_8)
        self.label_about.setObjectName(u"label_about")

        self.GeneralVertLayout.addWidget(self.label_about)

        self.line_about = QFrame(self.verticalLayoutWidget_8)
        self.line_about.setObjectName(u"line_about")
        self.line_about.setFrameShape(QFrame.Shape.HLine)
        self.line_about.setFrameShadow(QFrame.Shadow.Sunken)

        self.GeneralVertLayout.addWidget(self.line_about)

        self.label_version = QLabel(self.verticalLayoutWidget_8)
        self.label_version.setObjectName(u"label_version")

        self.GeneralVertLayout.addWidget(self.label_version)

        ScatterToolUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ScatterToolUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1478, 33))
        ScatterToolUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ScatterToolUI)
        self.statusbar.setObjectName(u"statusbar")
        ScatterToolUI.setStatusBar(self.statusbar)

        self.retranslateUi(ScatterToolUI)

        QMetaObject.connectSlotsByName(ScatterToolUI)
    # setupUi

    def retranslateUi(self, ScatterToolUI):
        ScatterToolUI.setWindowTitle(QCoreApplication.translate("ScatterToolUI", u"MainWindow", None))
        self.label_dmethod.setText(QCoreApplication.translate("ScatterToolUI", u"Distribution Method", None))
        self.button_spline.setText(QCoreApplication.translate("ScatterToolUI", u"Spline", None))
        self.button_surface.setText(QCoreApplication.translate("ScatterToolUI", u"Surface", None))
        self.button_pickSpline.setText(QCoreApplication.translate("ScatterToolUI", u"Pick Spline", None))
        self.button_pickSurface.setText(QCoreApplication.translate("ScatterToolUI", u"Pick Surface", None))
        self.label_delements.setText(QCoreApplication.translate("ScatterToolUI", u"Distribute Elements", None))
        self.pushButton_addList.setText(QCoreApplication.translate("ScatterToolUI", u"Add List", None))
        self.pushButton_add.setText(QCoreApplication.translate("ScatterToolUI", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("ScatterToolUI", u"Delete", None))
        self.pushButton_replace.setText(QCoreApplication.translate("ScatterToolUI", u"Replace", None))
        self.label_percent.setText(QCoreApplication.translate("ScatterToolUI", u" %", None))
        self.label_display.setText(QCoreApplication.translate("ScatterToolUI", u"Display", None))
        self.button_box.setText(QCoreApplication.translate("ScatterToolUI", u"Box", None))
        self.button_mesh.setText(QCoreApplication.translate("ScatterToolUI", u"Mesh", None))
        self.label_elementCount.setText(QCoreApplication.translate("ScatterToolUI", u"Elem Count", None))
        self.label_ViewDisplay.setText(QCoreApplication.translate("ScatterToolUI", u"Viewport Display %", None))
        self.label_elemTransf.setText(QCoreApplication.translate("ScatterToolUI", u"Elements Transform", None))
        self.checkBox_random.setText(QCoreApplication.translate("ScatterToolUI", u"Random", None))
        self.button_seed.setText(QCoreApplication.translate("ScatterToolUI", u"Seed", None))
        self.label_position.setText(QCoreApplication.translate("ScatterToolUI", u"Position", None))
        self.label_PosX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_PosY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_PosZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.label_rotation.setText(QCoreApplication.translate("ScatterToolUI", u"Rotation", None))
        self.label_RosX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_RosY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_RosZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.label_scale.setText(QCoreApplication.translate("ScatterToolUI", u"Scale", None))
        self.checkBox_proportionalScale.setText(QCoreApplication.translate("ScatterToolUI", u"Proportional Scale", None))
        self.label_EscX.setText(QCoreApplication.translate("ScatterToolUI", u"X", None))
        self.label_EscY.setText(QCoreApplication.translate("ScatterToolUI", u"Y", None))
        self.label_EscZ.setText(QCoreApplication.translate("ScatterToolUI", u"Z", None))
        self.Button_update.setText(QCoreApplication.translate("ScatterToolUI", u"Update", None))
        self.label_about.setText(QCoreApplication.translate("ScatterToolUI", u"About", None))
        self.label_version.setText(QCoreApplication.translate("ScatterToolUI", u"Scatter Tool Version 0.0.0", None))
    # retranslateUi

