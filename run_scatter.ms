source_obj = selection[1]
spline_obj = selection[2]

pythonScriptPath = @"C:\Users\Daniel Leon\Desktop\Trane\scattertool.py"

python.Execute ("exec(open(r'" + pythonScriptPath + "').read())")
python.Execute ("scatter_along_spline_distance(rt.getNodeByName('" + source_obj.name + "'), rt.getNodeByName('" + spline_obj.name + "'))")
