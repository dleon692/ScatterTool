import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
from PySide2 import QtWidgets,QtCore
from ui_scattertool_UI import Ui_ScatterToolUI
from scattertool import ScatterTool,ElementsManager
from pymxs import runtime as rt
from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QButtonGroup
import random

class ScatterToolApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ScatterToolApp, self).__init__(parent=None)
        self.ui = Ui_ScatterToolUI()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        #create group for mode selection
        self.distribution_group = QButtonGroup(self)
        self.distribution_group.addButton(self.ui.button_spline)
        self.distribution_group.addButton(self.ui.button_surface)

        #create scatter tool instance
        self.scatter_tool = ScatterTool()

        #connect mode buttons
        self.ui.button_spline.toggled.connect(self.mode_buttons)
        self.ui.button_surface.toggled.connect(self.mode_buttons)

        #connect box/mesh view buttons
        self.mode_buttons()

        self.ui.button_spline.setChecked(True)
        self.ui.button_mesh.setChecked(True)

        #elements manager to handle source objects.
        self.manager = ElementsManager()
        self.source_obj = None

        #show elements in the list widget.
        self.elements = []  # Your elements list
        self.model = QStringListModel()
        self.ui.ListElements.setModel(self.model)

        # turn off randomization controls by default
        self.ui.checkBox_random.setChecked(False)
        self.on_toggle_random(False)
        self.ui.checkBox_random.stateChanged.connect(lambda state: self.on_toggle_random(state == 2))
        self.ui.checkBox_proportionalScale.stateChanged.connect(self.on_toggle_random)



        self.setup_connections()
    
    def refresh_listview(self):
        self.elements = [obj.name for obj in self.manager.get_all()]
        self.model.setStringList(self.elements)
        
    def setup_connections(self):
        self.ui.button_pickSpline.clicked.connect(self.on_pick_spline)
        self.ui.button_pickSurface.clicked.connect(self.on_pick_surface)
        self.ui.pushButton_add.clicked.connect(self.on_add)
        self.ui.pushButton_delete.clicked.connect(self.on_delete)
        self.ui.pushButton_replace.clicked.connect(self.on_replace)
        self.ui.pushButton_addList.clicked.connect(self.on_add_list)
        self.ui.button_seed.clicked.connect(self.on_seed_clicked)
        self.ui.Button_update.clicked.connect(self.on_update)
    
    # Handle mode button toggles

    def mode_buttons(self):
        if self.ui.button_spline.isChecked():
            self.ui.button_pickSpline.setEnabled(True)
            self.ui.button_pickSurface.setEnabled(False)
            self.scatter_tool.set_surface(None)
        elif self.ui.button_surface.isChecked():
            self.ui.button_pickSurface.setEnabled(True)
            self.ui.button_pickSpline.setEnabled(False)
            self.scatter_tool.set_spline(None)

    # Handle display elements as box or mesh
    def on_box_view(self):
        if self.ui.button_box.isChecked():
            self.scatter_tool.set_display_as_box(True)
            self.ui.button_mesh.setChecked(False)
        else:
            self.scatter_tool.set_display_as_box(False)
            self.ui.button_mesh.setChecked(False)
    
    # Pick spline or surface from the scene
    def on_pick_spline(self):
        try:
            # Selecciona un objeto de la escena
            picked = rt.pickObject(prompt="Pick a spline")
            if not picked:
                self.ui.button_pickSpline.setText("No object selected.")
                return

            # Verifica si es un SplineShape; si no, lo convierte
            if rt.classOf(picked) != rt.SplineShape:
                try:
                    picked = rt.convertToSplineShape(picked)
                    print(f"Converted to SplineShape: {picked.name}")
                except RuntimeError:
                    self.ui.button_pickSpline.setText("Cannot convert to SplineShape.")
                    return

            # Asigna el spline al ScatterTool
            self.scatter_tool.set_spline(picked)
            self.ui.button_pickSpline.setText(f"Spline: {picked.name}")

        except RuntimeError:
            self.ui.button_pickSpline.setText("Pick canceled or invalid object.")
                
    def on_pick_surface(self):
        selection = rt.selection
        if selection.count > 0 and rt.isKindOf(selection[0], rt.GeometryClass):
            self.scatter_tool.set_surface(selection[0])
            self.ui.button_pickSurface.setText(f"Surface: {selection[0].name}")
        else:
            self.ui.button_pickSurface.setText("Select a valid Surface in viewport first.")
    
    # Manage source objects list

    def on_add(self):
        picked_obj = rt.selection[0] if rt.selection.count > 0 else None
        if picked_obj:
            self.manager.add(picked_obj)
            self.refresh_listview()

    def on_delete(self):
        selected_indexes = self.ui.ListElements.selectedIndexes()
        if selected_indexes:
            selected_name = selected_indexes[0].data()
            obj_to_remove = next((obj for obj in self.manager.get_all() if obj.name == selected_name), None)
            if obj_to_remove:
                self.manager.remove(obj_to_remove)
                self.refresh_listview()

    def on_replace(self):
        selected_indexes = self.ui.ListElements.selectedIndexes()
        picked_obj = rt.selection[0] if rt.selection.count > 0 else None
        if selected_indexes and picked_obj:
            selected_name = selected_indexes[0].data()
            old_obj = next((obj for obj in self.manager.get_all() if obj.name == selected_name), None)
            if old_obj:
                self.manager.replace(old_obj, picked_obj)
                self.refresh_listview()

    def on_add_list(self):
        selected_objs = list(rt.selection)
        if selected_objs:
            self.manager.add_many(selected_objs)
            self.refresh_listview()
    
    # Randomization seed button

    def on_seed_clicked(self):
        self.on_update()
    
    # Enable/disable randomization controls based on checkbox state
    
    def on_toggle_random(self,enabled):
        enabled= self.ui.checkBox_random.isChecked()

        self.ui.button_seed.setEnabled(enabled)
        self.ui.spin_PxMin.setEnabled(enabled)
        self.ui.spin_PxMax.setEnabled(enabled)
        self.ui.spin_PyMin.setEnabled(enabled)
        self.ui.spin_PyMax.setEnabled(enabled)
        self.ui.spin_PzMin.setEnabled(enabled)
        self.ui.spin_PzMax.setEnabled(enabled)
        self.ui.spin_RxMin.setEnabled(enabled)
        self.ui.spin_RxMax.setEnabled(enabled)
        self.ui.spin_RyMin.setEnabled(enabled)
        self.ui.spin_RyMax.setEnabled(enabled)
        self.ui.spin_RzMin.setEnabled(enabled)
        self.ui.spin_RzMax.setEnabled(enabled)
        self.ui.spin_SxMin.setEnabled(enabled)
        self.ui.spin_SxMax.setEnabled(enabled)
        if self.ui.checkBox_proportionalScale.isChecked() and enabled:
            self.ui.spin_SyMin.setEnabled(False)
            self.ui.spin_SyMax.setEnabled(False)
            self.ui.spin_SzMin.setEnabled(False)
            self.ui.spin_SxMax_2.setEnabled(False)
        else:
            self.ui.spin_SyMin.setEnabled(enabled)
            self.ui.spin_SyMax.setEnabled(enabled)
            self.ui.spin_SzMin.setEnabled(enabled)
            self.ui.spin_SxMax_2.setEnabled(enabled)
  

    #launch the scatter function

    def on_update(self):
        source_obj = self.manager.get_random()
        spline_obj = self.scatter_tool.spline
        source_surface = self.scatter_tool.surface
        distance = None #self.ui.spinBox_distance.value()
        count = self.ui.spin_elementCount.value()

        #check if randomization is False
        if self.ui.checkBox_random.isChecked():
            pos_jitterX =random.uniform(self.ui.spin_PxMin.value(),self.ui.spin_PxMax.value())
            pos_jitterY =random.uniform(self.ui.spin_PyMin.value(),self.ui.spin_PyMax.value())
            pos_jitterZ =random.uniform(self.ui.spin_PzMin.value(),self.ui.spin_PzMax.value())

            if self.ui.checkBox_proportionalScale.isChecked():
                scale_rangeX=scale_rangeY=scale_rangeZ=(self.ui.spin_SxMin.value(),self.ui.spin_SxMax.value())
            else:
                scale_rangeX = (self.ui.spin_SxMin.value(), self.ui.spin_SxMax.value())
                scale_rangeY = (self.ui.spin_SyMin.value(), self.ui.spin_SyMax.value())
                scale_rangeZ = (self.ui.spin_SzMin.value(), self.ui.spin_SxMax_2.value())

            rot_x_range = (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value())
            rot_y_range = (self.ui.spin_RyMin.value(), self.ui.spin_RyMax.value())
            rot_z_range = (self.ui.spin_RzMin.value(), self.ui.spin_RzMax.value())
        else:
            pos_jitterX = pos_jitterY = pos_jitterZ = 0.0
            scale_rangeX = scale_rangeY = scale_rangeZ = (1.0, 1.0)
            rot_x_range = rot_y_range = rot_z_range = (0.0, 0.0)

        #check if spline or surface mode is selected
            
        if self.ui.button_spline.isChecked():
            self.ui.button_pickSurface.setEnabled(False)
            self.scatter_tool.scatter_spline(source_obj, spline_obj,
                                  distance,
                                  count,
                                  pos_jitter=rt.point3(pos_jitterX, pos_jitterY, pos_jitterZ),
                                  scale_rangeX=scale_rangeX,
                                  scale_rangeY=scale_rangeY,
                                  scale_rangeZ=scale_rangeZ,
                                  rot_x_range=rot_x_range,
                                  rot_y_range=rot_y_range,
                                  rot_z_range=rot_z_range)
        else:
            self.ui.button_pickSpline.setEnabled(False)
            self.scatter_tool.scatter_surface(source_obj, source_surface,
                                  count,
                                  scale_rangeX=scale_rangeX,
                                  scale_rangeY=scale_rangeY,
                                  scale_rangeZ=scale_rangeZ,
                                  rot_x_range=rot_x_range,
                                  rot_y_range=rot_y_range,
                                  rot_z_range=rot_z_range)
_WINDOW = None
def launch():
    global _WINDOW
    app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
    if _WINDOW is None or not _WINDOW.isVisible():
        _WINDOW = ScatterToolApp()
    _WINDOW.show()
    _WINDOW.raise_()  # trae al frente
    return _WINDOW

if __name__ == "__main__":
    launch()