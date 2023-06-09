import os
import numpy as np
import pandas as pd
import shutil
import imghdr

baseDir = '/home/jmtanous/temp'
targetDir = '/home/jmtanous/temp/TestGrouped'

test_metadata=pd.read_csv(baseDir + '/Test.csv')
y_test = []

# Navegamos el directorio Test para crear correctamente nuestra lista de etiquetas
for root, dirs, files in os.walk(baseDir + "/TestBackup"):
    for name in files:
        # Solo usamos archivos de imágnes
        if imghdr.what(os.path.join(root, name)):
            x = test_metadata[test_metadata['Path'].str.contains(name)].ClassId.values[0]
            targetPath = targetDir + '/' + str(x)
            if not os.path.exists(targetPath):
                os.makedirs(targetPath)
            oldName = os.path.join(root, name)
            newName = targetPath + '/' + name
            shutil.move(oldName,newName)
