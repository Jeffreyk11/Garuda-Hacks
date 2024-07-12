from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Frame, Label, StringVar
import customtkinter
import cv2
import threading
from PIL import Image, ImageTk
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH_FRAME0 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame0")
ASSETS_PATH_FRAME1 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame1")
ASSETS_PATH_FRAME2 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame2")
ASSETS_PATH_FRAME3 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame3")
ASSETS_PATH_FRAME4 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame4")
ASSETS_PATH_FRAME5 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame5")
ASSETS_PATH_FRAME6 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame6")
ASSETS_PATH_FRAME7 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame7")
ASSETS_PATH_FRAME8 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame8")
ASSETS_PATH_FRAME9 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame9")
ASSETS_PATH_FRAME10 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame10")
ASSETS_PATH_FRAME11 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame11")
ASSETS_PATH_FRAME12 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame12")
ASSETS_PATH_FRAME13 = OUTPUT_PATH / Path(r"D:\Tugas\Binus\Garuda Hacks\build\assets\frame13")

def relative_to_assets_frame0(path:  str) -> Path:
    return ASSETS_PATH_FRAME0 / Path(path)
def relative_to_assets_frame1(path: str) -> Path:
    return ASSETS_PATH_FRAME1 / Path(path)

def relative_to_assets_frame2(path: str) -> Path:
    return ASSETS_PATH_FRAME2 / Path(path)

def relative_to_assets_frame3(path: str) -> Path:
    return ASSETS_PATH_FRAME3 / Path(path)

def relative_to_assets_frame4(path: str) -> Path:
    return ASSETS_PATH_FRAME4 / Path(path)

def relative_to_assets_frame5(path: str) -> Path:
    return ASSETS_PATH_FRAME5 / Path(path)

def relative_to_assets_frame6(path: str) -> Path:
    return ASSETS_PATH_FRAME6 / Path(path)

def relative_to_assets_frame7(path: str) -> Path:
    return ASSETS_PATH_FRAME7 / Path(path)

def relative_to_assets_frame8(path: str) -> Path:
    return ASSETS_PATH_FRAME8 / Path(path)

def relative_to_assets_frame9(path: str) -> Path:
    return ASSETS_PATH_FRAME9 / Path(path)

def relative_to_assets_frame10(path: str) -> Path:
    return ASSETS_PATH_FRAME10 / Path(path)

def relative_to_assets_frame11(path: str) -> Path:
    return ASSETS_PATH_FRAME11 / Path(path)

def relative_to_assets_frame12(path: str) -> Path:
    return ASSETS_PATH_FRAME12 / Path(path)

def relative_to_assets_frame13(path: str) -> Path:
    return ASSETS_PATH_FRAME13 / Path(path)
def play_video(video_path, canvas, x1, y1, x2, y2):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_time = 1 / fps
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = image.resize((x2 - x1, y2 - y1), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)
        canvas.create_image(x1, y1,anchor='nw', image=image_tk)
        canvas.image = image_tk
        canvas.update()
        time.sleep(frame_time)
    cap.release()

def start_video_thread(video_path, canvas, x1, y1, x2, y2):
    video_thread = threading.Thread(target=play_video, args=(video_path, canvas, x1, y1, x2, y2))
    video_thread.daemon = True
    video_thread.start()

window = Tk()
window.geometry("390x844")
window.configure(bg="#F5F5F5")

def show_frame(frame):
    frame.tkraise()

page_1 = Frame(window, bg="#F5F5F5")
page_2 = Frame(window, bg="#F5F5F5")
page_3 = Frame(window, bg="#F5F5F5")
page_4 = Frame(window, bg="#F5F5F5")
page_5 = Frame(window, bg="#F5F5F5")
page_6 = Frame(window, bg="#F5F5F5")
page_7 = Frame(window, bg="#F5F5F5")
page_8 = Frame(window, bg="#F5F5F5")
page_9 = Frame(window, bg="#F5F5F5")
page_10 = Frame(window, bg="#F5F5F5")
page_11 = Frame(window, bg="#F5F5F5")
page_12 = Frame(window, bg="#F5F5F5")
page_13 = Frame(window, bg="#F5F5F5")

video_AR = Label(window)
video_AR.pack()

for frame in (page_1, page_2, page_3, page_4, page_5, page_6, page_7, page_8, page_9, page_10, page_11, page_12, page_13):
    frame.place(x=0, y=0, width=390, height=844)

def on_text_change(*args):
    if password_var.get() and text_var.get():
        button2_1.configure(state="normal")
    else:
        button2_1.configure(state="disabled")

def on_text_change2(*args):
    if text_var.get():
        button2_2.configure(state="disabled")
        on_text_change()
    else:
        button2_2.configure(state="disabled")

def on_focus_in_username(event):
    if entry2_2.get() == 'Username':
        entry2_2.delete(0, "end")
        entry2_2.configure(fg_color="black")

def on_focus_out_username(event):
    if not entry2_2.get():
        entry2_2.insert(0, 'Username')
        entry2_2.configure(fg_color="grey")

def on_focus_in_password(event):
    if entry2_1.get() == 'Password':
        entry2_1.delete(0, "end")
        entry2_1.configure(fg_color="black")

def on_focus_out_password(event):
    if not entry2_1.get():
        entry2_1.insert(0, 'Password')
        entry2_1.configure(fg_color="grey")

# Page 1
canvas_1 = Canvas(
    page_1,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_1.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets_frame0("image_1.png"))
image_1 = canvas_1.create_image(
    196.0,
    422.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets_frame0("image_2.png"))
image_2 = canvas_1.create_image(
    195.0,
    375.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets_frame0("image_3.png"))
image_3 = canvas_1.create_image(
    195.0,
    376.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets_frame0("image_4.png"))
image_4 = canvas_1.create_image(
    195.0,
    23.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets_frame0("image_5.png"))
image_5 = canvas_1.create_image(
    195.0,
    827.0,
    image=image_image_5
)

canvas_1.create_text(
    24.0,
    436.0,
    anchor="nw",
    text="Detect Your Mistakes\nwith",
    fill="#F5F5F5",
    font=("SFProText Heavy", 28 * -1)
)
canvas_1.create_text(82.0,469.0, anchor="nw",text="Fixness",fill="#B5FF3E",font=("SFProText Heavy", 28 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets_frame0("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=24.0,
    y=610.0,
    width=342.0,
    height=60.0
)


canvas_1.create_text(24.0,512.0,anchor="nw",text="The efficient way to improve your workout \nexperiences",fill="#808080",font=("Inter SemiBold", 16 * -1))

image_image_6 = PhotoImage(file=relative_to_assets_frame0("image_6.png"))
image_6 = canvas_1.create_image(196.0,160.0,image=image_image_6)

image_image_7 = PhotoImage(
    file=relative_to_assets_frame0("image_7.png"))
image_7 = canvas_1.create_image(
    177.0,
    182.0,
    image=image_image_7
)

button_image_1 = PhotoImage(file=relative_to_assets_frame0("button_1.png"))
button_1 = Button(page_1, image=button_image_1, borderwidth=0, highlightthickness=0,
                  bg= "#000000",
                  command=lambda: show_frame(page_2),
                  relief="flat")
button_1.place(x=24.0, y=610.0, width=342.0, height=60.0)

button_2 = customtkinter.CTkButton(master=page_1, text="Create New Account", width=215, height=44, compound="left",bg_color= "#000000",
                                  fg_color='black', text_color='white', hover_color='#AFAFAF', command=lambda: show_frame(page_2))
button_2.place(x=89, y=680.0)

button_image_2 = PhotoImage(
    file=relative_to_assets_frame0("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command = lambda: show_frame(page_2),
    relief="flat"
)
button_2.place(
    x=88.0,
    y=680.0,
    width=215.0,
    height=44.0
)




# Page 2
canvas_2 = Canvas(page_2, bg="#F5F5F5", height=844, width=390, bd=0, highlightthickness=0, relief="ridge")
canvas_2.place(x=0, y=0)

image2_image_1 = PhotoImage(file=relative_to_assets_frame1("image_1.png"))
canvas_2.create_image(195.0, 422.0, image=image2_image_1)

image2_image_2 = PhotoImage(file=relative_to_assets_frame1("image_2.png"))
canvas_2.create_image(195.0, 23.0, image=image2_image_2)

image2_image_3 = PhotoImage(file=relative_to_assets_frame1("image_3.png"))
canvas_2.create_image(195.0, 827.0, image=image2_image_3)

canvas_2.create_rectangle(24.0, 223.0, 366.0, 271.0, fill="#222222", outline="")
entry2_image_1 = PhotoImage(file=relative_to_assets_frame1("entry_1.png"))
canvas_2.create_image(78.0, 247.5, image=entry2_image_1)



canvas_2.create_text(125, 371.0, anchor="nw", text="Forgot Password", fill="#F5F5F5", font=("Inter SemiBold", 14))

button2_image_1 = PhotoImage(file=relative_to_assets_frame1("button_1.png"))
button2_1 = Button(
    page_2,
    image=button2_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_3),
    relief="flat",
    state="disabled"
)
button2_1.place(x=24.0, y=291.0, width=342.0, height=60.0)

button2_image_2 = PhotoImage(file=relative_to_assets_frame1("button_2.png"))
button2_2 = Button(
    page_2,
    image=button2_image_2,
    bg = "#000000",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("Sign up button clicked"),
    relief="flat"
)
button2_2.place(x=24.0, y=430.0, width=343.0, height=56.0)

image2_image_7 = PhotoImage(file=relative_to_assets_frame1("image_7.png"))
canvas_2.create_image(210.0, 90.0, image=image2_image_7)

#Username
text_var = StringVar()
text_var.trace_add('write', on_text_change2)

entry2_2 = customtkinter.CTkEntry(
    master=page_2,
    height=48,
    width=342,
    bg_color="#000000",
    textvariable=text_var
)

entry2_2.place(x=24, y=163)
entry2_2.insert(0, 'Username')
entry2_2.configure(fg_color="grey")
entry2_2.bind("<FocusIn>", on_focus_in_username)
entry2_2.bind("<FocusOut>", on_focus_out_username)

password_var = StringVar()
password_var.trace_add('write', on_text_change)

entry2_1 = customtkinter.CTkEntry(
    master=page_2,
    height=48,
    width=342,
    bg_color= "#000000",
    placeholder_text='Password',
    show="*",
    textvariable=password_var
)
entry2_1.place(x=24, y=223.0)

entry2_1.insert(0, 'Password')
entry2_1.configure(fg_color="grey")
entry2_1.bind("<FocusIn>", on_focus_in_password)
entry2_1.bind("<FocusOut>", on_focus_out_password)

canvas_2.create_rectangle(24.0, 163.0, 366.0, 211.0, fill="#222222", outline="")
entry2_image_2 = PhotoImage(file=relative_to_assets_frame1("entry_2.png"))
canvas_2.create_image(80.0, 187.5, image=entry2_image_2)



# Page 3
canvas3 = Canvas(page_3, bg="#F5F5F5", height=844, width=390, bd=0, highlightthickness=0, relief="ridge")
canvas3.place(x=0, y=0)


canvas3.place(x = 0, y = 0)
image3_image_1 = PhotoImage(
    file=relative_to_assets_frame2("image_1.png"))
image3_1 = canvas3.create_image(
    195.0,
    422.0,
    image=image3_image_1
)

image3_image_2 = PhotoImage(
    file=relative_to_assets_frame2("image_2.png"))
image3_2 = canvas3.create_image(
    195.0,
    23.0,
    image=image3_image_2
)

image3_image_3 = PhotoImage(
    file=relative_to_assets_frame2("image_3.png"))
image3_3 = canvas3.create_image(
    195.0,
    827.0,
    image=image3_image_3
)

canvas3.create_text(
    24.0,
    230.0,
    anchor="nw",
    text="Activity",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 18 * -1)
)

canvas3.create_text(
    24.0,
    128.0,
    anchor="nw",
    text="Gender",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 18 * -1)
)

canvas3.create_text(
    24.0,
    332.0,
    anchor="nw",
    text="Weight",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 18 * -1)
)

canvas3.create_text(
    141.0,
    379.0,
    anchor="nw",
    text="kg",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 14 * -1)
)

canvas3.create_text(
    141.0,
    487.0,
    anchor="nw",
    text="cm",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 14 * -1)
)

canvas3.create_text(
    24.0,
    438.0,
    anchor="nw",
    text="Height",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 18 * -1)
)

canvas3.create_text(
    24.0,
    554.0,
    anchor="nw",
    text="How long you’ve been",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 18 * -1)
)

canvas3.create_text(
    31.0,
    338.0,
    anchor="nw",
    text=" ",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 20 * -1)
)

canvas3.create_rectangle(
    24.0,
    264.0,
    366.0,
    312.0,
    fill="#191919",
    outline="")

canvas3.create_rectangle(
    24.0,
    588.0,
    366.0,
    636.0,
    fill="#191919",
    outline="")

canvas3.create_rectangle(
    24.0,
    162.0,
    182.0,
    210.0,
    fill="#191919",
    outline="")

entry3_image_1 = PhotoImage(
    file=relative_to_assets_frame2("entry_1.png"))
entry3_bg_1 = canvas3.create_image(
    75.5,
    390.0,
    image=entry3_image_1
)

entry3_1 = customtkinter.CTkEntry(
    master=page_3,
    bg_color= "#000000",
    height=46,
    width=103,
)
entry3_1.place(x=24, y=366)

entry3_image_2 = PhotoImage(
    file=relative_to_assets_frame2("entry_2.png"))
entry3_bg_2 = canvas3.create_image(
    74.0,
    496.0,
    image=entry3_image_2
)

entry3_2 = customtkinter.CTkEntry(
    master=page_3,
    bg_color= "#000000",
    height=46,
    width=100
)
entry3_2.place(x=24, y=472)

button3_image_1 = PhotoImage(
    file=relative_to_assets_frame2("button_1.png"))
button3_1 = Button(
    page_3,
    image=button3_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button3_1.place(x=24.0,y=660.0,width=342.0, height=60.0)

canvas3.create_text(
    147.0,
    735.0,
    anchor="nw",
    text="Skip For Now",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 14 * -1)
)

image3_image_4 = PhotoImage(
    file=relative_to_assets_frame2("image_4.png"))
image3_4 = canvas3.create_image(
    158.0,
    186.0,
    image=image3_image_4
)

image3_image_5 = PhotoImage(
    file=relative_to_assets_frame2("image_5.png"))
image3_5 = canvas3.create_image(
    342.0,
    288.0,
    image=image3_image_5
)

image3_image_6 = PhotoImage(
    file=relative_to_assets_frame2("image_6.png"))
image3_6 = canvas3.create_image(
    342.0,
    612.0,
    image=image3_image_6
)

canvas3.create_text(
    40.0,
    177.0,
    anchor="nw",
    text="Please Select",
    fill="#808080",
    font=("Inter SemiBold", 14 * -1)
)

canvas3.create_text(
    40.0,
    279.0,
    anchor="nw",
    text="Please Select",
    fill="#808080",
    font=("Inter SemiBold", 14 * -1)
)

canvas3.create_text(
    40.0,
    603.0,
    anchor="nw",
    text="Please Select",
    fill="#808080",
    font=("Inter SemiBold", 14 * -1)
)


#Page 4
canvas4 = Canvas(
    page_4,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas4.place(x = 0, y = 0)
canvas4.create_rectangle(
    0.0,
    0.0,
    390.0,
    844.0,
    fill="#111111",
    outline="")

canvas4.create_rectangle(
    24.0,
    571.0,
    366.0,
    691.0,
    fill="#222222",
    outline="")

canvas4.create_text(
    44.0,
    624.0,
    anchor="nw",
    text="Lunges",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 20 * -1)
)

canvas4.create_text(
    126.0,
    631.0,
    anchor="nw",
    text="Beginner",
    fill="#B5FF3E",
    font=("Inter SemiBold", 12 * -1)
)

canvas4.create_text(
    44.0,
    652.0,
    anchor="nw",
    text="Leg",
    fill="#808080",
    font=("Inter SemiBold", 16 * -1)
)

image4_image_1 = PhotoImage(
    file=relative_to_assets_frame3("image_1.png"))
image4_1 = canvas4.create_image(
    338.0,
    636.0,
    image=image4_image_1
)

canvas4.create_rectangle(
    24.0,
    707.0,
    366.0,
    967.0,
    fill="#000000",
    outline="")

canvas4.create_rectangle(
    24.0,
    767.0,
    366.0,
    887.0,
    fill="#222222",
    outline="")

canvas4.create_text(
    169.0,
    69.0,
    anchor="nw",
    text="Chest",
    fill="#000000",
    font=("Inter SemiBold", 18 * -1)
)

image4_image_2 = PhotoImage(
    file=relative_to_assets_frame3("image_2.png"))
image4_2 = canvas4.create_image(
    195.0,
    786.0,
    image=image4_image_2
)

canvas4.create_text(
    44.0,
    820.0,
    anchor="nw",
    text="Tricep Dips",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 20 * -1)
)

canvas4.create_text(
    44.0,
    785.0,
    anchor="nw",
    text="Intermidiet",
    fill="#808080",
    font=("Inter SemiBold", 16 * -1)
)

canvas4.create_rectangle(
    24.0,
    67.0,
    366.0,
    127.0,
    fill="#222222",
    outline="")

image4_image_3 = PhotoImage(
    file=relative_to_assets_frame3("image_3.png"))
image4_3 = canvas4.create_image(
    149.0,
    97.0,
    image=image4_image_3
)

image4_image_4 = PhotoImage(
    file=relative_to_assets_frame3("image_4.png"))
image4_4 = canvas4.create_image(
    157.0,
    167.0,
    image=image4_image_4
)

image4_image_5 = PhotoImage(
    file=relative_to_assets_frame3("image_5.png"))
image4_5 = canvas4.create_image(
    67.0,
    167.0,
    image=image4_image_5
)

image4_image_6 = PhotoImage(
    file=relative_to_assets_frame3("image_6.png"))
image4_6 = canvas4.create_image(
    332.0,
    166.0,
    image=image4_image_6
)

image4_image_7 = PhotoImage(
    file=relative_to_assets_frame3("image_7.png"))
image4_7 = canvas4.create_image(
    238.0,
    166.0,
    image=image4_image_7
)

image4_image_8 = PhotoImage(
    file=relative_to_assets_frame3("image_8.png"))
image4_8 = canvas4.create_image(
    196.0,
    797.0,
    image=image4_image_8
)

image4_image_9 = PhotoImage(
    file=relative_to_assets_frame3("image_9.png"))
image4_9 = canvas4.create_image(
    67.0,
    786.0,
    image=image4_image_9
)

image4_image_10 = PhotoImage(
    file=relative_to_assets_frame3("image_10.png"))
image4_10 = canvas4.create_image(
    152.0,
    786.0,
    image=image4_image_10
)

image4_image_11 = PhotoImage(
    file=relative_to_assets_frame3("image_11.png"))
image4_11 = canvas4.create_image(
    237.0,
    786.0,
    image=image4_image_11
)

image4_image_12 = PhotoImage(
    file=relative_to_assets_frame3("image_12.png"))
image4_12 = canvas4.create_image(
    322.0,
    786.0,
    image=image4_image_12
)

image4_image_13 = PhotoImage(
    file=relative_to_assets_frame3("image_13.png"))
image4_13 = canvas4.create_image(
    195.0,
    23.0,
    image=image4_image_13
)

image4_image_14 = PhotoImage(
    file=relative_to_assets_frame3("image_14.png"))
image4_14 = canvas4.create_image(
    195.0,
    827.0,
    image=image4_image_14
)

image4_image_15 = PhotoImage(
    file=relative_to_assets_frame3("image_15.png"))
image4_15 = canvas4.create_image(
    336.0,
    97.0,
    image=image4_image_15
)



button4_image_1 = PhotoImage(
    file=relative_to_assets_frame3("button_1.png"))
button4_1 = Button(
    page_4,
    image=button4_image_1,
    borderwidth=0,
    bg= "#000000",
    highlightthickness=0,
    command=lambda: show_frame(page_5),
    relief="flat"
)
button4_1.place(
    x=24.0,
    y=207.0,
    width=342.0,
    height=234.0
)

image4_image_16 = PhotoImage(
    file=relative_to_assets_frame3("image_16.png"))
image4_16 = canvas4.create_image(
    338.0,
    386.0,
    image=image4_image_16
)

image4_image_17 = PhotoImage(
    file=relative_to_assets_frame3("image_17.png"))
image4_17 = canvas4.create_image(
    196.0,
    532.0,
    image=image4_image_17
)

#Page 5
canvas5 = Canvas(
    page_5,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas5.place(x = 0, y = 0)
canvas5.create_rectangle(
    0.0,
    0.0,
    390.0,
    844.0,
    fill="#111111",
    outline="")

image5_image_1 = PhotoImage(
    file=relative_to_assets_frame4("image_1.png"))
image5_1 = canvas5.create_image(
    195.0,
    23.0,
    image=image5_image_1
)

image5_image_2 = PhotoImage(
    file=relative_to_assets_frame4("image_2.png"))
image5_2 = canvas5.create_image(
    195.0,
    827.0,
    image=image5_image_2
)

#MAKE THIS RECTANGLE TO SHOW CAMERA

x1, y1, x2, y2 = 24, 134, 366, 698
canvas5.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video_path = "tutorial_las.mp4"
start_video_thread(video_path, canvas5, x1, y1, x2, y2)


button5_image_1 = PhotoImage(
    file=relative_to_assets_frame4("button_1.png"))
button5_1 = Button(
    page_5,
    image=button5_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_6),
    relief="flat"
)
button5_1.place(
    x=24.0,
    y=718.0,
    width=342.0,
    height=60.0
)

canvas5.create_text(
    154.0,
    78.0,
    anchor="nw",
    text="Push Up",
    fill="#F5F5F5",
    font=("Inter ExtraBold", 20 * -1)
)


button5_image_2 = PhotoImage(
    file=relative_to_assets_frame4("image_3.png"))
button5_2 = Button(
    page_5,
    image=button5_image_2,
    borderwidth=0,
    bg= "#000000",
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button5_2.place(
    x=24.0,
    y=78.0,
    width=24.0,
    height=24.0
)

image5_image_3 = PhotoImage(
    file=relative_to_assets_frame4("image_3.png"))
image5_3 = canvas5.create_image(
    36.0,
    90.0,
    image=image5_image_3
)

show_frame(page_1)
##########################################
#Page 6

canvas6 = Canvas(
    page_6,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas6.place(x = 0, y = 0)
image6_image_1 = PhotoImage(
    file=relative_to_assets_frame6("image_1.png"))
image6_1 = canvas6.create_image(
    195.0,
    203.0,
    image=image6_image_1
)

image6_image_2 = PhotoImage(
    file=relative_to_assets_frame6("image_2.png"))
image6_2 = canvas6.create_image(
    195.0,
    23.0,
    image=image6_image_2
)

canvas6.create_rectangle(
    0.0,
    810.0,
    390.0000305175781,
    844.0000038146973,
    fill="#000000",
    outline="")

button6_image_1 = PhotoImage(
    file=relative_to_assets_frame6("button_1.png"))
button6_1 = Button(
    page_6,
    image=button6_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button6_1.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)

button6_image_2 = PhotoImage(
    file=relative_to_assets_frame6("button_2.png"))
button6_2 = Button(
    page_6,
    image=button6_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_7),
    relief="flat"
)
button6_2.place(
    x=100.0,
    y=718.0,
    width=266.0,
    height=60.0
)

image6_image_3 = PhotoImage(
    file=relative_to_assets_frame6("image_3.png"))
image6_3 = canvas6.create_image(
    54.0,
    748.0,
    image=image6_image_3
)

x1, y1, x2, y2 = 24, 134, 366, 698
canvas6.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video2_path = "ar.mp4"
start_video_thread(video2_path, canvas6, x1, y1, x2, y2)

##################
#Page 7
canvas7 = Canvas(
    page_7,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)



canvas7.place(x = 0, y = 0)
image7_image_1 = PhotoImage(
    file=relative_to_assets_frame7("image_1.png"))
image7_1 = canvas7.create_image(
    195.0,
        23.0,
    image=image7_image_1
)

image7_image_3 = PhotoImage(
    file=relative_to_assets_frame7("image_3.png"))
image7_3 = canvas7.create_image(
    194.0,
    195.0,
    image=image7_image_3
)



image7_image_4 = PhotoImage(
    file=relative_to_assets_frame7("image_4.png"))
image7_4 = canvas7.create_image(
    195.0,
    827.0,
    image=image7_image_4
)

button7_image_1 = PhotoImage(
    file=relative_to_assets_frame7("button_1.png"))
button7_1 = Button(
    page_7,
    image=button7_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button7_1.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)

button7_image_2 = PhotoImage(
    file=relative_to_assets_frame7("image_2.png"))
button7_2 = Button(
    page_7,
    bg = "black",
    image=button7_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_8),
    relief="flat"
)
button7_2.place(
    x=150.0,
    y=600.0,
)

x1, y1, x2, y2 = 0, 0, 390, 844
canvas7.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video3_path = "good_form.mp4"
start_video_thread(video3_path, canvas7, x1, y1, x2, y2)

#Page 8
canvas8 = Canvas(
    page_8,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas8.place(x = 0, y = 0)
image8_image_1 = PhotoImage(
    file=relative_to_assets_frame8("image_1.png"))
image8_1 = canvas8.create_image(
    196.0,
    23.0,
    image=image8_image_1
)

image8_image_3 = PhotoImage(
    file=relative_to_assets_frame8("image_9.png"))
image8_3 = canvas8.create_image(
    194,
    390,
    image=image8_image_3
)

button8_image_1 = PhotoImage(
    file=relative_to_assets_frame8("button_1.png"))
button8_1 = Button(
    page_8,
    image=button8_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button8_1.place(
    x=0.0,
    y=810.0,
    width=390.0000305175781,
    height=34.000003814697266
)

image8_image_2 = PhotoImage(
    file=relative_to_assets_frame8("image_2.png"))
image8_2 = canvas8.create_image(
    195.0,
    187.0,
    image=image8_image_2
)

button8_image_2 = PhotoImage(
    file=relative_to_assets_frame8("button_2.png"))
button8_2 = Button(
    page_8,
    image=button8_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_9),
    relief="flat"
)
button8_2.place(
    x=24.0,
    y=718.0,
    width=342.0,
    height=60.0
)

button8_image_3 = PhotoImage(
    file=relative_to_assets_frame8("button_3.png"))
button8_3 = Button(
    page_8,
    image=button8_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button8_3.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)




#Page 9
canvas9 = Canvas(
    page_9,
    bg = "#F5F5F5",
    height = 844,
    width = 395,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas9.place(x = 0, y = 0)
canvas9.create_rectangle(
    0.0,
    6.0,
    395.0,
    856.0,
    fill="#111111",
    outline="")

image9_image_1 = PhotoImage(
    file=relative_to_assets_frame9("image_1.png"))
image9_1 = canvas9.create_image(
    200.0,
    23.0,
    image=image9_image_1
)

image9_image_2 = PhotoImage(
    file=relative_to_assets_frame9("image_2.png"))
image9_2 = canvas9.create_image(
    200.0,
    827.0,
    image=image9_image_2
)

canvas9.create_rectangle(
    29.0,
    134.0,
    371.0,
    698.0,
    fill="#2A2A2A",
    outline="")

button9_image_1 = PhotoImage(
    file=relative_to_assets_frame9("button_1.png"))
button9_1 = Button(
    page_9,
    image=button9_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_10),
    relief="flat"
)
button9_1.place(
    x=24.0,
    y=718.0,
    width=347.0,
    height=60.0
)

image9_image_3 = PhotoImage(
    file=relative_to_assets_frame9("image_3.png"))
image9_3 = canvas9.create_image(
    200.0,
    90.0,
    image=image9_image_3
)

button9_image_2 = PhotoImage(
    file=relative_to_assets_frame9("button_2.png"))
button9_2 = Button(
    page_9,
    image=button9_image_2,
    borderwidth=0,
    highlightthickness=0,
    bg= 'black',
    command=lambda: show_frame(page_4),
    relief="flat"
)
button9_2.place(
    x=29.0,
    y=78.0,
    width=24.0,
    height=24.0
)

image9_image_4 = PhotoImage(
    file=relative_to_assets_frame9("image_4.png"))
image9_4 = canvas9.create_image(
    196.0,
    206.0,
    image=image9_image_4
)

x1, y1, x2, y2 = 24, 134, 366, 698
canvas9.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video5_path = "tutorial_las.mp4"
start_video_thread(video5_path, canvas9, x1, y1, x2, y2)

#Page 10
canvas10 = Canvas(
    page_10,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas10.place(x = 0, y = 0)
image10_image_1 = PhotoImage(
    file=relative_to_assets_frame10("image_1.png"))
image10_1 = canvas10.create_image(
    195.0,
    23.0,
    image=image10_image_1
)

image10_image_2 = PhotoImage(
    file=relative_to_assets_frame10("image_2.png"))
image10_2 = canvas10.create_image(
    195.0,
    203.0,
    image=image10_image_2
)

image10_image_3 = PhotoImage(
    file=relative_to_assets_frame10("image_3.png"))
image10_3 = canvas10.create_image(
    195.0,
    827.0,
    image=image10_image_3
)

button10_image_1 = PhotoImage(
    file=relative_to_assets_frame10("button_1.png"))
button10_1 = Button(
    page_10,
    image=button10_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_11),
    relief="flat"
)
button10_1.place(
    x=100.0,
    y=718.0,
    width=266.0,
    height=60.0
)

button10_image_2 = PhotoImage(
    file=relative_to_assets_frame10("button_2.png"))
button10_2 = Button(
    page_10,
    image=button10_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button10_2.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)

image10_image_4 = PhotoImage(
    file=relative_to_assets_frame10("image_4.png"))
image10_4 = canvas10.create_image(
    54.0,
    748.0,
    image=image10_image_4
)

x1, y1, x2, y2 = 24, 134, 366, 698
canvas10.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video6_path = "start_scanning2.mp4"
start_video_thread(video6_path, canvas10, x1, y1, x2, y2)

#Page 11
canvas11 = Canvas(
    page_11,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas11.place(x = 0, y = 0)
image11_image_1 = PhotoImage(
    file=relative_to_assets_frame11("image_1.png"))
image11_1 = canvas7.create_image(
    195.0,
    23.0,
    image=image11_image_1
)

image11_image_3 = PhotoImage(
    file=relative_to_assets_frame11("image_3.png"))
image11_3 = canvas11.create_image(
    195.0,
    195.0,
    image=image11_image_3
)

image11_image_4 = PhotoImage(
    file=relative_to_assets_frame11("image_4.png"))
image11_4 = canvas7.create_image(
    195.0,
    827.0,
    image=image11_image_4
)

button11_image_1 = PhotoImage(
    file=relative_to_assets_frame11("button_1.png"))
button11_1 = Button(
    page_11,
    image=button11_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button11_1.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)

button11_image_2 = PhotoImage(
    file=relative_to_assets_frame11("image_2.png"))
button11_2 = Button(
    page_11,
    image=button11_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_12),
    relief="flat"
)
button11_2.place(
    x=150.0,
    y=600.0,
)

x1, y1, x2, y2 = 24, 134, 366, 698
canvas11.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video7_path = "try_again.mp4"
start_video_thread(video7_path, canvas11, x1, y1, x2, y2)

#Page 12
canvas12 = Canvas(
    page_12,
    bg = "#F5F5F5",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas12.place(x = 0, y = 0)
image12_image_1 = PhotoImage(
    file=relative_to_assets_frame12("image_1.png"))
image12_1 = canvas12.create_image(
    195.0,
    23.0,
    image=image12_image_1
)

image12_image_2 = PhotoImage(
    file=relative_to_assets_frame12("image_2.png"))
image12_2 = canvas12.create_image(
    195.0,
    827.0,
    image=image12_image_2
)

image12_image_3 = PhotoImage(
    file=relative_to_assets_frame12("image_3.png"))
image12_3 = canvas12.create_image(
    195.0,
    195.0,
    image=image12_image_3
)

button12_image_1 = PhotoImage(
    file=relative_to_assets_frame12("button_1.png"))
button12_1 = Button(
    page_12,
    image=button12_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button12_1.place(
    x=24.0,
    y=704.0,
    width=342.0,
    height=60.0
)

button12_image_2 = PhotoImage(
    file=relative_to_assets_frame12("button_2.png"))
button12_2 = Button(
    page_12,
    image=button12_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:show_frame(page_4),
    relief="flat"
)
button12_2.place(
    x=24.0,
    y=632.0,
    width=342.0,
    height=60.0
)

button12_image_3 = PhotoImage(
    file=relative_to_assets_frame12("button_3.png"))
button12_3 = Button(
    page_12,
    image=button12_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_frame(page_4),
    relief="flat"
)
button12_3.place(
    x=24.0,
    y=67.0,
    width=40.0,
    height=40.0
)
x1, y1, x2, y2 = 24, 134, 366, 698
canvas12.create_rectangle(x1, y1, x2, y2, fill="#2A2A2A", outline="")
video8_path = "good_form.mp4"
start_video_thread(video8_path, canvas12, x1, y1, x2, y2)

#Page 13


window.resizable(False, False)
window.mainloop()
