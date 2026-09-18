import tkinter as tk
from tkinter import filedialog, messagebox

import numpy as np
import PIL.Image as im


n1 = 1
n2 = 1

rotate_ccw = np.array([[0, -1], [1, 0]])
rotate_cw = np.array([[0, 1], [-1, 0]])
resize = np.array([[n1, 0], [0, n2]])
flip_x = np.array([[1,0],[0,-1]])
flip_y = np.array([[-1, 0], [0, 1]])
shear = np.array([[1, 1], [0, 1]])


def show_options_window():
    custom_message = "Choose the image transformation you want to apply:"
    options = [
        "CCW 90 degree rotation",
        "CW 90 degree rotation",
        "Resize",
        "Flip along X",
        "Flip along Y",
        "Shear",
        "Reset"
    ]

    root = tk.Tk()
    root.title("TOOLBOX - Choose a option")
    selected_option = tk.IntVar(value=0)
    tk.Label(root, text=custom_message).pack(anchor="w", padx=15, pady=(15, 5))

    for number, option in enumerate(options):
        tk.Radiobutton(
            root,
            text=f"{number}. {option}",
            variable=selected_option,
            value=number,
            anchor="w",
        ).pack(fill="x", padx=15)

    tk.Button(root, text="Select", command=root.destroy).pack(pady=12)
    root.mainloop()
    return selected_option.get()


path_window = tk.Tk()
path_window.title("TOOLBOX - Image Path")
image_path = tk.StringVar()

tk.Label(path_window, text="Please enter or choose the path of the image:").pack(padx=15, pady=(15, 5))
tk.Entry(path_window, textvariable=image_path, width=65).pack(padx=15)

buttons = tk.Frame(path_window)
buttons.pack(pady=12)
tk.Button(
    buttons,
    text="Browse",
    command=lambda: image_path.set(filedialog.askopenfilename(
        title="Choose an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif"), ("All files", "*.*")],
    )),
).pack(side=tk.LEFT, padx=5)
tk.Button(
    buttons,
    text="Open",
    command=lambda: path_window.destroy()
    if image_path.get().strip()
    else messagebox.showwarning("Missing path", "Please enter an image path."),
).pack(side=tk.LEFT, padx=5)
path_window.mainloop()
image_path = image_path.get().strip()

if not image_path:
    raise SystemExit("No image path was provided.")

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



    


#transforming each vectors
def transformation(A):
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
    im.fromarray(output_ary).show()




trans = show_options_window()
if trans == 0 :
    A= rotate_ccw
    transformation(A)
elif trans == 1:
    A = rotate_cw
    transformation(A)
elif trans==2:
    A = resize
    transformation(A)
elif trans ==3:
    A = flip_x
    transformation(A)
elif trans==4:
    A = flip_y
    transformation(A)
elif trans == 5:
    A = shear
    transformation(A)

elif trans == 6:
    im.fromarray(img_ary).show()

#showing the transformed image.

            