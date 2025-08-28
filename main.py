from PySide6 import QtWidgets
from ui_window import Ui_ScatterToolUI
from scatter_tool import ScatterTool
from scatter_tool import ElementsManager
from pymxs import runtime as rt
from PySide6.QtCore import QStringListModel
import random

class ScatterToolApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(ScatterToolApp, self).__init__()
        self.ui = Ui_ScatterToolUI()
        self.ui.setupUi(self)
        self.ui.button_mesh.setChecked(True)
        self.scatter_tool = ScatterTool()
        """elements manager to handle source objects."""
        self.manager = ElementsManager()
        self.source_obj = None
        """show elements in the list widget."""
        self.elements = []  # Your elements list
        self.model = QStringListModel()
        self.ui.ListElements.setModel(self.model)
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

    def on_box_view(self):
        if self.ui.button_box.ischecked():
            self.scatter_tool.set_display_as_box(True)
            self.ui.button_mesh.setChecked(False)
        else:
            self.scatter_tool.set_display_as_box(False)
            self.ui.button_mesh.setChecked(False)
    def on_pick_spline(self):
        spline = rt.selection[0] if rt.selection.count > 0 else None
        if spline and rt.isKindOf(spline, rt.SplineShape):
            self.scatter_tool.set_spline(spline)
            self.ui.splineLabel.setText(f"Spline: {spline.name}")
        else:
            self.ui.splineLabel.setText("No valid spline selected.")

    def on_pick_surface(self):
        mesh = rt.selection[0] if rt.selection.count > 0 else None
        if mesh and rt.isKindOf(mesh, rt.GeometryClass):
            self.scatter_tool.set_mesh(mesh)
            self.ui.meshLabel.setText(f"Mesh: {mesh.name}")
        else:
            self.ui.meshLabel.setText("No valid mesh selected.")

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

    def on_seed_clicked(self):
        self.on_update()

    def on_toggle_random(self):
        self.ui.button_seed.setEnabled(False)
        self.ui.spinBox_Px_min.setEnabled(False)
        self.ui.spinBox_Px_max.setEnabled(False)
        self.ui.spinBox_Py_min.setEnabled(False)
        self.ui.spinBox_Py_max.setEnabled(False)
        self.ui.spinBox_Pz_min.setEnabled(False)
        self.ui.spinBox_Pz_max.setEnabled(False)
        self.ui.spinBox_scaleX_min.setEnabled(False)
        self.ui.spinBox_scaleX_max.setEnabled(False)
        self.ui.spinBox_scaleY_min.setEnabled(False)
        self.ui.spinBox_scaleY_max.setEnabled(False)
        self.ui.spinBox_scaleZ_min.setEnabled(False)
        self.ui.spinBox_scaleZ_max.setEnabled(False)
        self.ui.spinBox_rotX_min.setEnabled(False)
        self.ui.spinBox_rotX_max.setEnabled(False)
        self.ui.spinBox_rotY_min.setEnabled(False)
        self.ui.spinBox_rotY_max.setEnabled(False)
        self.ui.spinBox_rotZ_min.setEnabled(False)
        self.ui.spinBox_rotZ_max.setEnabled(False)

    #launch the scatter function

    def on_update(self):
        source_obj = self.manager.get_random()
        spline_obj = self.scatter_tool.spline
        source_surface = self.scatter_tool.mesh
        distance = None #self.ui.spinBox_distance.value()
        count = self.ui.spin_elementCount.value()

        #check if randomization is False
        if self.ui.checkBox_random.ischecked():
            pos_jitterX =random.uniform(self.ui.spin_PxMin.value(),self.ui.spin_PxMax.value())
            pos_jitterY =random.uniform(self.ui.spin_PyMin.value(),self.ui.spin_PyMax.value())
            pos_jitterZ =random.uniform(self.ui.spin_PzMin.value(),self.ui.spin_PzMax.value())

            if self.ui.checkBox_proportionalScale.isChecked():
                scale_rangeX=scale_rangeY=scale_rangeZ=(self.ui.spin_SxMin.value(),self.ui.spin_SxMax.value())
                self.ui.spinBox_scaleY_min.setEnabled(False)
                self.ui.spinBox_scaleY_max.setEnabled(False)
                self.ui.spinBox_scaleZ_min.setEnabled(False)
                self.ui.spinBox_scaleZ_max.setEnabled(False)
            else:
                scale_rangeX = (self.ui.spin_SxMin.value(), self.ui.spin_SxMax.value())
                scale_rangeY = (self.ui.spin_SyMin.value(), self.ui.spin_SyMax.value())
                scale_rangeZ = (self.ui.spin_SzMin.value(), self.ui.spin_SzMax.value())

            rot_x_range = (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value())
            rot_y_range = (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value())
            rot_z_range = (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value())
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
            self.ui.button_pickspline.setEnabled(False)
            self.scatter_tool.scatter_surface(source_obj, source_surface,
                                  count,
                                  scale_rangeX=scale_rangeX,
                                  scale_rangeY=scale_rangeY,
                                  scale_rangeZ=scale_rangeZ,
                                  rot_x_range=rot_x_range,
                                  rot_y_range=rot_y_range,
                                  rot_z_range=rot_z_range)