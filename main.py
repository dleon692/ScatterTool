import os, sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)
from PySide2 import QtWidgets,QtCore
from ui_scattertool_UI import Ui_ScatterToolUI
from scattertool import ScatterTool,ElementsManager,ScatterGroup
from pymxs import runtime as rt
from PySide2.QtCore import QStringListModel
from PySide2.QtWidgets import QButtonGroup
import random
import builtins

class ScatterToolApp(QtWidgets.QMainWindow):
    def __init__(self):
        #create controller before UI to avoid null references

        def new_controller():
    
            create_controller = """
            global lastDummy
            global lastDummyLayer

            rollout NameDummyRollout "Trane Scatter Tool"
            (
                edittext edt_name "Name:" width:160
                button btn_ok "Apply" width:160

                on btn_ok pressed do
                (
                    if lastDummy != undefined and isValidNode lastDummy then
                    (
                        local dummyName = edt_name.text
                        lastDummy.name = dummyName

                        -- create or get layer
                        local lyr = LayerManager.getLayerFromName dummyName
                        if lyr == undefined then
                            lyr = LayerManager.newLayerFromName dummyName
                        
                        lastDummyLayer = lyr

                        -- add dummy to layer
                        lyr.addNode lastDummy
                    )

                    destroyDialog NameDummyRollout
                )
            )

            tool CreateNamedDummyTool
            (
                on mousePoint clickNo do
                (
                    if mouse.buttonStates[1] then
                    (
                        local r = mapScreenToWorldRay mouse.pos
                        local rayOrigin = r.pos
                        local rayDir    = r.dir

                        if rayDir.z != 0 then
                        (
                            local t = -rayOrigin.z / rayDir.z
                            local hitPos = rayOrigin + rayDir * t

                            -- create dummy at hit position
                            lastDummy = point pos:hitPos size:10 box:true cross:false

                            -- ⛔ stop tool and show naming dialog
                            stopTool CreateNamedDummyTool

                            -- show window
                            createDialog NameDummyRollout modal:true
                        )
                    )
                )
            )

            startTool CreateNamedDummyTool
            """
            rt.execute(create_controller)
        new_controller()

       
        #create main window
        super(ScatterToolApp, self).__init__(parent=None)
        self.ui = Ui_ScatterToolUI()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)


        #create group for mode selection
        self.distribution_group = QButtonGroup(self)
        self.distribution_group.addButton(self.ui.button_spline)
        self.distribution_group.addButton(self.ui.button_surface)
        self.distribution_group.addButton(self.ui.button_painter)
        self.distribution_group.setExclusive(True)
        self.ui.button_spline.toggled.connect(self.mode_buttons)
        self.ui.button_surface.toggled.connect(self.mode_buttons)
        self.ui.button_painter.toggled.connect(self.mode_buttons)

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

        #distribution mode buttons
        self.ui.button_elementCount.toggled.connect(self.on_distribution_mode_changed)
        self.ui.button_distance.toggled.connect(self.on_distribution_mode_changed)

        #default distribution mode
        
        self.ui.button_elementCount.setChecked(True)
        self.on_distribution_mode_changed()

        #default count
        self.ui.spin_elementCount.setValue(5)

        #default distance
        self.ui.spin_distance.setValue(50)

        #default brush size
        self.ui.spin_brush.setValue(100)

        #default slider direction
        self.ui.horizontalSlider_direction.setValue(100)
        slider_value = self.ui.horizontalSlider_direction.value()
        self.ui.spinBox_direction.setValue(slider_value)
        self.ui.horizontalSlider_direction.valueChanged.connect(
            lambda value: self.ui.spinBox_direction.setValue(value)
        )

        #default viewport display 
        self.ui.spinBox_viewDisp.setValue(100)
        
        #elements manager to handle source objects.
        self.manager = ElementsManager()
        self.source_obj = None

        #show elements in the list widget.
        self.elements = []  # Your elements list
        self.model = QStringListModel()
        self.ui.ListElements.setModel(self.model)

        #set collition radius default
        self.ui.checkBox_collision.setChecked(True)
        self.ui.spinBox_colRadius.setValue(100)

        # turn off randomization controls by default
        self.ui.checkBox_random.setChecked(False)
        self.on_toggle_random(False)
        self.ui.checkBox_random.stateChanged.connect(lambda state: self.on_toggle_random(state == 2))
        self.ui.checkBox_proportionalScale.stateChanged.connect(self.on_toggle_random)
        self.ui.checkBox_proportionalScale.setChecked(True)

        # ---------------- Collision widgets ----------------
        self.ui.checkBox_collision.stateChanged.connect(self.on_collision_changed)
        self.ui.spinBox_colRadius.valueChanged.connect(self.on_collision_changed)

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
        except Exception as e:
            print(f"Error adding selection callback: {e}")
        
        # Expose the application instance to builtins for access in the callback
        builtins.scattertool_app_instance = self

        try:
            self.on_selection_changed()  # Load initial selection if any
        except Exception:
            pass 

        


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
        self.ui.horizontalSlider_direction.valueChanged.connect(self.on_direction_changed)
        self.ui.Button_update.clicked.connect(self.on_update)
        self.ui.spinBox_viewDisp.valueChanged.connect(self.on_viewport_disp_changed)
        self.ui.pushButton_apply.clicked.connect(self.on_apply_color_variation)
    
   # --------------------------- Mode buttons ---------------------------

    def mode_buttons(self):
         # reset buttons
        widgets_to_enable = [
            self.ui.spin_brush, self.ui.label_brushSize,
            self.ui.button_pickSpline, self.ui.button_pickSurface,
            self.ui.button_distance, self.ui.spin_distance,
            self.ui.button_elementCount, self.ui.spin_elementCount,
            self.ui.spin_PxMin, self.ui.spin_PxMax,
            self.ui.spin_PyMin, self.ui.spin_PyMax,
            self.ui.spin_PzMin, self.ui.spin_PzMax,
            self.ui.spin_RxMin, self.ui.spin_RxMax,
            self.ui.spin_RyMin, self.ui.spin_RyMax,
            self.ui.spin_RzMin, self.ui.spin_RzMax,
            self.ui.spin_SxMin, self.ui.spin_SxMax,
            self.ui.spin_SyMin, self.ui.spin_SyMax,
            self.ui.spin_SzMin, self.ui.spin_SzMax
        ]
        for w in widgets_to_enable:
            w.setEnabled(True)
     
        #surface mode
        if self.ui.button_surface.isChecked():

            self.ui.button_pickSurface.setEnabled(True)
            self.ui.button_pickSpline.setEnabled(False)

            #disable distribution mode not applicable to surface
            self.ui.button_distance.setEnabled(False)
            self.ui.spin_distance.setEnabled(False)

            self.ui.label_brushSize.setEnabled(False)
            self.ui.spin_brush.setEnabled(False)

           

            #position jitter disable
            for w in (self.ui.spin_PxMin, self.ui.spin_PxMax,
                  self.ui.spin_PyMin, self.ui.spin_PyMax,
                  self.ui.spin_PzMin, self.ui.spin_PzMax):
                w.setEnabled(False) 

         #spline mode
        elif self.ui.button_spline.isChecked():
            self.ui.button_pickSpline.setEnabled(True)
            self.ui.button_pickSurface.setEnabled(False)

            # enable distribution
            self.ui.button_distance.setEnabled(True)
            self.ui.spin_distance.setEnabled(self.ui.button_distance.isChecked())
            self.ui.button_elementCount.setEnabled(True)
            self.ui.spin_elementCount.setEnabled(self.ui.button_elementCount.isChecked())

            self.ui.label_brushSize.setEnabled(False)
            self.ui.spin_brush.setEnabled(False)

        
        #painter mode
        elif self.ui.button_painter.isChecked():
            self.ui.button_pickSpline.setEnabled(False)
            self.ui.button_pickSurface.setEnabled(False)

            #disable distribution modes not applicable to painter

            self.ui.button_distance.setEnabled(False)
            self.ui.spin_distance.setEnabled(False)
            self.ui.button_elementCount.setEnabled(False)
            self.ui.spin_elementCount.setEnabled(False)
            # enable brush
            self.ui.spin_brush.setEnabled(True)
            self.ui.label_brushSize.setEnabled(True)

            #execute painter click function
            if self.ui.button_painter.isChecked():
                self.activate_painter_mode()
                print("UI DEBUG ▶ Painter mode ACTIVATED")
            else:
                rt.execute("try(stopTool T) catch()")
                print("❌ Scatter Painter detenido")

             
   

        self.on_toggle_random(self.ui.checkBox_random.isChecked())
        
    # --------------------------- Scatter Painter ---------------------------
    
    def activate_painter_mode(self):
        """
        Activa el modo Painter en 3ds Max.
        Al hacer clic y arrastrar sobre la escena, se crean instancias
        de objetos usando la función scatter_place_at_point().
        """

        # Primero, intentamos detener cualquier tool T activa
        try:
            rt.execute("try(stopTool T) catch()")
            print("✅  Painter mode detenido previamente (si estaba activo)")
        except RuntimeError as e:
            print("⚠️ No se pudo detener la tool previamente:", e)

        # Exponemos la instancia actual de la app a MaxScript
        import builtins
        builtins.scattertool_app_instance = self
        print("PY ▶ scattertool_app_instance asignado")

        # Definimos el MaxScript de la tool
        ms_tool = r'''
    tool T
    (
        on mouseMove clickNo do
        (
            if mouse.buttonStates[1] then
            (
                local r = mapScreenToWorldRay mouse.pos
                local hits = intersectRayScene r

                if hits != undefined and hits.count > 0 then
                (
                    local hitData = hits[1][2]
                    local hitPos = if isProperty hitData #pos then hitData.pos else [0,0,0]

                    local py_cmd = "scattertool_app_instance.scatter_place_at_point((" +
                                (hitPos.x as string) + "," +
                                (hitPos.y as string) + "," +
                                (hitPos.z as string) + "))"
                    python.execute py_cmd
                )
                else
                (
                    print "No sobre superficie"
                )
            )
        )
    )
    startTool T
    '''
        # Ejecutamos la tool en 3ds Max
        try:
            rt.execute(ms_tool)
            print("✅ Painter mode activado desde Python")
        except RuntimeError as e:
            print("❌ Error al activar  Painter mode:", e)

    def scatter_place_at_point(self,world_pos):
        print("PY ▶ scatter_place_at_point recibido:", world_pos)

        # Intenta obtener un grupo activo
        active_group = None
        if hasattr(self, "scatter_tool") and self.scatter_tool:
            active_group = self.scatter_tool.get_group_by_selection()

        # Si no hay grupo activo, crear uno temporal
        if not active_group:
            active_group = getattr(self, "_painter_free_group", None)
            if not active_group:
                print("DEBUG ▶ No hay grupo activo, creando un grupo temporal 'PainterFree'")
                temp_group_name = "PainterFree"
                active_group = ScatterGroup(temp_group_name)
                active_group.manager = self.manager  # asigna los objetos fuente
                active_group.controller = rt.lastDummy  # usa el último dummy creado como controlado
                active_group.layer = rt.lastDummyLayer
                #-------active_group.controller.position = rt.point3(*world_pos)
                active_group.params = {
                        "check_collisions": True,
                        "collision_radius_factor":(self.ui.spinBox_colRadius.value() / 100.0),
                        "brush_size": self.ui.spin_brush.value(),
                        "pos_jitterX": (self.ui.spin_PxMin.value(), self.ui.spin_PxMax.value()),
                        "pos_jitterY": (self.ui.spin_PyMin.value(), self.ui.spin_PyMax.value()),
                        "pos_jitterZ": (self.ui.spin_PzMin.value(), self.ui.spin_PzMax.value()),
                        "scale_rangeX": (self.ui.spin_SxMin.value()/100, self.ui.spin_SxMax.value()/100),
                        "scale_rangeY": (self.ui.spin_SyMin.value()/100, self.ui.spin_SyMax.value()/100),
                        "scale_rangeZ": (self.ui.spin_SzMin.value()/100, self.ui.spin_SzMax.value()/100),
                        "rot_x_range": (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value()),
                        "rot_y_range": (self.ui.spin_RyMin.value(), self.ui.spin_RyMax.value()),
                        "rot_z_range": (self.ui.spin_RzMin.value(), self.ui.spin_RzMax.value()),
                        "orientation_value": self.ui.horizontalSlider_direction.value(),
                        "source_obj": self.manager.get_random(),
                        "proportional_scale": self.ui.checkBox_proportionalScale.isChecked(),
                        "random": self.ui.checkBox_random.isChecked()
                    }
                self._painter_free_group = active_group
        # Llamar al método scatter_painter del grupo (con colisión y random)
        active_group.scatter_painter(world_pos)



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
        # --- Target object ---
        target_name = rt.getUserProp(ctrl, "ScatterTarget")
        if target_name:
            node = rt.getNodeByName(target_name)
            if node and rt.isValidNode(node):
                self.pending_target = node
                group.target = node
            else:
                self.pending_target = None
                group.target = None
        else:
            self.pending_target = None
            group.target = None
        # --- Buttons / checkboxes ---
        mode = rt.getUserProp(ctrl, "ScatterMode")
        self.ui.button_spline.setChecked(mode == "spline")
        self.ui.button_surface.setChecked(mode == "surface")
        self.ui.button_painter.setChecked(mode == "painter")

        # --- Checkboxes ---
        val_random = rt.getUserProp(ctrl, "ScatterRandom")
        random_enabled = val_random if isinstance(val_random, bool) else str(val_random).lower() == "true"
        self.ui.checkBox_random.setChecked(random_enabled)

        val_prop = rt.getUserProp(ctrl, "ScatterProportionalScale")
        proportional = val_prop if isinstance(val_prop, bool) else str(val_prop).lower() == "true"
        self.ui.checkBox_proportionalScale.setChecked(proportional)
       
        val_box = rt.getUserProp(ctrl, "ScatterDisplayAsBox")
        self.ui.button_box.setChecked(val_box if isinstance(val_box, bool) else str(val_box).lower() == "true")

        val_coll_enabled = rt.getUserProp(ctrl, "ScatterCollisionEnabled")
        coll=val_coll_enabled if isinstance(val_coll_enabled, bool) else str(val_coll_enabled).lower() == "true"
        self.ui.checkBox_collision.setChecked(coll)


        # --- Numeric parameters ---
        # Count
        count = rt.getUserProp(ctrl, "ScatterCount")
        if count:
            self.ui.spin_elementCount.setValue(int(count))
        
        # Distance
        distance = rt.getUserProp(ctrl, "ScatterDistance")
        if distance:
            self.ui.spin_distance.setValue(float(distance))
        
        # Brush size
        size_brush = rt.getUserProp(ctrl, "ScatterBrushSize")
        if size_brush:
            self.ui.spin_brush.setValue(float(size_brush))

        #collision radius
        coll_radius = rt.getUserProp(ctrl, "ScatterCollisionRadius")
        if coll_radius:
            self.ui.spinBox_colRadius.setValue(int(coll_radius) if coll_radius else 100)

        #direction slider
        direction_value = rt.getUserProp(ctrl, "direction_value")
        if direction_value:
            self.ui.horizontalSlider_direction.setValue(int(direction_value))
            self.ui.spinBox_direction.setValue(int(direction_value))
            
        # Position jitter
        pos_jitterX = rt.getUserProp(ctrl, "ScatterPosJitterX")
        x_min, x_max = map(float, pos_jitterX.split(","))
        self.ui.spin_PxMin.setValue(int(x_min))
        self.ui.spin_PxMax.setValue(int(x_max))

        pos_jitterY = rt.getUserProp(ctrl, "ScatterPosJitterY")
        y_min, y_max = map(float, pos_jitterY.split(","))
        self.ui.spin_PyMin.setValue(int(y_min))
        self.ui.spin_PyMax.setValue(int(y_max))

        pos_jitterZ = rt.getUserProp(ctrl, "ScatterPosJitterZ")
        z_min, z_max = map(float, pos_jitterZ.split(","))
        self.ui.spin_PzMin.setValue(int(z_min))
        self.ui.spin_PzMax.setValue(int(z_max))
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
        
        #read viewport display percentage and apply
        vp_prop = rt.getUserProp(ctrl, "ScatterViewportDisplay")
        try:
            vp_value = int(vp_prop) if vp_prop else 100
        except ValueError:
            vp_value = 100
        group.params["viewport_percentage"] = vp_value

        #update spinbox without triggering signal
        try:
            self.ui.spinBox_viewDisp.blockSignals(True)
            self.ui.spinBox_viewDisp.setValue(vp_value)
        finally:
            self.ui.spinBox_viewDisp.blockSignals(False)

         # --- Update internal params dict ---
        group.params.update({
            "count": self.ui.spin_elementCount.value(),
            "distance": self.ui.spin_distance.value(),
            "brush_size": self.ui.spin_brush.value(),
            "pos_jitterX": (self.ui.spin_PxMin.value(), self.ui.spin_PxMax.value()),
            "pos_jitterY": (self.ui.spin_PyMin.value(), self.ui.spin_PyMax.value()),
            "pos_jitterZ": (self.ui.spin_PzMin.value(), self.ui.spin_PzMax.value()),
            "scale_rangeX": (self.ui.spin_SxMin.value()/100, self.ui.spin_SxMax.value()/100),
            "scale_rangeY": (self.ui.spin_SyMin.value()/100, self.ui.spin_SyMax.value()/100),
            "scale_rangeZ": (self.ui.spin_SzMin.value()/100, self.ui.spin_SzMax.value()/100),
            "rot_x_range": (self.ui.spin_RxMin.value(), self.ui.spin_RxMax.value()),
            "rot_y_range": (self.ui.spin_RyMin.value(), self.ui.spin_RyMax.value()),
            "rot_z_range": (self.ui.spin_RzMin.value(), self.ui.spin_RzMax.value()),
            "orientation_value": self.ui.horizontalSlider_direction.value(),
            "source_obj": self.manager.get_random(),
            "proportional_scale": proportional,
            "random": random_enabled
        })

        # --- Debug output ---
        print(f"DEBUG: Loaded group '{group.name}' with params: {group.params}")

        # --- Update spinboxes enabled/disabled according to random & proportional flags ---
        self.on_toggle_random(random_enabled) 
        if proportional and random_enabled:
            self.ui.spin_SyMin.setEnabled(False)
            self.ui.spin_SyMax.setEnabled(False)
            self.ui.spin_SzMin.setEnabled(False)
            self.ui.spin_SzMax.setEnabled(False)     
        self.update_ui_from_group(group)
        
        #update group name
        self.show_group_name()


    # --------------------------- Cleanup callback ---------------------------
    def closeEvent(self, event):
        if hasattr(self, 'sel_callback') and self.sel_callback:
            try:
                rt.callbacks.removeScripts(rt.Name('selectionSetChanged'))
            except Exception as e:
                print(f"Error removing callback: {e}")
  
        if hasattr(builtins, "scattertool_app_instance"):
            del builtins.scattertool_app_instance
        super().closeEvent(event)

    # --------------------------- Viewport display ---------------------------
    def on_viewport_disp_changed(self, value):
        if not self.current_group:
            return
        try:
            #save value in params
            self.current_group.params["viewport_percentage"] = value
            # apply to current group
            self.current_group.set_viewport_display(value)
            # save persistently in userProp
            ctrl = self.current_group.controller
            if ctrl and rt.isValidNode(ctrl):
                rt.setUserProp(ctrl, "ScatterViewportDisplay", str(value))
            print(f"DEBUG: Viewport display set to {value}% for group {self.current_group.name}")
        except Exception as e:
            print(f"ERROR: Failed to set viewport display -> {e}")
    

     # --------------------------- Box / Mesh View ---------------------------# 
    def on_box_view(self,enable=True):
        """Toggle display as box for the currently selected group's instances."""
        # Find the group associated with the selected controller
        group = self.scatter_tool.get_group_by_selection()
        if not group:
            print("No valid scatter group selected.")
            return
        enable = self.ui.button_box.isChecked()  # get state from UI

        # ---------------- SET DISPLAY MODE ----------------
        try:
            group.set_display_as_box(enable)
            # Save state directly in the group's params
            group.params["display_as_box"] = enable
            # Save it persistently in the controller's UserProp
            ctrl = group.controller
            if ctrl and rt.isValidNode(ctrl):
                rt.setUserProp(ctrl, "ScatterDisplayAsBox", str(enable))

            print(f"DEBUG:Display mode changed to {'BOX' if enable else 'MESH'}")

            # Block signals from BOTH buttons to prevent listener loops
            self.ui.button_box.blockSignals(True)
            self.ui.button_mesh.blockSignals(True)

            # Sync UI with actual state
            self.ui.button_box.setChecked(enable)
            self.ui.button_mesh.setChecked(not enable)

            # Unblock signals
            self.ui.button_box.blockSignals(False)
            self.ui.button_mesh.blockSignals(False)

        except Exception as e:
            self.ui.button_box.blockSignals(True)
            print(f"ERROR: set_display_as_box failed: {e}")
            # revert UI to MESH safely
            self.ui.button_box.blockSignals(True)
            self.ui.button_mesh.blockSignals(True)

            self.ui.button_box.setChecked(False)
            self.ui.button_mesh.setChecked(True)

            self.ui.button_box.blockSignals(False)
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

    #---------------------------distribution mode selection ---------------------------
    def on_distribution_mode_changed(self):
        if self.ui.button_distance.isChecked():
            self.ui.button_elementCount.blockSignals(True)
            self.ui.button_elementCount.setChecked(False)
            self.ui.button_elementCount.blockSignals(False)

            self.ui.spin_elementCount.setEnabled(False)
            self.ui.spin_distance.setEnabled(True)

        elif self.ui.button_elementCount.isChecked():

            self.ui.button_distance.blockSignals(True)
            self.ui.button_distance.setChecked(False)
            self.ui.button_distance.blockSignals(False)

            self.ui.spin_elementCount.setEnabled(True)
            self.ui.spin_distance.setEnabled(False)

        else:
            self.ui.button_elementCount.blockSignals(True)
            self.ui.button_elementCount.setChecked(True)
            self.ui.button_elementCount.blockSignals(False)
            
            self.ui.spin_distance.setEnabled(True)
            self.ui.spin_elementCount.setEnabled(False)

    #show current group name in the window title
    def show_group_name(self):
        sel = rt.selection
        print(f"DEBUG: Current selection = {[obj.name for obj in sel]}") 
        if not sel or len(sel) == 0:
            self.ui.scattergroupname.setText("")
            self.ui.colorbox.setStyleSheet(
                "QFrame {background-color: rgb(45, 45, 45); border: 1px solid; border-radius: 4px;}"
            )
            print("DEBUG: No selection")
            return

        obj = sel[0]
        print(f"DEBUG: Selected object = {obj.name}")  # debug objeto seleccionado
        group = self.scatter_tool.get_group_by_controller(obj)  # <-- usa la función del ScatterTool
        if group:
            print(f"DEBUG: Found group = {group.name}")  # debug grupo encontrado
        else:
            print("DEBUG: No group found for selected object")  # debug no se encontró grupo
        if group and rt.isValidNode(group.controller):
            self.ui.scattergroupname.setText(group.name)
            color = group.controller.wirecolor
            rgb = f"rgb({color.r},{color.g},{color.b})"
            self.ui.colorbox.setStyleSheet(
                f"QFrame {{background-color: {rgb}; border: 1px solid; border-radius: 4px;}}"
            )
        else:
            self.ui.scattergroupname.setText("")
            self.ui.colorbox.setStyleSheet(
                "QFrame {background-color: rgb(45, 45, 45); border: 1px solid; border-radius: 4px;}"
            )
    # --------------------------- Elements list management ---------------------------

    def on_add(self):
        picked_obj = rt.selection[0] if rt.selection.count > 0 else None
        if picked_obj:
            self.manager.add(picked_obj)
            self.refresh_listview()
            if self.current_group and rt.isValidNode(self.current_group.controller):
                elements_names = [o.name for o in self.manager.get_all() if rt.isValidNode(o)]
                rt.setUserProp(self.current_group.controller, "ScatterElements", ",".join(elements_names))
                print(f"DEBUG: Updated ScatterElements userProp: {picked_obj}")

    def on_delete(self):
        selected_indexes = self.ui.ListElements.selectedIndexes()
        if selected_indexes:
            selected_name = selected_indexes[0].data()
            obj_to_remove = next((obj for obj in self.manager.get_all() if obj.name == selected_name), None)
            if obj_to_remove:
                self.manager.remove(obj_to_remove)
                self.refresh_listview()
                if self.current_group and rt.isValidNode(self.current_group.controller):
                    elements_names = [o.name for o in self.manager.get_all() if rt.isValidNode(o)]
                    rt.setUserProp(self.current_group.controller, "ScatterElements", ",".join(elements_names))
                    print(f"DEBUG: Updated ScatterElements userProp: {obj_to_remove.name} was removed.")

    def on_replace(self):
        selected_indexes = self.ui.ListElements.selectedIndexes()
        picked_obj = rt.selection[0] if rt.selection.count > 0 else None
        if selected_indexes and picked_obj:
            selected_name = selected_indexes[0].data()
            old_obj = next((obj for obj in self.manager.get_all() if obj.name == selected_name), None)
            if old_obj:
                self.manager.replace(old_obj, picked_obj)
                self.refresh_listview()
                if self.current_group and rt.isValidNode(self.current_group.controller):
                    elements_names = [o.name for o in self.manager.get_all() if rt.isValidNode(o)]
                    rt.setUserProp(self.current_group.controller, "ScatterElements", ",".join(elements_names))
                    print(f"DEBUG: Updated ScatterElements userProp: {old_obj.name} was replaced by {picked_obj.name}  .")

    def on_add_list(self):
        selected_objs = list(rt.selection)
        if selected_objs:
            self.manager.add_many(selected_objs)
            self.refresh_listview()
            if self.current_group and rt.isValidNode(self.current_group.controller):
                elements_names = [o.name for o in self.manager.get_all() if rt.isValidNode(o)]
                rt.setUserProp(self.current_group.controller, "ScatterElements", ",".join(elements_names))
                added_names = [o.name for o in selected_objs]
                print(f"DEBUG: Updated ScatterElements userProp: the {added_names} were added.")
    # --------------------------- Randomization ---------------------------

    def on_shuffle_clicked(self):
        if not self.current_group:
            print("No current group to shuffle.")
            return
        self.current_group.shuffle_instances()
        
    def on_toggle_random(self,enabled):
        enabled= self.ui.checkBox_random.isChecked()

        #get mode
        surface_or_painter_mode= self.ui.button_surface.isChecked() or self.ui.button_painter.isChecked()
        #determine if position jitter controls should be enabled
        enable_position= enabled and not surface_or_painter_mode
    

        self.ui.button_shuffle.setEnabled(enabled)
        self.ui.spin_PxMin.setEnabled(enable_position)
        self.ui.spin_PxMax.setEnabled(enable_position)
        self.ui.spin_PyMin.setEnabled(enable_position)
        self.ui.spin_PyMax.setEnabled(enable_position)
        self.ui.spin_PzMin.setEnabled(enable_position)
        self.ui.spin_PzMax.setEnabled(enable_position)
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

    # ---------------------------collision detection ---------------------------
    def on_collision_changed(self):
        if not self.current_group or not rt.isValidNode(self.current_group.controller):
            return
        
        ctrl = self.current_group.controller
        collision_enabled = self.ui.checkBox_collision.isChecked()
        collision_radius = self.ui.spinBox_colRadius.value()
        
        # save in current group's params
        self.current_group.params["collision_enabled"] = collision_enabled
        self.current_group.params["collision_radius"] = collision_radius

        # save persistently in userProps
        rt.setUserProp(ctrl, "ScatterCollisionEnabled", str(collision_enabled))
        rt.setUserProp(ctrl, "ScatterCollisionRadius", str(collision_radius))
        
        print(f"DEBUG: Collision updated -> Enabled: {collision_enabled}, Radius: {collision_radius}")

    
    # --------------------------- Direction slider ---------------------------

    def on_direction_changed(self, value):
    #DEBUG-NORMAL
    
       # update slider and spinbox values
        self.ui.spinBox_direction.blockSignals(True)
        self.ui.spinBox_direction.setValue(value)
        self.ui.spinBox_direction.blockSignals(False)

        # save in current group's params
        if hasattr(self, "current_group") and self.current_group:
            self.current_group.params["direction_value"] = value

            self.current_group. normal_direction(value)

    # --------------------------- Launch scatter ---------------------------

    def on_update(self):
        print("DEBUG: Starting scatter update...")#DEBUG
              
        source_obj = self.manager.get_random()
        if not source_obj:
            print("No source object selected.")
            return
        
        # determine mode: spline, painter or surface
        if self.ui.button_spline.isChecked():
            mode = "spline"
        elif self.ui.button_painter.isChecked():
            mode = "painter"
        else:
            mode = "surface"

        # ------------- Gather parameters from UI -------------
        count = self.ui.spin_elementCount.value() if self.ui.button_elementCount.isChecked() else None
        distance = self.ui.spin_distance.value() if self.ui.button_distance.isChecked() else None
        brush_size = self.ui.spin_brush.value()
      
        #check if randomization is False
        if self.ui.checkBox_random.isChecked():
            pos_jitterX = (self.ui.spin_PxMin.value(), self.ui.spin_PxMax.value())
            pos_jitterY = (self.ui.spin_PyMin.value(), self.ui.spin_PyMax.value())
            pos_jitterZ = (self.ui.spin_PzMin.value(), self.ui.spin_PzMax.value())
        

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
            pos_jitterX = pos_jitterY = pos_jitterZ = (0.0, 0.0)
            scale_rangeX = scale_rangeY = scale_rangeZ = (1.0, 1.0)
            rot_x_range = rot_y_range = rot_z_range = (0.0, 0.0)
            proportional = False  # default to proportional if random is off 

        #store parameters
        params_dict={
            "count": count,
            "distance": distance,
            "brush_size": brush_size,
            "pos_jitterX": pos_jitterX,
            "pos_jitterY": pos_jitterY,
            "pos_jitterZ": pos_jitterZ,
            "scale_rangeX": scale_rangeX,
            "scale_rangeY": scale_rangeY,
            "scale_rangeZ": scale_rangeZ,
            "rot_x_range": rot_x_range,
            "rot_y_range": rot_y_range,
            "rot_z_range": rot_z_range,
            "source_obj": source_obj,
            "proportional_scale": proportional,
            "collision_enabled": self.ui.checkBox_collision.isChecked(),
            "collision_radius": self.ui.spinBox_colRadius.value(),
            "orientation_value": self.ui.horizontalSlider_direction.value(),
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

            target_name = rt.getUserProp(self.current_group.controller, "ScatterTarget")
            self.pending_target = rt.getNodeByName(target_name) if target_name else None
            if self.pending_target and rt.isValidNode(self.pending_target):
                self.pending_mode = "spline" if rt.superClassOf(self.pending_target) == rt.Shape else "surface"
            elif self.ui.button_painter.isChecked():
                self.pending_mode = "painter"
                self.pending_target = None
            else:
                self.pending_mode = None
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

                 #update group name
                self.show_group_name()
                print(f"DEBUG: Created new group: {self.current_group.name}")#DEBUG
                    
                if self.current_group.manager is None:
                    self.current_group.manager = self.manager  

        # Update current group's params
        self.current_group.params.update(params_dict)
        print(f"DEBUG: Updated group params: {self.current_group.params}")#DEBUG
 

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
            rt.setUserProp(ctrl, "ScatterPosJitterX", f"{pos_jitterX[0]},{pos_jitterX[1]}")
            rt.setUserProp(ctrl, "ScatterPosJitterY", f"{pos_jitterY[0]},{pos_jitterY[1]}")
            rt.setUserProp(ctrl, "ScatterPosJitterZ", f"{pos_jitterZ[0]},{pos_jitterZ[1]}") 
            rt.setUserProp(ctrl, "ScatterScaleX", f"{scale_rangeX[0]},{scale_rangeX[1]}") 
            rt.setUserProp(ctrl, "ScatterScaleY", f"{scale_rangeY[0]},{scale_rangeY[1]}") 
            rt.setUserProp(ctrl, "ScatterScaleZ", f"{scale_rangeZ[0]},{scale_rangeZ[1]}") 
            rt.setUserProp(ctrl, "ScatterRotX", f"{rot_x_range[0]},{rot_x_range[1]}")     
            rt.setUserProp(ctrl, "ScatterRotY", f"{rot_y_range[0]},{rot_y_range[1]}")     
            rt.setUserProp(ctrl, "ScatterRotZ", f"{rot_z_range[0]},{rot_z_range[1]}")   
            rt.setUserProp(ctrl, "ScatterBrushSize", str(brush_size))
            rt.setUserProp(ctrl, "ScatterCollisionRadius", str(self.ui.spinBox_colRadius.value()))
            rt.setUserProp(ctrl, "direction_value", str(self.ui.horizontalSlider_direction.value()))  
            #save button states / checkbox states
            rt.setUserProp(ctrl, "ScatterRandom", "True" if self.ui.checkBox_random.isChecked() else "False")
            rt.setUserProp(ctrl, "ScatterCollisionEnabled", str(self.ui.checkBox_collision.isChecked()))
            rt.setUserProp(ctrl, "ScatterProportionalScale", "True" if self.ui.checkBox_proportionalScale.isChecked() else "False")
            rt.setUserProp(ctrl, "ScatterDisplayAsBox", str(self.ui.button_box.isChecked()))
            rt.setUserProp(ctrl, "ScatterMode", mode)

        # Set display mode
        if mode == "spline":
            self.current_group.scatter_spline(self.current_group.params["source_obj"])
        else:
            self.current_group.scatter_surface(self.current_group.params["source_obj"])
        
        #Freeze elements 
        if self.current_group:
            self.current_group.set_frozen_elements(freeze=True)

    def update_ui_from_group(self, group):
            if not group or not rt.isValidNode(group.controller):
                return
            
            ctrl = group.controller

            target_name = rt.getUserProp(ctrl, "ScatterTarget")
            self.pending_target = rt.getNodeByName(target_name) if target_name else None

            if not self.pending_target or not rt.isValidNode(self.pending_target):
                print(f"DEBUG: Target node '{target_name}' not found in scene.")
                self.ui.button_pickSpline.setText("Pick Spline")
                self.ui.button_pickSurface.setText("Pick Surface")
            else:
                if rt.superClassOf(self.pending_target) == rt.Shape:
                    self.ui.button_pickSpline.setText(f"Spline: {self.pending_target.name}")
                    self.ui.button_spline.setChecked(True)
                    self.ui.button_surface.setChecked(False)
                elif rt.isKindOf(self.pending_target, rt.GeometryClass):
                    self.ui.button_pickSurface.setText(f"Surface: {self.pending_target.name}")
                    self.ui.button_surface.setChecked(True)
                    self.ui.button_spline.setChecked(False)

            p = group.params
            # Spinners
            self.ui.spin_elementCount.setValue(p.get("count", 0))
            self.ui.spin_PxMin.setValue(p["pos_jitter"].x if "pos_jitter" in p else 0)
            self.ui.spin_PyMin.setValue(p["pos_jitter"].y if "pos_jitter" in p else 0)
            self.ui.spin_PzMin.setValue(p["pos_jitter"].z if "pos_jitter" in p else 0)
            self.ui.spin_SxMin.setValue(int(p["scale_rangeX"][0]*100))
            self.ui.spin_SxMax.setValue(int(p["scale_rangeX"][1]*100))
            self.ui.spin_SyMin.setValue(int(p["scale_rangeY"][0]*100))
            self.ui.spin_SyMax.setValue(int(p["scale_rangeY"][1]*100))
            self.ui.spin_SzMin.setValue(int(p["scale_rangeZ"][0]*100))
            self.ui.spin_SzMax.setValue(int(p["scale_rangeZ"][1]*100))
            self.ui.spin_RxMin.setValue(p["rot_x_range"][0])
            self.ui.spin_RxMax.setValue(p["rot_x_range"][1])
            self.ui.spin_RyMin.setValue(p["rot_y_range"][0])
            self.ui.spin_RyMax.setValue(p["rot_y_range"][1])
            self.ui.spin_RzMin.setValue(p["rot_z_range"][0])
            self.ui.spin_RzMax.setValue(p["rot_z_range"][1])
            self.ui.spin_distance.setValue(p.get("distance", 0))
            self.ui.spin_brush.setValue(p.get("brush_size", 0))
            self.ui.horizontalSlider_direction.setValue(p.get("orientation_value", 0))
            self.ui.spinBox_direction.setValue(p.get("orientation_value", 0))
            self.ui.spinBox_colRadius.setValue(p.get("collision_radius", 100))

            # Checkboxes
            self.ui.checkBox_collision.setChecked(p.get("collision_enabled", False))
            self.ui.checkBox_random.setChecked(p.get("random", True))
            self.ui.checkBox_proportionalScale.setChecked(p.get("proportional_scale", True))

            # Buttons
            if group.target and rt.isValidNode(group.target):
                if rt.superClassOf(group.target) == rt.Shape:
                    self.ui.button_spline.setChecked(True)
                    self.ui.button_surface.setChecked(False)
                elif rt.isKindOf(group.target, rt.GeometryClass):
                    self.ui.button_surface.setChecked(True)
                    self.ui.button_spline.setChecked(False)
                else:
                    self.ui.button_spline.setChecked(False)
                    self.ui.button_surface.setChecked(False)
                    self.ui.button_painter.setChecked(True)
            else:
                self.ui.button_spline.setChecked(False)
                self.ui.button_surface.setChecked(False)
            self.ui.button_box.setChecked(rt.getUserProp(group.controller,"ScatterDisplayAsBox")=="True")

        # ------------------- Apply color variation -------------------   
    def on_apply_color_variation (self):
        if not self.current_group or not rt.isValidNode(self.current_group.controller):
            print("No current scatter group selected.")
            return

        submat_id= self.ui.spinBox_elemtID.value()
        hue_var=self.ui.spinBox_hueVar.value()
        sat_var=self.ui.spinBox_satVar.value()
        val_var=self.ui.spinBox_briVar.value()

        self.scatter_tool.apply_color_variation(hue_var, sat_var, val_var, submat_id,self.current_group,num_variations=5)
    




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