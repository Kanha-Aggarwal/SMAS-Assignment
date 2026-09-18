import numpy as np
import PIL.Image as im

#defining matrix
A1 = np.array([[2, 0],
              [0, 0.5]])

A2 = np.array([[0, -1],
              [1, 0]])

A3 = np.array([[1, 1],
              [0, 1]])

A4 = np.array([[-1, 0],
              [0, 1]])

A5 = np.array([[1, 0],
              [0, 0.02]])
e1 = np.array([[1],
               [0]])
e2 = np.array([[0],
               [1]])


#importing image by making an object variable and converting it into an array.
image_path = "C:\\Users\\HP\\OneDrive\\UNIFIED ENGINEERING SEM 1\\PYTHON\\HareKrishna.jpg"
img = im.open(image_path)
img_ary = np.array(img)

#setting shape of canvas
s =  np.shape(img_ary)
h, w = s[:2]
max_dim = int(np.sqrt(h**2 + w**2))
output_shape = (max_dim, max_dim) + img_ary.shape[2:]
output_ary = np.zeros(output_shape, dtype=img_ary.dtype)


#DEFINING COORDIANTE SYSTEM
cx_in , cy_in = w//2, h//2
cx_out, cy_out = max_dim //2, max_dim//2




#asking user about which transformation he/she wants
trans = int(input("Enter what transformation you want: \n0. Original image\n1. Scaling\n2. 90 Rotation\n3. Horizonatl Shear\n4. Reflection on y-axis\n5. Projection on x-axis\n Enter the no. only."))
if trans == 0:
    im.fromarray(img_ary).show()
    raise SystemExit
elif trans == 1:
    A = A1
    print("No information is not lost.")
    print("The image is stretched twice along X-axis but, reduced by half along Y-axis.")
elif trans==2:
    A= A2
    print("No information is not lost.")
    print("The image is rotated.")
elif trans ==3:
    A=A3
    print("No information is not lost.")
    print("")
elif trans==4:
    A=A4
    print("No information is not lost.")
    print("The image's projection hasbeen taken on X-axis.")
elif trans == 5:
    A=A5
    print("The information is lost!!!")
else:
    raise ValueError("Enter the correct transformation number!!!!")

print("T(e1) =", A*e1)
print("T(e2) =", A*e2)



#transforming each vectors
for y in range (h):
    for x in range (w):
        x_coord = x - cx_in
        y_coord = cy_in - y #invert because image indexing goes down, math goes up

        pos_vect = np.array([[x_coord],
                            [y_coord]])
        transformed_vector = np.dot(A,pos_vect)
        new_x = int(round(transformed_vector[0,0]))
        new_y = int(round(transformed_vector[1,0]))

        out_x = new_x +cx_out
        out_y = cy_out - new_y

        if 0<= out_x < max_dim and 0<= out_y <max_dim :
            output_ary[out_y, out_x] = img_ary[y, x]



#showing the transformed image.
im.fromarray(output_ary).show()

            