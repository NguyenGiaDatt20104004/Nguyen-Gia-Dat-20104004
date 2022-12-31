from tkinter import *
from tkinter.filedialog import *
import os
from PIL import Image, ImageTk
import tensorflow as tf
from keras.utils import load_img, img_to_array

model = tf.keras.models.load_model("Pneumonia.h5")

root = Tk()
root.title("Diagnostic Pneumonia")
root.geometry("1200x700+200+50")
root.resizable(False,False)

main_frame = Frame(root, width=1200, height=700, bg="white")
main_frame.place(x=0, y=0)

def diagnostic():
    dudoan = {
            0 : "NORMAL",
            1 : "PNEUMONIA"
                            }

    def Genrate_pred():
        prediction = model.predict(img).argmax()
        pred = model.predict(img)
        if prediction == 0:
            Label(frame_diag, text="***Predicted Label for the image is NORMAL***", font=("Arial 13"), bg="white").place(x=520, y=80)
            a = pred.max()
            a = a*100
            Label(frame_diag, text=("Accuracy:",a,"%"), font="Arial 11", bg="white").place(x=520, y=110)
        else:
            Label(frame_diag, text="***Predicted Label for the image is PNEUMONIA***", font=("Arial 13"), bg="white").place(x=520, y=80)
            a = pred.max()
            a = a*100
            Label(frame_diag, text=("***Accuracy:",a,"%***"), font="Arial 11", bg="white").place(x=520, y=110)     

    def clear_img():
        frame_diag.destroy()

    def browsefile():
        global frame_diag, img
        file = askopenfilename(filetypes = [('All Files','*.*'),('JPG Files','*.jpg'),('PNG Files','*.png'),('JPEG Files','*.jpeg')])

        if file is not None:
            frame_diag = Frame(frame1, width=1200, height=470, bg="white")
            frame_diag.place(x=0, y=130)
            file_name = os.path.basename(file)
            Label(frame_diag, text=file_name, font=("Arial 13"), fg="black", bg="white").place(x=230, y=0)
            openfile = Image.open(file)
            openfile = openfile.resize((256,256), Image.Resampling.LANCZOS)
            showfile = ImageTk.PhotoImage(openfile)
            lb1 = Label(frame_diag, image=showfile)
            lb1.place(x=200, y=40)
        
            img = load_img(file, target_size=(64,64))
            img = img_to_array(img)
            img = img.reshape(1,64,64,3)
            img = img.astype("float32")
            img = img/255
            gen_btn = Button(frame_diag, text="Generate Prediction", font=("Arial 13"), bg="white", borderwidth=1, cursor="hand2", width=20, command=Genrate_pred)
            gen_btn.place(x=200, y=310)

            load_X_icon = ImageTk.PhotoImage(Image.open("Xicon.png"))
            clear_btn = Button(frame_diag, image=load_X_icon, bg="white", borderwidth=0, cursor="hand2", command=clear_img)
            clear_btn.place(x=500, y=0)

        mainloop()


    Diag_btn.config(fg="white", bg="Green1", font=("Arial 16 bold"))
    more_btn.config(fg="black", bg="GhostWhite", font=("Arial 16 bold"))
    frame1 = Frame(main_frame, width=1200, height=600, bg="white")
    frame1.place(x=0 , y=100)
    Label(frame1, text="Choose an image file", font=("Arial 10"), fg="black", bg="white").place(x=200,y=10)
    Label(frame1, text="Choose an image file here\nLimit 200Mb per file ∙ JPG, JPEG, PNG", font=("Arial 12"), fg="black", justify=LEFT, anchor="w", padx=30,  width=82, height=4, bg="#F8F8F8").place(x=200,y=40)
    choose_btn = Button(frame1, text="Browse files", font="Arial 13", fg="black", bg="white", cursor="hand2", width=13, borderwidth=1, command=browsefile)
    choose_btn.place(x=860, y=64)

def more():
    more_btn.config(fg="white", bg="Green1", font=("Arial 16 bold"))
    Diag_btn.config(fg="black", bg="GhostWhite", font=("Arial 16 bold"))
    frame2 = Frame(main_frame, width=1200, height=600, bg="white")
    frame2.place(x=0 , y=100)
    
    def data():
        Label(frame_more, font="Arial 28 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="BỆNH VIÊM PHỔI: NGUYÊN NHÂN, TRIỆU CHỨNG, ĐIỀU TRỊ VÀ CÁCH PHÒNG NGỪA"
            ).grid(row=1, column=1)
        Label(frame_more, font="Arial 28 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="------------------------------------------------------------------"
            ).grid(row=2, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Viêm phổi là gì?                                                                        "
            ).grid(row=3, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Viêm phổi là tình trạng viêm nhiễm (sưng) nhu mô phổi bao gồm viêm phế nang (túi khí nhỏ), túi phế nang, ống phế nang, tổ chức liên kết khe kẽ và viêm tiểu phế quản tận cùng, chủ yếu do vi khuẩn, virus, nấm gây nên. Các phế nang, đường dẫn khí chứa nhiều dịch nhầy hoặc mủ, xuất tiết dịch đường hô hấp trên gây ho đờm, sốt ớn lạnh, khó thở. Hiện tượng viêm phổi có thể ở một vùng hoặc ở một vài vùng (viêm phổi thùy hoặc “đa thùy”) hoặc toàn bộ phổi."
            ).grid(row=4, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Nguyên nhân gây bệnh viêm phổi                                            "
            ).grid(row=5, column=1)
        Label(frame_more, font="Arial 16 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="1. Viêm phổi mắc phải cộng đồng                                                                             "
            ).grid(row=6, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="+ Viêm phổi do vi khuẩn: Vi khuẩn là nguyên nhân thường gặp nhất gây viêm phổi ở trẻ em vàa người lớn. Viêm phổi do vi khuẩn nếu không nhận biết sớm và điều trị kịp thời sẽ dễ dẫn đến hậu quả khó lường, thậm chí tử vong. Các loại vi khuẩn thường gặp gồm: Streptococcus pneumoniae, Legionella pneumophila, Haemophilus influenzae, Mycoplasma pneumoniae, Chlamydia pneumoniae,…"
            ).grid(row=7, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="+ Viêm phổi do nấm: Viêm phổi do nấm là tình trạng bệnh nhân hít phải bào tử của nấm gây viêm nhiễm, ảnh hưởng nghiêm trọng đến hệ hô hấp với mức độ phát triển nhanh. Bệnh thường có diễn biến phức tạp nếu không được điều trị kịp thời có thể gây ra những biến chứng nguy hiểm thậm chí thiệt mạng."
            ).grid(row=8, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="+ Viêm phổi do hóa chất: Viêm phổi do hóa chất thường hiếm gặp, ít xảy ra nhưng cực kỳ nguy hiểm vì tỷ lệ gây tử vong cao cho người bệnh. Tùy thuộc vào loại hóa chất đã phơi nhiễm mà có mức độ nguy hiểm khác nhau. Bên cạnh tổn thương phổi, các hóa chất còn có thể gây hại cho nhiều cơ quan khác. Chính vì vậy việc phòng ngừa các tác nhân gây bệnh viêm phổi là việc làm cấp thiết, tránh những hậu quả đáng tiếc xảy ra."
            ).grid(row=9, column=1)
        Label(frame_more, font="Arial 16 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="2. Viêm phổi mắc phải ở bệnh viện                                                                           "
            ).grid(row=10, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Theo nghiên cứu, viêmm phổi bệnh viện ở cácc nước phát triển chiếm tỷ lệ 15% trong  tổng số  trường hợp nhiễm khuẩn bệnh viện và chiếm 27% xảy ra nhiễm khuẩn này ở khoa hồi sức cấp cứu. Những vi khuẩn gây ra tình trạng này là P. aeruginosa, Acinetobacter spp, Enterobacteriacae, Haemophillus spp, S. aureus (MRSA), Streptococcus spp,…"
            ).grid(row=11, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Tại Việt Nam, viêm phổi bệnh viện chiếm tỷ lệ khoảng từ 21% đến 75%, trong đó viêm  phổi do lây nhiễm qua thở máy chiếm đến 90% và được xác định sau thở máy 48 giờ. Đây là một vấn đề rất khó khăn mà các khoa lâm sàng, đặc biệt là khoa hồi sức tích cực phải đương đầu vì khó chẩn đoán, kéo dài thời gian điều trị, tốn kém rất nhiều chi phí."
            ).grid(row=12, column=1)
        Label(frame_more, font="Arial 16 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="3. Viêm phổi do hít thở                                                                                               "
            ).grid(row=13, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Nguyên  nhân  gây  viêm  phổi  ở  trường  hợp  này  là  do  người  bệnh  hít phải lượng lớn dị vật từ đường thở (miệng, hầu họng, dạ dày,…) và dị vật rơi vào phổi 2 bên. Các dị vật hít phải có thể là nước bọt, thức ăn, hóa chất, axit dịch vị,… nếu chúng đi vào phổi sẽ kích thích phản ứng viêm của niêm mạc phổi, tạo cơ hội để vi khuẩn xâm nhập và gây viêm phổi."
            ).grid(row=14, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Thời gian ủ bệnh viêm phổi bao lâu?                                       "
            ).grid(row=15, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Phần  lớn  trường  hợp,  viêm  phổi  thường  xuất  hiện  ở  dạng  cấp  tính (bệnh  kéo  dài dưới 6 tuần) với các triệu chứng rất rõ ràng ở những ngày đầu mới phát bệnh. Đặc biệt, nếu tình trạng khó thở càng trở nặng thì nguy cơ tử vong trong thời gian ngắn càng cao."
            ).grid(row=16, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Mặt  khác,  viêm  phổi  mạn  tính  cũng  có  biểu  hiện  tương  tự,  thời gian bệnh kéo dài không dứt. Một người được chẩn đoán mắc viêm phổi mạn tính khi bệnh kéo dài quá 6 tuần."
            ).grid(row=17, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Dấu hiệu viêm phổi thường gặp                                               "
            ).grid(row=18, column=1)
        Label(frame_more, font="Arial 14", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="Các  triệu  chứng  viêm  phổi  thường  gặp  như:  Đau ngực khi thở hoặc ho; Ho, ho khan, ho có đờm; Sốt trên 38 độ, đổ mồ hôi và ớn lạnh; Mệt mỏi, uể oải và chán ăn; Thở nhanh, khó thở khi gắng sức; Buồn nôn, nôn mửa hoặc tiêu chảy;"
            ).grid(row=19, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="                                "
            ).grid(row=20, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="                                  "
            ).grid(row=21, column=1)
        Label(frame_more, font="Arial 20 bold", fg="black", bg="white", justify=LEFT, wraplength=800, padx=200,
            text="               "
            ).grid(row=22, column=1)

    def myfunction(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=1178, height=600)

    canvas = Canvas(frame2, width=1200, height=600, bg="white")
    frame_more = Frame(canvas, width=1200, height=600, bg="white")
    myscrollbar=Scrollbar(frame2, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side=LEFT)
    #canvas.place(x=200,y=10)
    canvas.create_window((0,0), window=frame_more, anchor='nw')
    frame_more.bind("<Configure>",myfunction)
    data()
    #mainloop()


#Tạo các nút
Diag_btn = Button(main_frame, text="Diagnostic", font=("Arial 16 bold"), fg="black", width=15, cursor="hand2", borderwidth=1, bg="GhostWhite", command=diagnostic)
Diag_btn.place(x=400, y=50)

more_btn = Button(main_frame, text="More", font=("Arial 16 bold"), fg="black", width=15, cursor="hand2", borderwidth=1, bg="GhostWhite", command=more)
more_btn.place(x=600, y=50)

mainloop()