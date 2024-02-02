import tkinter
import tkinter.messagebox
import customtkinter
from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import os

customtkinter.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(os.path.join("", "custom_theme.json"))  # Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.set_default_color_theme("dark-blue") 

#Content Text
content_landingpage1 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."
content_landingpage2 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."
content_landingpage3 = "Experience clarity and precision with our innovative solution. \nStreamlined and efficient, our product delivers a seamless experience."
content_start_page = "Your text.\nDecode your text. We analyze first 500 tokens."
content_aboutpage1 = "Factify, your trusted ally in navigating the complex world of news and information. We understand the importance of reliable, unbiased news in today's \ninterconnected society, and we are committed to empowering you to make informed decisions."
content_aboutpage2 = "At Factify, our mission is simple: to foster a more informed and discerning public by helping you distinguish between credible news and misinformation. \nWe believe that access to accurate information is a cornerstone of a healthy and thriving society."

#get images
chat_img_data = Image.open(os.path.join('images', "chat.png"), 'r')
logo_img_data = Image.open(os.path.join('images', "logo.png"), 'r')
about_img_data = Image.open(os.path.join('images', "about.png"), 'r')
add_img_data = Image.open(os.path.join('images', "add.png"), 'r')
delete_img_data = Image.open(os.path.join('images', "delete.png"), 'r')
updates_img_data = Image.open(os.path.join('images', "updates.png"), 'r')
target_img_data = Image.open(os.path.join('images', "target.png"), 'r')
trendup_img_data = Image.open(os.path.join('images', "trend_up.png"), 'r')
arrowleft_img_data = Image.open(os.path.join('images', "arrow-left.png"), 'r')
profile1_img_data =Image.open(os.path.join('images', "profile1.png"), 'r')
profile2_img_data =Image.open(os.path.join('images', "profile2.png"), 'r')
profile3_img_data =Image.open(os.path.join('images', "profile3.png"), 'r')

#set it to CTKImages
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(60, 60))
about_img = CTkImage(dark_image=about_img_data, light_image=about_img_data)
add_img = CTkImage(dark_image=add_img_data, light_image=add_img_data)
delete_img = CTkImage(dark_image=delete_img_data, light_image=delete_img_data)
updates_img = CTkImage(dark_image=updates_img_data, light_image=updates_img_data)
chat_img = CTkImage(dark_image=chat_img_data, light_image=chat_img_data)
target_img = CTkImage(dark_image=target_img_data, light_image=target_img_data)
trendup_img = CTkImage(dark_image=trendup_img_data, light_image=trendup_img_data)
arrowleft_img = CTkImage(dark_image=arrowleft_img_data, light_image=arrowleft_img_data)
profile1_img = CTkImage(dark_image=profile1_img_data, light_image=profile1_img_data, size=(200,200))
profile2_img = CTkImage(dark_image=profile2_img_data, light_image=profile2_img_data, size=(200,200))
profile3_img = CTkImage(dark_image=profile3_img_data, light_image=profile3_img_data, size=(200,200))

class PreviousChats(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.radiobuttons = []
        for i in range(30):
            self.sidebar = customtkinter.CTkButton(self,  height=48, width=280, text="Values here", image=chat_img, compound=LEFT, anchor="w")
            self.sidebar.grid(row=i, column=0, padx=20, pady=(20, 10))

class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self,parent)
  
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # SIDEBAR
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, height=48, width=280, text="Factify", image=logo_img, font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"), compound=LEFT)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # TODO must get to a data to database
        self.my_frame = PreviousChats(master=self.sidebar_frame, width=300, fg_color="#F8F8F8")
        self.my_frame.grid(row=1, column=0, sticky="nsew")
      

        self.new_chat = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280 , text="Start a new chat",text_color="white", fg_color="#004CC6", image=add_img, compound=LEFT)
        self.new_chat.grid(row=4, column=0, pady=10)

        self.delete_conversation = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Clear all conversation", image=delete_img, compound=LEFT , anchor="w")
        self.delete_conversation.grid(row=6, column=0, pady=(10, 0))

        self.updates_and_faq = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Updates and FAQ", image=updates_img, compound=LEFT , anchor="w")
        self.updates_and_faq.grid(row=7, column=0, pady=(10, 0))

        self.about_btn = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="About", image=about_img, compound=LEFT , anchor="w", command=lambda: controller.show_frame(AboutPage))
        self.about_btn.grid(row=8, column=0, pady=(10, 20))

        # MAIN CONTENT
        self.main_content = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), rowspan=3 , sticky="nsew")
        self.main_content.grid_rowconfigure(3, weight=1)
        self.main_content.grid_columnconfigure(3, weight=1)

        self.main_header1 = customtkinter.CTkLabel(self.main_content, text="Fake News Detector", font=controller.set_font(40, "bold"), justify=LEFT)
        self.main_header1.grid(row=3, column=3, padx=(0,970), pady =(0,800))

        self.sub_header = customtkinter.CTkLabel(self.main_content, text=content_start_page, font=controller.set_font(20, "normal"), justify=LEFT)
        self.sub_header.grid(row=3, column=3, padx=(0,920), pady=(0,700))

        self.textbox = customtkinter.CTkTextbox(self.main_content,height=500, width=400, corner_radius=15, border_width=2)
        self.textbox.grid(row=3, column=3, padx=(100,100), pady=(0, 110),sticky="ew", columnspan=3)
        
        self.btn_clear = customtkinter.CTkButton(self.main_content, text="Clear", height=50, width=70, text_color="#2364cd", fg_color="#e4eaf3")
        self.btn_clear.grid(row=3, column=3, padx=(1100, 0), pady=(450,0))

        self.detect = customtkinter.CTkButton(self.main_content , text="Detect" , height=50, width=70, text_color="white", fg_color="#004CC6")
        self.detect.grid(row=3, column=3, padx=(1300, 0),pady=(450,0))
        
class LandingPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self,parent)
     
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # SIDEBAR
        self.sidebar_frame = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, height=48, width=280, text="Factify", image=logo_img, font=customtkinter.CTkFont(family="Inter", size=24, weight="bold"), compound=LEFT)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # TODO must get to a data to database
        self.my_frame = PreviousChats(master=self.sidebar_frame, width=300, fg_color="#F8F8F8")
        self.my_frame.grid(row=1, column=0, sticky="nsew")

        self.new_chat = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280 , text="Start a new chat",text_color="white", fg_color="#004CC6", image=add_img, compound=LEFT)
        self.new_chat.grid(row=4, column=0, pady=10)

        self.delete_conversation = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Clear all conversation", image=delete_img, compound=LEFT , anchor="w")
        self.delete_conversation.grid(row=6, column=0, pady=(10, 0))

        self.updates_and_faq = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="Updates and FAQ", image=updates_img, compound=LEFT , anchor="w")
        self.updates_and_faq.grid(row=7, column=0, pady=(10, 0))

        self.about_btn = customtkinter.CTkButton(self.sidebar_frame, height=48, width=280, text="About", image=about_img, compound=LEFT , anchor="w", command=lambda: controller.show_frame(AboutPage))
        self.about_btn.grid(row=8, column=0, pady=(10, 20))

        # MAIN CONTENT
        self.main_content = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_content.grid(row=0, column=1, padx=(10, 10), pady=(10, 10), rowspan=4 , sticky="nsew")
        self.main_content.grid_rowconfigure(4, weight=1)
        self.main_content.grid_columnconfigure(4, weight=1)
       
        self.main_header = customtkinter.CTkLabel(self.main_content, text="Welcome to Factify", font=controller.set_font(48, "bold"), text_color="#004CC6")
        self.main_header.grid(row=4, column=4, pady=(0,600))

        self.sub_header = customtkinter.CTkLabel(self.main_content,text="The power of AI at your service - Tame the knowledge.", font=controller.set_font(16, "bold"))
        self.sub_header.grid(row=4, column=4, pady=(0,510))

        self.cta = customtkinter.CTkButton(self.main_content,  height=48, width=70, text="Start", command=lambda: controller.show_frame(StartPage) , fg_color="#004CC6", text_color="white")
        self.cta.grid(row=4, column=4, pady=(0,300))

        self.card_title1 = customtkinter.CTkLabel(self.main_content,text="Clear and precise", font=controller.set_font(16, "bold"), image=about_img, compound=TOP)
        self.card_title1.grid(row=4, column=4, padx=(0,1000))
        self.card_content_landingpage1 = customtkinter.CTkLabel(self.main_content, font=controller.set_font(14, "normal"), width=300,text=content_landingpage1, anchor="w")
        self.card_content_landingpage1.grid(row=4, column=4, padx=(0,1000), pady=(100,0))

        self.card_title2 = customtkinter.CTkLabel(self.main_content,text="Personalized answers", font=controller.set_font(16, "bold"), image=target_img, compound=TOP)
        self.card_title2.grid(row=4, column=4)
        self.card_content_landingpage2 = customtkinter.CTkLabel(self.main_content, font=controller.set_font(14, "normal"), width=300, text=content_landingpage2, anchor="w")
        self.card_content_landingpage2.grid(row=4, column=4,pady=(100,0))
        
        self.card_title3 = customtkinter.CTkLabel(self.main_content,text="Increased efficiency", font=controller.set_font(16, "bold"), image=trendup_img, compound=TOP)
        self.card_title3.grid(row=4, column=4, padx=(1000,0))
        self.card_content_landingpage3 = customtkinter.CTkLabel(self.main_content, font=controller.set_font(14, "normal"), width=300,text=content_landingpage3, anchor="w")                                                   
        self.card_content_landingpage3.grid(row=4, column=4, padx=(1000,0) , pady=(100,0))

class AboutPage(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self,parent)
      
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
      
        # configure grid layout (12x12)
        self.main_content = customtkinter.CTkFrame(self, corner_radius=15, width=self.winfo_screenwidth())
        self.main_content.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), rowspan=11 , sticky="nsew")
        self.main_content.grid_columnconfigure(list(range(13)), weight=1)
        self.main_content.grid_rowconfigure(list(range(13)), weight=1)

        # for x in range(12):
        #     self.main_header = customtkinter.CTkLabel(self.main_content, text="Fake News", justify=LEFT, fg_color="#ff0000")
        #     self.main_header.grid(row=4, column=x)
        
        self.back_btn = customtkinter.CTkButton(self.main_content, text="Back to app", command=lambda: controller.show_frame(StartPage), text_color="#004CC6",font=controller.set_font(18, "normal"), image=arrowleft_img, compound=LEFT)
        self.back_btn.grid(row=0, column=1)

        self.header = customtkinter.CTkLabel(self.main_content, text="About" , font=controller.set_font(40, "bold"),anchor="w")
        self.header.grid(row=1, column=1)

        self.content1 =customtkinter.CTkLabel(self.main_content, text=content_aboutpage1 , font=controller.set_font(16, "normal"), justify="left", anchor="w" )
        self.content1.grid(row=2, column=0, columnspan=9, padx=(70, 0))

        self.content1 =customtkinter.CTkLabel(self.main_content, text=content_aboutpage2 , font=controller.set_font(16, "normal"), justify="left", anchor="w" )
        self.content1.grid(row=3, column=0, columnspan=9, padx=(70, 0), pady=(0,100))

        self.content1 =customtkinter.CTkLabel(self.main_content, text=content_aboutpage2 , font=controller.set_font(16, "normal"), justify="left", anchor="w" )
        self.content1.grid(row=3, column=0, columnspan=9, padx=(70, 0), pady=(0,100))


        self.profile_header = customtkinter.CTkLabel(self.main_content, text="Meet the Factify team", font=controller.set_font(20, "normal"))
        self.profile_header.grid(row=4, column=4,pady=(0,300))

        self.profilepic1 = customtkinter.CTkLabel(self.main_content, width=100, height=200, image=profile1_img, text="")
        self.profilepic1.grid(row=4, column=3, pady=(50,0))
        self.profilepic1 = customtkinter.CTkLabel(self.main_content, text="Developer\nAbner Dominic B. Belotindos", font=controller.set_font(16, "bold"))
        self.profilepic1.grid(row=5, column=3, pady=(0,100))

        self.profilepic1 = customtkinter.CTkLabel(self.main_content, width=200, height=200, image=profile2_img, text="")
        self.profilepic1.grid(row=4, column=4, pady=(50,0))
        self.profilepic1 = customtkinter.CTkLabel(self.main_content, text="Developer\nJohn Andrei A. Manalo", font=controller.set_font(16, "bold"))
        self.profilepic1.grid(row=5, column=4, pady=(0,100))

        self.profilepic1 = customtkinter.CTkLabel(self.main_content, width=200, height=200, image=profile3_img, text="")
        self.profilepic1.grid(row=4, column=5, pady=(50,0))
        self.profilepic1 = customtkinter.CTkLabel(self.main_content, text="Developer\nLendon N. Ato", font=controller.set_font(16, "bold"))
        self.profilepic1.grid(row=5, column=5, pady=(0,100))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        container = customtkinter.CTkFrame(self)
        
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        #List all Frame class to interchange the display/design
        for F in (LandingPage,StartPage, AboutPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LandingPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def set_font(self, size, weight):
        return customtkinter.CTkFont(family="Inter", size=size , weight=weight)
    
    
if __name__ == "__main__":
    
    app = App()
    app.after(0, lambda:app.state('zoomed'))
    
    # TODO Resolve Logo of the app
    # app.iconphoto(True, tkinter.PhotoImage(file=os.path.join('images', "logo.png")))
    app.title("Factify")
    app.mainloop()