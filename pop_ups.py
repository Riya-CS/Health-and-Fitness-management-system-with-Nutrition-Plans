import tkinter as tk
from tkinter import Label, Button, Toplevel

def popup_message(message, title="Heyy", bg_color="#E7F2D6", font=("Otomanopee One", 12 ,), width=500, height=150):
    
    popup = Toplevel()
    popup.wm_title(title)  
    popup.geometry(f"{width}x{height}") 
    popup.configure(bg=bg_color)  

   
    popup.update_idletasks()  
    x = (popup.winfo_screenwidth() // 2) - (popup.winfo_width() // 2)
    y = (popup.winfo_screenheight() // 2) - (popup.winfo_height() // 2)
    popup.geometry(f"+{x}+{y}")  


    label = Label(popup, text=message, font=font, bg=bg_color, fg="#3C98A4")
    label.pack(pady=(20, 10))

    
    button = Button(
        popup, text="Okay", command=popup.destroy,
        bg="#82BBB5", fg="white", font=("Otomanopee One", 10, "bold"),
        activebackground="#82BBB5", activeforeground="white", relief="flat"
    )
    button.pack(pady=(0, 20))

    
    try:
        popup.iconbitmap("path_to_your_icon.ico")  
    except:
        pass  

    popup.mainloop()
#perfect

