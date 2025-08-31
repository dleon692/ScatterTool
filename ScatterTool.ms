try
(
    local thisFile = getSourceFileName()
    local toolDir  = getFilenamePath thisFile

    local py = ""
    py += "import sys, os, importlib\n"
    py += "TOOL_DIR = r'" + (substituteString toolDir "\\" "\\\\") + "'\n"
    py += "sys.path.append(TOOL_DIR) if TOOL_DIR not in sys.path else None\n"
    py += "import ui_scattertool_UI, scattertool, main\n"
    py += "importlib.reload(ui_scattertool_UI)\n"
    py += "importlib.reload(scattertool)\n"
    py += "importlib.reload(main)\n"
    py += "main.launch()\n"

    python.execute py
)
catch
(
    messageBox ("Failed to launch (DEV) ScatterTool.\n" + getCurrentException())
)