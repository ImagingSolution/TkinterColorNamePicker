import tkinter as tk
import tkcolor



class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("tkinter Color Name Picker")
        self.master.geometry("770x350") 

        self.selected_item = None

        frame = ScrollableFrame(self.master)

        printflag = False
        count = 0
        cols = 8

        # 色の一覧を表示
        colors = vars(tkcolor)
        for color in colors:
            if color == "SNOW":
                printflag = True

            if printflag == True:
                self.button = tk.Button(
                    frame.scrollable_frame, width=12, pady = 3,
                    text = "'" + colors[color] + "'",
                    background= colors[color])
                self.button.grid(row=count // cols, column=count % cols)
                self.button.bind("<Button-1>", self.button_click)
                self.button.bind('<Motion>', self.mouse_move)

                count += 1

        frame.pack(expand = True, fill = tk.BOTH)

        # ウィンドウ下に色と名前を表示
        frame_bottom = tk.Frame(self.master, bd = 2, relief = tk.SUNKEN)
        frame_radio = tk.Frame(frame_bottom)

        # ラジオボタン
        self.radio_val = tk.IntVar()
        radio_color_name = tk.Radiobutton(frame_radio, value = 0, variable = self.radio_val, text = "Color Name", command = self.radio_changed)
        radio_rgb = tk.Radiobutton(frame_radio, value = 1, variable = self.radio_val, text = "RGB", command = self.radio_changed)
        radio_color_name.pack(anchor = tk.W)
        radio_rgb.pack(anchor = tk.W)
        frame_radio.pack(side = tk.RIGHT)
        # 色文字表示用ラベル
        self.label_color = tk.Label(frame_bottom, width = 20, bg = 'white', font = ("", 18))
        self.label_color.pack(side = tk.RIGHT, fill = tk.Y)
        # 色表示キャンバス
        self.canvas = tk.Canvas(frame_bottom, height = 40)
        self.canvas.pack(side = tk.LEFT, expand = True, fill = tk.X)
        frame_bottom.pack(side = tk.BOTTOM, fill = tk.X)

    def button_click(self, event):
        '''ボタン上をクリックしたとき'''
        color_name = self.label_color["text"]
        print(color_name)
        tk.Text().clipboard_clear()
        tk.Text().clipboard_append(color_name)

    def mouse_move(self, event):
        '''ボタン上をマウスが移動したとき'''
        self.selected_item = event.widget
        self.disp_color_info()

    def disp_color_info(self):
        '''色情報の表示'''
        if self.selected_item == None:
            return
        color = self.selected_item["bg"]
        self.canvas["bg"] = color
        if self.radio_val.get() == 0:
            self.label_color["text"] = self.selected_item["text"]
        else:
            r, g, b = self.canvas.winfo_rgb(color)
            self.label_color["text"] = f"\'#{(r >> 8):02X}{(g >> 8):02X}{(b >> 8):02X}\'"

    def radio_changed(self):
        '''ラジオボタンが変更されたとき'''
        self.disp_color_info()


class ScrollableFrame(tk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()