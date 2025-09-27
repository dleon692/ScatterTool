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
import builtins

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
        self.ui.button_spline.toggled.connect(self.mode_buttons)
        self.ui.button_surface.toggled.connect(self.mode_buttons)

        self.pending_target = None   #temp target object before creating the group
        self.pending_mode = None     #temp mode before creating the group

        #create scatter tool instance
        self.scatter_tool = ScatterTool()

        self.current_group = None

        #Default view mode
        self.ui.button_box.setChecked(False) 
        self.ui.button_mesh.setChecked(True) 

        #connect box/mesh view buttons
        self.ui.button_box.toggled.connect(self.on_box_view)
        self.ui.button_mesh.toggled.connect(self.on_box_view)
        
        #default selections
        self.ui.button_spline.setChecked(True)
        self.ui.button_mesh.setChecked(True)

        #default count
        self.ui.spin_elementCount.setValue(5)
        
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
        self.ui.checkBox_proportionalScale.setChecked(True)
        #default scale values
        self.ui.spin_SxMin.setValue(100)
        self.ui.spin_SxMax.setValue(100)

        self.setup_connections()

        #selection callback
        try:
            ms_script = 'python.Execute "scattertool_app_instance._selection_changed_static()"'
            self._sel_cb_name = rt.Name('ScatterToolAppSelCallback')
            self.sel_callback = rt.callbacks.addScript(
                rt.Name('selectionSetChanged'),
                ms_script,
                id=self._sel_cb_name
                )
            print("DEBUG: Selection callback added successfully.")#DEBUG
        except Exception as e:
            print(f"Error adding selection callback: {e}")
        
        # Expose the application instance to builtins for access in the callback
        builtins.ScatterToolApp = ScatterToolApp
        builtins.scattertool_app_instance = self
  
    # --------------------------- UI & list handling ---------------------------
    def refresh_listview(self):
        self.manager.elements = [obj for obj in self.manager.get_all() if rt.isValidNode(obj)]
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

    # --------------------------- Selection callback ---------------------------
    @staticmethod
    def _selection_changed_static():
        try:

            app = getattr(builtins, "scattertool_app_instance", None)
            if app:
                app.on_selection_changed()
        except Exception as e:
            print(f"DEBUG: error en _selection_changed_static -> {e}")

    def on_selection_changed(self):
        """Automatically load group parameters if a group's dummy is selected."""
        sel = list(rt.selection)
        if not sel:
            return
        obj = sel[0]
        group = self.scatter_tool.get_group_by_controller(obj)

        if not group:
            self.current_group = None
            print("DEBUG: Selected object is not a group controller.")
            return

        self.current_group = group
        
        if group.manager is None:
            group.manager = ElementsManager()
        self.manager = group.manager
        self.refresh_listview()

        ctrl = group.controller
        if not ctrl or not rt.isValidNode(ctrl):
            print("DEBUG: Group controller invalid.")
            return
        # --- Buttons / checkboxes ---
        mode = rt.getUserProp(ctrl, "ScatterMode")
        self.ui.button_spline.setChecked(mode == "spline")
        self.ui.button_surface.setChecked(mode == "surface")
        # --- Checkboxes ---
        val_random = rt.getUserProp(ctrl, "ScatterRandom")
        random_enabled = val_random if isinstance(val_random, bool) else str(val_random).lower() == "true"
        self.ui.checkBox_random.setChecked(random_enabled)

        val_prop = rt.getUserProp(ctrl, "ScatterProportionalScale")
        proportional = val_prop if isinstance(val_prop, bool) else str(val_prop).lower() == "true"
        self.ui.checkBox_proportionalScale.setChecked(proportional)
       
        val_box = rt.getUserProp(ctrl, "ScatterDisplayAsBox")
        self.ui.button_box.setChecked(val_box if isinstance(val_box, bool) else str(val_box).lower() == "true")

        #test
        children = [c for c in rt.children(ctrl) if rt.isValidNode(c) and c.layer == ctrl.layer]
        if children:
            self.manager.clear()
            for child in children:
                self.manager.add(child)
            print(f"DEBUG: Repobladas {len(children)} instancias desde hijos en el layer {ctrl.layer.name}")
        #test



        # --- Numeric parameters ---
        # Count
        count = rt.getUserProp(ctrl, "ScatterCount")
        if count:
            self.ui.spin_elementCount.setValue(int(count))
        
        # Distance
        distance = rt.getUserProp(ctrl, "ScatterDistance")
        # TODO: if you have a spinbox for distance, set it here

        # Position jitter
        pos_jitter = rt.getUserProp(ctrl, "ScatterPosJitter")
        if pos_jitter:
            x, y, z = map(float, pos_jitter.split(","))
            self.ui.spin_PxMin.setValue(x)
            self.ui.spin_PxMax.setValue(x)
            self.ui.spin_PyMin.setValue(y)
            self.ui.spin_PyMax.setValue(y)
            self.ui.spin_PzMin.setValue(z)
            self.ui.spin_PzMax.setValue(z)

        # Scale ranges
        for axis, spin_min, spin_max, prop in [
            ("X", self.ui.spin_SxMin, self.ui.spin_SxMax, "ScatterScaleX"),
            ("Y", self.ui.spin_SyMin, self.ui.spin_SyMax, "ScatterScaleY"),
            ("Z", self.ui.spin_SzMin, self.ui.spin_SzMax, "ScatterScaleZ"),
        ]:
            val = rt.getUserProp(ctrl, prop)
            if val:
                min_val, max_val = map(float, val.split(","))
                spin_min.setValue(min_val*100)
                spin_max.setValue(max_val*100)

        # Rotation ranges
        for axis, spin_min, spin_max, prop in [
            ("X", self.ui.spin_RxMin, self.ui.spin_RxMax, "ScatterRotX"),
            ("Y", self.ui.spin_RyMin, self.ui.spin_RyMax, "ScatterRotY"),
            ("Z", self.ui.spin_RzMin, self.ui.spin_RzMax, "ScatterRotZ"),
        ]:
            val = rt.getUserProp(ctrl, prop)
            if val:
                min_val, max_val = map(float, val.split(","))
                spin_min.setValue(min_val)
                spin_max.setValue(max_val)

        # --- Source object ---
        elements_names = rt.getUserProp(ctrl, "ScatterElements")
        if elements_names:
            self.manager.clear()
            for name in elements_names.split(","):
                obj_node = rt.getNodeByName(name)
                if obj_node and rt.isValidNode(obj_node):
                    self.manager.add(obj_node)
        
        # --- Update internal params dict ---
        group.params.update({
            "count": self.ui.spin_elementCount.value(),
            "distance": float(distance) if distance else None,
            "pos_jitter": rt.point3(self.ui.spin_PxMin.value(), self.ui.spin_PyMin.value(), self.ui.spin_PzMin.value()),
            "scale_rangeX": (self.ui.spin_SxMin.value()/100, self.ui.spin_SxMax.value()/100),
            "scale_rangeY": (self.ui.spin_SyMin.value()/100, self.ui.spin_SyMax.value()/100),
            "scale_rangeZ": (self.ui.spin_SzMin.value()/100, self.ui.spin_SzMax.value()/100),
            "rot_x_range": (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value()),
            "rot_y_range": (self.ui.spin_RyMin.value(), self.ui.spin_RyMax.value()),
            "rot_z_range": (self.ui.spin_RzMin.value(), self.ui.spin_RzMax.value()),
            "source_obj": self.manager.get_random(),
            "proportional_scale": proportional,
            "random": random_enabled
        })

        # --- Debug output ---
        print(f"DEBUG: Loaded group '{group.name}' with parameters:")
        print(f"  Mode: {mode}")
        print(f"  Random: {random_enabled}")
        print(f"    scale: {proportional}")
        print(f"  Display as box: {self.ui.button_box.isChecked()}")
        print(f"  Count: {self.ui.spin_elementCount.value()}")
        print(f"  Distance: {distance}")
        print(f"  Pos jitter: {group.params['pos_jitter']}")
        print(f"  Scale ranges: X{group.params['scale_rangeX']}, Y{group.params['scale_rangeY']}, Z{group.params['scale_rangeZ']}")
        print(f"  Rotation ranges: X{group.params['rot_x_range']}, Y{group.params['rot_y_range']}, Z{group.params['rot_z_range']}")
        print(f"  Source objects: {[obj.name for obj in self.manager.get_all()]}")
 
        # --- Update spinboxes enabled/disabled according to random & proportional flags ---
        self.on_toggle_random(random_enabled) 
        if proportional and random_enabled:
            self.ui.spin_SyMin.setEnabled(False)
            self.ui.spin_SyMax.setEnabled(False)
            self.ui.spin_SzMin.setEnabled(False)
            self.ui.spin_SzMax.setEnabled(False)     



    # --------------------------- Cleanup callback ---------------------------
    def closeEvent(self, event):
        if hasattr(self, 'sel_callback') and self.sel_callback:
            try:
                rt.callbacks.removeScripts(rt.Name('selectionSetChanged'))
                print("DEBUG: Selection callback removed successfully.")  # CAMBIO: debug
            except Exception as e:
                print(f"Error removing callback: {e}")
  
        if hasattr(builtins, "scattertool_app_instance"):
            del builtins.scattertool_app_instance
        super().closeEvent(event)

     # --------------------------- Box / Mesh View ---------------------------# 
    def on_box_view(self,enable=True):
        """Toggle display as box for the currently selected group's instances."""
        enable = self.ui.button_box.isChecked() if enable is None else enable
        sel = list(rt.selection)
        if not sel:
            rt.messageBox(
                "Select the group's dummy controller first.",
                title="Scatter Tool Warning",
                button=rt.name("ok"),
                icon=rt.name("warning")
            )
            return
        
        obj = sel[0]
        # search for the group that has this controller
        group = self.scatter_tool.get_group_by_controller(obj)
        if not group:
            rt.messageBox(
                "Select the group's dummy controller first.",
                title="Scatter Tool Warning",
                button=rt.name("ok"),
                icon=rt.name("warning")
            )
            return

        print(f"DEBUG: on_box_view called. button_box={enable}")

        ctrl = group.controller
        if ctrl and rt.isValidNode(ctrl) and not group.manager.get_all():
            children = [c for c in rt.children(ctrl) if rt.isValidNode(c) and c.layer == ctrl.layer]
            if children:
                for child in children:
                    group.manager.add(child)
                print(f"DEBUG: Repobladas {len(children)} instancias desde hijos en el layer {ctrl.layer.name}")

        # set display mode
        try:
            group.set_display_as_box(enable)
            print(f"DEBUG: on_box_view -> Display mode changed to {'BOX' if enable else 'MESH'}")
            self.ui.button_mesh.blockSignals(True)
            self.ui.button_mesh.setChecked(not enable)
            self.ui.button_mesh.blockSignals(False)
        except Exception as e:
            # revert update button states if fail
            print(f"ERROR: set_display_as_box failed: {e}")
            self.ui.button_box.blockSignals(True)
            self.ui.button_box.setChecked(False)
            self.ui.button_box.blockSignals(False)

            self.ui.button_mesh.blockSignals(True)
            self.ui.button_mesh.setChecked(True)
            self.ui.button_mesh.blockSignals(False)
            return

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


            proportional = self.ui.checkBox_proportionalScale.isChecked()
            if proportional:
                scale_rangeX = (self.ui.spin_SxMin.value()/100, self.ui.spin_SxMax.value()/100)
                scale_rangeY = scale_rangeZ = scale_rangeX #same range for Y and Z
                
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
            proportional = False  # default to proportional if random is off 

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
            "source_obj": source_obj,
            "proportional_scale": proportional
        }
       
        # Check if there's a selected group in the scene
        selected_group = self.scatter_tool.get_group_by_selection()
        if selected_group:
            self.current_group = selected_group
            print(f"DEBUG: Using existing group: {self.current_group.name}")#DEBUG
            if self.current_group.manager is None:
                self.current_group.manager = ElementsManager()
            #load manager and UI for this group
            self.manager = self.current_group.manager
            self.refresh_listview()
        #------------- Update UI from current group -------------
            self.update_ui_from_group(self.current_group)
        else:
            # If no group is selected, ensure we have a target and mode picked
            if self.current_group is None:
                if self.pending_target is None or self.pending_mode != mode:
                    raise ValueError("You must pick a valid target (Spline or Surface) before updating scatter.")
        # ------------- Create group dynamically -------------
                self.current_group=self.scatter_tool.create_group(
                    source_obj=source_obj,
                    target_obj=self.pending_target,
                    mode=mode
                ) #placeholder to avoid errors
                print(f"DEBUG: Created new group: {self.current_group.name}")#DEBUG
                    
                if self.current_group.manager is None:
                    self.current_group.manager = self.manager   
                    
        # ------------- Update parameters and scatter -------------
        self.current_group.params.update(params_dict)

        # Reposition controller to target center
        if self.pending_target and rt.isValidNode(self.pending_target):
            target_bb_min, target_bb_max = rt.nodeGetBoundingBox(self.pending_target, rt.matrix3(1))
            self.current_group.controller.position = (target_bb_min + target_bb_max) / 2
        
        # Set display mode
        if mode == "spline":
            self.current_group.scatter_spline(self.current_group.params["source_obj"])
        else:
            self.current_group.scatter_surface(self.current_group.params["source_obj"])

        # ------------------- SAVE TO CONTROLLER -------------------
        ctrl = self.current_group.controller 
        if ctrl and rt.isValidNode(ctrl):  
            #save target in user prop
            rt.setUserProp(ctrl, "ScatterTarget", self.pending_target.name if self.pending_target else "")  
            #save elements names in user prop
            elements_names = [o.name for o in self.manager.get_all() if rt.isValidNode(o)] 
            rt.setUserProp(ctrl, "ScatterElements", ",".join(elements_names))            

            #save other parameters in user props
            rt.setUserProp(ctrl, "ScatterCount", str(count))                              
            rt.setUserProp(ctrl, "ScatterDistance", str(distance) if distance else "")    
            rt.setUserProp(ctrl, "ScatterPosJitter", f"{pos_jitterX},{pos_jitterY},{pos_jitterZ}") 
            rt.setUserProp(ctrl, "ScatterScaleX", f"{scale_rangeX[0]},{scale_rangeX[1]}") 
            rt.setUserProp(ctrl, "ScatterScaleY", f"{scale_rangeY[0]},{scale_rangeY[1]}") 
            rt.setUserProp(ctrl, "ScatterScaleZ", f"{scale_rangeZ[0]},{scale_rangeZ[1]}") 
            rt.setUserProp(ctrl, "ScatterRotX", f"{rot_x_range[0]},{rot_x_range[1]}")     
            rt.setUserProp(ctrl, "ScatterRotY", f"{rot_y_range[0]},{rot_y_range[1]}")     
            rt.setUserProp(ctrl, "ScatterRotZ", f"{rot_z_range[0]},{rot_z_range[1]}")     
            #save button states / checkbox states
            rt.setUserProp(ctrl, "ScatterRandom", "True" if self.ui.checkBox_random.isChecked() else "False")
            rt.setUserProp(ctrl, "ScatterProportionalScale", "True" if self.ui.checkBox_proportionalScale.isChecked() else "False")
            rt.setUserProp(ctrl, "ScatterDisplayAsBox", str(self.ui.button_box.isChecked()))
            rt.setUserProp(ctrl, "ScatterMode", mode)
                    # ------------------- DEBUG: Read back user props -------------------
            print("DEBUG: Saved userProps on controller:")
            for prop in ["ScatterElements", "ScatterCount", "ScatterDistance",
                        "ScatterPosJitter", "ScatterScaleX", "ScatterScaleY", "ScatterScaleZ",
                        "ScatterRotX", "ScatterRotY", "ScatterRotZ",
                        "ScatterProportionalScale", "ScatterRandom", "ScatterDisplayAsBox", "ScatterMode"]:
                val = rt.getUserProp(ctrl, prop)
                print(f"  {prop}: {val}")

            print(f"DEBUG: Completed update for group: {self.current_group.name}")

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