# -*- coding: UTF-8 -*-
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.messagebox import showinfo
import  os

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("PDF to JPG Progame")
        self.master.rowconfigure(50, weight=10)
        self.master.columnconfigure(50, weight=10)
        self.grid(sticky=W+E+N+S)
        #生成三个按钮，并将对应的需要转换的图片格式作为参数传给load_file函数
        self.button = Button(self, text="选择需要转成JPG格式的PDF文件", command=lambda:self.load_file("jpg","pdf"), width=50)
        self.button.grid(row=1, column=0, sticky=W)
        self.button2 = Button(self, text="选择需要转成PNG格式的PDF文件", command=lambda:self.load_file("png","pdf"), width=50)
        self.button2.grid(row=2, column=0, sticky=W)
        self.button3 = Button(self, text="选择需要转成JPG格式的PNG文件", command=lambda:self.load_file("jpg","png"), width=50)
        self.button3.grid(row=3, column=0, sticky=W)



    def load_file(self,converttype,imagetpye):
        #点击按钮后触发的文件选择框，converttype函数传过来的值决定选择哪种文件类型
        fname = askopenfilename(filetypes=(("PDF files", "*.%s;" % (imagetpye)),
                                           ("All files", "*.*") ))
        if fname:
            try:
                #将文件进行重命名，以便让下面的convert函数使用
                desjpg = fname.replace(r'.%s' % (imagetpye) ,'.%s' % (converttype))
                #调用macgick的convert函数，进行格式转换，并将pdf和为一张图片，macgick程序和convert程序放在bin目录下调用
                os.system(r'".\bin\convert  +append  -quality 1000 -density 100  %s %s"' % (fname , desjpg) )
                showinfo('提示','格式转化完毕,输出文件在本地同个目录')
            except:                     # <- naked except is a bad idea
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return


if __name__ == "__main__":
    MyFrame().mainloop()