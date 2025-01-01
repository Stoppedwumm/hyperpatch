import importlib
import tempfile
import os
import importlib.util
import sys
def exec(extension, installPath):
    print(extension, installPath)
    module_name = extension.split(".")[0].split("/")[-1]
    file_path = extension
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    
    # Create a temporary directory
    temp_dir = tempfile.mkdtemp()
    ext = mod
    ext.main(installPath, temp_dir)
    os.rmdir(temp_dir)
    
    