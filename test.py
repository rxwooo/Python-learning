import os
for i in range(5000,155000, 5000):
    path = "rm work/model/yolov3_darknet/"
    cmd = path + str(i) + ".pdopt"
    os.system(cmd)
    cmd = path + str(i) + ".pdmodel"
    os.system(cmd)
    cmd = path + str(i) + ".pdparams"
    os.system(cmd)