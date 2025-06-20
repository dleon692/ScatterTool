source_obj = selection[1]
source_surface = selection[2]

pythonScriptPath = @"C:\Users\Daniel Leon\Desktop\Trane\scattertool.py"

python.Execute ("exec(open(r'" + pythonScriptPath + "').read())")
python.Execute ("scatter_along_surface(rt.getNodeByName('" + source_obj.name + "'), rt.getNodeByName('" + source_surface.name + "'))")
