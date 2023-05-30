import c3d
import xml.etree.ElementTree as ET
import cv2
import numpy as np

xml_data = open('../Sequences/p1s1/Calibration/c1.xml', 'r').read()  # Read file
root = ET.XML(xml_data)  # Parse XML
print(enumerate(root))
print(root[1].get("focal"))
focal = float(root[1].get("focal"))
kappa = float(root[1].get("kappa1"))
cx = float(root[1].get("cx"))
cy = float(root[1].get("cy"))
sx = float(root[1].get("sx"))
tx = float(root[2].get("tx"))
ty = float(root[2].get("ty"))
tz = float(root[2].get("tz"))
rx = float(root[2].get("rx"))
ry = float(root[2].get("ry"))
rz = float(root[2].get("rz"))

camera_matrix = np.array([[focal, 0, cx], [0, kappa, cy], [0, 0, 1]])

result_points = []

reader = c3d.Reader(open('../Sequences/p1s1/MoCap/p1s1.c3d', 'rb'))
for i, points, analog in reader.read_frames():
    #print('frame {}: point {}, analog {}'.format(i, points.shape, analog.shape))
    #print(points[0])
    points_xyz = []
    for point in points:
        [x,y,z, r, c] = point
        points_xyz.append((float(x),float(y),float(z)))

    imagePoints = cv2.projectPoints(points_xyz[0], np.array([rx,ry,rz]), np.array([tx,ty,tz]), camera_matrix, np.array([0.0,0.0,0.0,0.0]))
    print(imagePoints[0])
    result_points.append(imagePoints)


#print(result_points)


data = []
cols = []
for i, child in enumerate(root):
    data.append([subchild.text for subchild in child])
    cols.append(child.tag)
