from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageSteganographyApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Image Steganography")  # Set window title
        self.root.configure(bg="#2f4155")  # Set window background color
        self.root.wm_attributes("-fullscreen", True)  # Make window full screen
        
        # Load and display the logo image
        '''NOTE : This File directory has to be changed if this code is being used in some other laptops - the logo is in resource folder.'''
        logo_image = Image.open("D:\\SEM-1 PROJECT DC\\FINAL PROJECT CODE\\RESOURCES\\1.png")  # Replace 'path_to_your_logo.png' with your logo file path
        logo = ImageTk.PhotoImage(logo_image)
        self.logo_label = Label(self.root, image=logo, bg="#2f4155")
        self.logo_label.image = logo # Keep a reference to avoid garbage collection
        self.logo_label.place(x=200, y=50)  # Adjust the position as needed
        Label(self.root,text="Image Steganography",bg="#2f4155",fg="pink",font=("arial 35 bold")).place(x=700,y=60) #Placing the text in frame

        # Label to display the selected image
        self.lbl = Label(self.root, bg="black")
        self.lbl.place(x=150, y=130)  # Place the label at a specific position
        
        # Create text input frame and buttons frame
        self.create_text_input_frame()
        self.create_buttons_frame()
        
    def create_text_input_frame(self):
        # Frame for text input
        self.frame_text_input = Frame(self.root, bg="white", width=500, height=500)
        self.frame_text_input.place(x=700, y=130)  # Place text input frame
        
        # Text box for user input
        self.text_box = Text(self.frame_text_input, font="arial 25", bg="white", fg="black", wrap=WORD)
        self.text_box.place(x=0, y=0)  # Place text box inside the frame
        
    def create_buttons_frame(self):
        # Frame for buttons
        self.frame_buttons = Frame(self.root, bd=7, bg="blue", width=1150, height=100, relief=GROOVE)
        self.frame_buttons.place(x=100, y=640)  # Place buttons frame
        
        # Button to import an image
        btn_import_image = Button(self.frame_buttons, text="Import Image", width=15, height=2,
                                  font="arial 12 bold", fg="pink", bg="black", command=self.get_image)
        btn_import_image.place(x=50, y=20)  # Place the import image button
        
        # Button to hide message and save image
        btn_hide_msg = Button(self.frame_buttons, text="Hide message & save image", width=25, height=2,
                              font="arial 12 bold", fg="pink", bg="black", command=self.hide_message)
        btn_hide_msg.place(x=250, y=20)  # Place the hide message button
        
        # Button to show the hidden message
        btn_show_msg = Button(self.frame_buttons, text="Show hidden message", width=30, height=2,
                              font="arial 12 bold", fg="pink", bg="black", command=self.show_hidden_message)
        btn_show_msg.place(x=540, y=20)  # Place the show hidden message button
        
        # Button to exit the program
        btn_exit = Button(self.frame_buttons, text="Exit", width=15, height=2, font="arial 12 bold",
                          fg="pink", bg="black", command=self.root.destroy)
        btn_exit.place(x=900, y=20)  # Place the exit button
    
    def get_image(self):
        # Function to get an image file
        self.filename = filedialog.askopenfile(
            initialdir=os.getcwd(),
            title="Select Image File",
            filetype=(("PNG File", "*.png"), ("JPG File", "*.jpg"), ("All Files", "*.*"))
        )
        if self.filename:
            image_file = Image.open(self.filename.name)
            img = ImageTk.PhotoImage(image_file)
            self.lbl.configure(image=img)
            self.lbl.image = img
            self.lbl.configure(width=img.width(), height=img.height())
    
    def embed_text_in_image(self, image_path, text):
        #function which does lsb steganography in picture
        image = Image.open(image_path) # importing the user image
        
        binary_format_text = "".join(format(ord(char), '08b')for char in text) # converts every single input text character's ascii value to binary format (8-bit)
        
        if (len(binary_format_text) > image.width * image.height * 3): #error condition if the image is not capable to hold the data
            raise Exception("Text is too large to embed in the image.")
        
        binary_index = 0 #keeps track of the position within the binary text that is being hidden.
        
        #lsb insertion
        for x in range(image.width): #accessing all the bits
            for y in range(image.height):
                pixel = list(image.getpixel((x,y))) #getting the list as pixels of x,y
                for color_channel in range(3): #considering the rgb elements in every pixel
                    if binary_index < len(binary_format_text): #checking if the picture has more binary data to hide 
                        pixel[color_channel] = int(f"{pixel[color_channel]:08b}"[:-1]+binary_format_text[binary_index],2) #modifies the least significant bit (LSB) of each color channel to embed one bit of the binary text.
                        binary_index+=1 #updating index for next iteration
                    else:
                        break
                image.putpixel((x,y),tuple(pixel)) #updating the image with new pixel data
                if binary_index >= len(binary_format_text): # breaks the loop if all the binary text has been hidden in the image.
                    break
        
        
        return image #returns the image        
    
    
    def extract_text_from_image(self, image_path):
        # Open the image
        image = Image.open(image_path)
            
        binary_text = ""
        binary_index = 0
        text = ""
    
        # Loop through each pixel of the image
        for x in range(image.width):
            for y in range(image.height):
                pixel = list(image.getpixel((x, y)))

                # Extract LSBs from each color channel
                for color_channel in range(3):
                    # Extract the LSB and add it to the binary_text
                    binary_text += str(pixel[color_channel] & 1)
                    binary_index += 1

                    # Check for the end of the text
                    if binary_index % 8 == 0:
                        # Convert the binary_text to ASCII character
                        character = chr(int(binary_text, 2))
                        # If character is null terminator, stop extraction
                        if character == '\x00':
                            return text
                        text += character
                        binary_text = ""
            
            return text
        
    
    def hide_message(self):
        # Function to hide a message within an image
        if not hasattr(self, 'filename'):
            self.text_box.insert(END, "Please select an image first.\n")
            return
        
        text_to_hide = self.text_box.get("1.0", "end-1c")
        try:
            self.output_image = self.embed_text_in_image(self.filename.name, text_to_hide)
            if not hasattr(self,'output_image'):
                self.text_box.insert(END,"No image to save.")
                return

            file_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")]
            )
            
            if file_path:
                self.output_image.save(file_path)
                self.text_box.insert(END, f"The file has been saved as {file_path}.\n")
                
        except Exception as e:
            self.text_box.insert(END, f"Error: {str(e)}\n")
            

    
    def show_hidden_message(self):
        # Function to show the hidden message within an image
        if not hasattr(self, 'filename'):
            self.text_box.insert(END, "Please select an image first.\n")
            return
        
        try:
            hidden_message = self.extract_text_from_image(self.filename.name)
            self.text_box.insert(END, f"The hidden message is:\n {hidden_message}\n")
        except Exception as e:
            self.text_box.insert(END, f"Error: {str(e)}\n")
    
# Initialize the main window and start the application
root = Tk()
app = ImageSteganographyApp(root)
root.mainloop()
