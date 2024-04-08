import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from pathlib import Path
from conversion import ConversionSimulatorLogic


OUTPUT_PATH = Path(__file__).parent

 # Defining function to convert relative path to absolute path
def relative_to_assets(path: str) -> Path:
    return OUTPUT_PATH / Path(path)
class ConversionSimulatorGUI(tk.Tk):

    def __init__(self):
        super().__init__()

        # initialize GUI
        self.title("CSARCH2 X22 Simulation Project")
        self.geometry("600x500")
        self.configure(bg = "#FFFFFF")

        # Fixed window size
        self.resizable(width=False, height=False)

        # create GUI widget
        self.create_widgets()

    def create_widgets(self):

        # Create Canvas and Load Background Images
        canvas = Canvas(self, height=500, width=600, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)

        # main label
        label = tk.Label(self, text="Binary 64 Floating Point Converter", font=("Helvetica", 16))
        label.pack(side=tk.TOP, pady=30)

        self.background_image = ImageTk.PhotoImage(file=relative_to_assets("image_1.png"))
        image_1 = canvas.create_image(301.0, 301.0, image=self.background_image)

        self.image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
        image_2 = canvas.create_image(385.0, 297.0, image=self.image_2)

        self.image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
        image_3 = canvas.create_image(92.0, 297.0, image=self.image_3)

        self.image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
        image_4 = canvas.create_image(300.0, 53.0, image=self.image_4)

        # left div - for inputs
        self.input_frame = tk.Frame(self, bg='')
        self.input_frame.pack(side=tk.LEFT, padx=23)

        # left div - for inputs (top part)
        self.input_top_frame = tk.Frame(self.input_frame, bg='')  # Set background color to transparent
        self.input_top_frame.pack(side=tk.TOP, padx=24, pady=30)

        # input label and box
        input_label = tk.Label(self.input_top_frame, text="Choose Input:") # label
        input_label.pack()

        self.test_case_var = tk.StringVar(value="Binary") # default is binary
        r1 = ttk.Radiobutton(self.input_top_frame, text='Binary', value='Binary', variable=self.test_case_var, command=self.show_entries)
        r1.pack()
        r2 = ttk.Radiobutton(self.input_top_frame, text='Decimal', value='Decimal', variable=self.test_case_var, command=self.show_entries)
        r2.pack()

        tk.Label(self.input_top_frame).pack()  # Empty label for padding

        # Binary entry fields
        self.input_binary_entry = tk.Entry(self.input_top_frame, width=14)  
        self.input_binary_entrytext = tk.Label(self.input_top_frame, text=" x 2^ ") 
        self.input_exponent_binary_entry = tk.Entry(self.input_top_frame, width=7)  

        self.input_binary_entry.pack(side=tk.TOP)
        self.input_binary_entrytext.pack(side=tk.LEFT)
        self.input_exponent_binary_entry.pack(side=tk.LEFT)

        # Decimal entry fields
        self.input_decimal_entry = tk.Entry(self.input_top_frame, width=14)  
        self.input_decimal_entrytext = tk.Label(self.input_top_frame, text=" x 10^ ") 
        self.input_exponent_decimal_entry = tk.Entry(self.input_top_frame, width=7)  

        # left div - for inputs (bottom part)
        self.input_bottom_frame = tk.Frame(self.input_frame, bg='')  # Set background color to transparent
        self.input_bottom_frame.pack(side=tk.BOTTOM, pady=10)

        # Convert button -- run simulation
        convert_button = tk.Button(self.input_bottom_frame, text="Convert", command=self.run_simulation)
        convert_button.pack(side=tk.TOP, padx=10, pady=5)

        # Reset button
        reset_button = tk.Button(self.input_bottom_frame, text="Reset", command=self.reset_display)
        reset_button.pack(side=tk.TOP, pady=5)

        # right div - for outputs
        result_frame = tk.Frame(self, bg='')  # Set background color to transparent
        result_frame.pack(side=tk.RIGHT, padx=20)

        # scrollbar for outputs of step-by-step
        scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
        self.result_text = tk.Text(result_frame, height=20, width=45, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack()

        tk.Label(result_frame).pack()  # Empty label for padding

        # Print to Txt File output
        save_button = tk.Button(result_frame, text="Save to File", command=self.save_to_file)
        save_button.pack()

    def show_entries(self):

        # Show or hide entry fields based on selected input type
        if self.test_case_var.get() == "Binary":
            self.input_binary_entry.pack(side=tk.TOP)
            self.input_binary_entrytext.pack(side=tk.LEFT)
            self.input_exponent_binary_entry.pack(side=tk.LEFT)

            # Clear existing decimal entry widgets
            self.input_decimal_entry.pack_forget()
            self.input_decimal_entrytext.pack_forget()
            self.input_exponent_decimal_entry.pack_forget()


        elif self.test_case_var.get() == "Decimal":
            self.input_decimal_entry.pack(side=tk.TOP)
            self.input_decimal_entrytext.pack(side=tk.LEFT)
            self.input_exponent_decimal_entry.pack(side=tk.LEFT)

            # Clear existing binary entry widgets
            self.input_binary_entry.pack_forget()
            self.input_binary_entrytext.pack_forget()
            self.input_exponent_binary_entry.pack_forget()


# LOGIC SKELETON -- LOGIC FUNCTIONS ARE IN CONVERSION.PY

    def run_simulation(self):
        self.result_text.config(state="normal")

        # Method to run the simulation
        self.result_text.delete(1.0, tk.END)  # Clear previous content

        # Get input values based on selected input type
        if self.test_case_var.get() == "Binary":
            # Fetch binary input values
            binary_input = self.input_binary_entry.get()
            binary_exponent_input = self.input_exponent_binary_entry.get()

            # Call validateInput from conversion.py
            checkValid = ConversionSimulatorLogic.validateInput(binary_input, binary_exponent_input, self.test_case_var.get(), self.result_text)

            if checkValid == True:      

                self.result_text.insert(tk.END, "Binary:")
                self.result_text.insert(tk.END, binary_input)
                self. result_text.insert(tk.END, " x 2^ ")
                self.result_text.insert(tk.END, binary_exponent_input)   
                
                # convert to IEEE-754 rep
                sign, e_prime, f = ConversionSimulatorLogic.converter64(binary_input, binary_exponent_input)
                converted_IEEE = sign + e_prime + f

                # Convert to Hex
                converted_hex = ConversionSimulatorLogic.convert_to_hexadecimal(converted_IEEE)


        elif self.test_case_var.get() == "Decimal":
            # Fetch decimal input values
            decimal_input = self.input_decimal_entry.get()
            decimal_exponent_input = self.input_exponent_decimal_entry.get()

            # Call validateInput from conversion.py
            checkValid = ConversionSimulatorLogic.validateInput(decimal_input, decimal_exponent_input, self.test_case_var, self.result_text)

            # Convert to Binary
            if checkValid == True:
                # Convert to Binary                
                whole_decimal = str(ConversionSimulatorLogic.descientific_decimal(decimal_input, decimal_exponent_input))
                binary_of_decimal = ConversionSimulatorLogic.convert_to_binary(whole_decimal)
                binary_input, binary_exponent_input = ConversionSimulatorLogic.normalize(binary_of_decimal, 0)

                self.result_text.insert(tk.END, "\nBinary:")
                self.result_text.insert(tk.END, binary_input)
                self. result_text.insert(tk.END, " x 2^")
                self.result_text.insert(tk.END, binary_exponent_input)
                
                # convert to IEEE-754 rep
                sign, e_prime, f = ConversionSimulatorLogic.converter64(binary_input, binary_exponent_input)
                converted_IEEE = sign + e_prime + f
                
                # Convert to Hex
                converted_hex = ConversionSimulatorLogic.convert_to_hexadecimal(converted_IEEE)

        self.result_text.insert(tk.END, "\n\nIEEE-754 Representation:\n")
        self.result_text.insert(tk.END, sign)
        self.result_text.insert(tk.END, " ")
        self.result_text.insert(tk.END, e_prime)
        self.result_text.insert(tk.END, " ")
        self.result_text.insert(tk.END, f)

        self.result_text.insert(tk.END, "\n\nIEEE-754 Hexadecimal Representation:\n")
        self.result_text.insert(tk.END, converted_hex)

        self.result_text.insert(tk.END, "\n\nSimulation Completed!\n")

        self.result_text.config(state="disabled") # Disable user editing


    def reset_display(self):
        # Method to reset the display
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

    def save_to_file(self):
        
        try:
            content = self.result_text.get("1.0", tk.END)

            file = open("resultOutput.txt", 'w')
            file.write(content)
            file.close()  # Close the file explicitly
            self.result_text.insert(tk.END, "\nResult exported to resultOutput.txt!\n")
        except IOError:
            self.result_text.insert(tk.END, "\nError: Unable to export result.\n")

if __name__ == "__main__":
    # Run the GUI application
    app = ConversionSimulatorGUI()
    app.mainloop()
