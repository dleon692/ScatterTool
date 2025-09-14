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
        self.distribution_group.setExclusive(True)

        self.pending_target = None   #temp target object before creating the group
        self.pending_mode = None     #temp mode before creating the group

        #create scatter tool instance
        self.scatter_tool = ScatterTool()

        self.current_group = None

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

    # --------------------------- UI & list handling ---------------------------
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
        self.ui.button_shuffle.clicked.connect(self.on_shuffle_clicked)
        self.ui.Button_update.clicked.connect(self.on_update)
    
   # --------------------------- Mode buttons ---------------------------

    def mode_buttons(self):
        if self.ui.button_spline.isChecked():
            self.ui.button_pickSpline.setEnabled(True)
            self.ui.button_pickSurface.setEnabled(False)
             
        else:
            
            self.ui.button_pickSurface.setEnabled(True)
            self.ui.button_pickSpline.setEnabled(False)

     # --------------------------- Box / Mesh View ---------------------------# 
    def on_box_view(self):
        if self.current_group:
            self.current_group.set_display_as_box(self.ui.button_box.isChecked())
        self.ui.button_mesh.setChecked(not self.ui.button_box.isChecked())

    # --------------------------- Pick spline / surface ---------------------------
    def on_pick_spline(self):
        selection = rt.selection
        if selection.count > 0 and rt.superClassOf(selection[0]) == rt.Shape:
            shape=selection[0]
            self.pending_target=shape
            self.pending_mode="spline"
            self.ui.button_pickSpline.setText(f"Spline: {shape.name}")
        else:
            self.ui.button_pickSpline.setText("ERROR: Select a valid Spline.")        

    def on_pick_surface(self):
        selection = rt.selection
        if selection.count > 0 and rt.isKindOf(selection[0], rt.GeometryClass):
            surface=selection[0]
            self.pending_target=surface
            self.pending_mode="surface"
            self.ui.button_pickSurface.setText(f"Surface: {surface.name}")  
        else:
            self.ui.button_pickSurface.setText("ERROR:Select a valid Surface.")
    
    # --------------------------- Elements list management ---------------------------

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
    
    # --------------------------- Randomization ---------------------------

    def on_shuffle_clicked(self):
        elements = self.manager.get_all()
        if not elements:
            print("No elements to shuffle.")
            return
        random.shuffle(elements)
        self.manager.elements = elements
        self.refresh_listview()
        print("Elements shuffled.")
    # Enable/disable randomization controls based on checkbox state
    
    def on_toggle_random(self,enabled):
        enabled= self.ui.checkBox_random.isChecked()

        self.ui.button_shuffle.setEnabled(enabled)
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
            self.ui.spin_SzMax.setEnabled(False)
        else:
            self.ui.spin_SyMin.setEnabled(enabled)
            self.ui.spin_SyMax.setEnabled(enabled)
            self.ui.spin_SzMin.setEnabled(enabled)
            self.ui.spin_SzMax.setEnabled(enabled)
  

    # --------------------------- Launch scatter ---------------------------

    def on_update(self):
               
        source_obj = self.manager.get_random()
        if not source_obj:
            print("No source object selected.")
            return
        
        mode = "spline" if self.ui.button_spline.isChecked() else "surface"
        # ------------- Gather parameters from UI -------------
        count = self.ui.spin_elementCount.value()
        distance = None  # Opcional: self.ui.spinBox_distance.value()

        #check if randomization is False
        if self.ui.checkBox_random.isChecked():
            pos_jitterX = random.uniform(self.ui.spin_PxMin.value(), self.ui.spin_PxMax.value())
            pos_jitterY = random.uniform(self.ui.spin_PyMin.value(), self.ui.spin_PyMax.value())
            pos_jitterZ = random.uniform(self.ui.spin_PzMin.value(), self.ui.spin_PzMax.value())

            if self.ui.checkBox_proportionalScale.isChecked():
                scale_rangeX = scale_rangeY = scale_rangeZ = (
                    self.ui.spin_SxMin.value()/100,
                    self.ui.spin_SxMax.value()/100
                )
            else:
                scale_rangeX = (self.ui.spin_SxMin.value()/100, self.ui.spin_SxMax.value()/100)
                scale_rangeY = (self.ui.spin_SyMin.value()/100, self.ui.spin_SyMax.value()/100)
                scale_rangeZ = (self.ui.spin_SzMin.value()/100, self.ui.spin_SzMax.value()/100)

            rot_x_range = (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value())
            rot_y_range = (self.ui.spin_RyMin.value(), self.ui.spin_RyMax.value())
            rot_z_range = (self.ui.spin_RzMin.value(), self.ui.spin_RzMax.value())
        else:
            pos_jitterX = pos_jitterY = pos_jitterZ = 0.0
            scale_rangeX = scale_rangeY = scale_rangeZ = (1.0, 1.0)
            rot_x_range = rot_y_range = rot_z_range = (0.0, 0.0)

        #store parameters
        params_dict={
            "count": count,
            "distance": distance,
            "pos_jitter": rt.point3(pos_jitterX, pos_jitterY, pos_jitterZ),
            "scale_rangeX": scale_rangeX,
            "scale_rangeY": scale_rangeY,
            "scale_rangeZ": scale_rangeZ,
            "rot_x_range": rot_x_range,
            "rot_y_range": rot_y_range,
            "rot_z_range": rot_z_range,
            "source_obj": source_obj
        }
       
        # Check if there's a selected group in the scene
        selected_group = self.scatter_tool.get_group_by_selection()
        if selected_group:
            self.current_group = selected_group
            print(f"DEBUG: Using existing group: {self.current_group.name}")#DEBUG
        # ------------- Create or update group -------------
        if self.current_group is None:
            if self.pending_target is None or self.pending_mode != mode:
                raise ValueError("You must pick a valid target (Spline or Surface) before updating scatter.")
            target_obj = self.pending_target    

        
        # ------------- Create group dynamically -------------
            self.current_group = self.scatter_tool.create_group(
                source_obj=source_obj,
                target_obj=target_obj,
                mode=mode
            )
            print(f"DEBUG:Created new group with target: {target_obj.name} in mode: {mode}")#DEBUG
        # ------------- Update parameters and scatter -------------
        self.current_group.params.update(params_dict)
        
        if mode == "spline":
            self.current_group.scatter_spline(source_obj)
        else:
            self.current_group.scatter_surface(source_obj)

# --------------------------- Launch window ---------------------------            
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