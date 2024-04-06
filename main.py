import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from PIL import Image, ImageTk
from pathlib import Path
from conversion import ConversionSimulatorLogic


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\rombl\OneDrive - De La Salle University - Manila\CSARCH2\Simulation Project\CSARCH2-Binary64FloatingPointConverterSimulationProject\build\assets\frame0") # change to path in local folder

 # Defining function to convert relative path to absolute path
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
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
        input_frame = tk.Frame(self, bg='')  # Set background color to transparent
        input_frame.pack(side=tk.LEFT, padx=25)

        # input label and box
        input_label = tk.Label(input_frame, text="Input:")  # label
        input_label.pack()
        self.input_entry = tk.Entry(input_frame)  # textbox
        self.input_entry.pack()

        tk.Label(input_frame).pack()  # Empty label for padding

        # checkbox for step-by-step simulation (Optional? -- idk if need natin pakita yung step-by-step tbh)
        self.step_by_step_var = tk.BooleanVar()
        step_by_step_checkbox = tk.Checkbutton(input_frame, text="Step-by-Step", variable=self.step_by_step_var)
        step_by_step_checkbox.pack()

        # Adding padding
        tk.Label(input_frame).pack()  # Empty label for padding

        # convert button -- run simulation
        convert_button = tk.Button(input_frame, text="Convert", command=self.run_simulation)
        convert_button.pack(side=tk.LEFT, padx=10)

        # reset button
        reset_button = tk.Button(input_frame, text="Reset", command=self.reset_display)
        reset_button.pack(side=tk.LEFT, padx=10)

        # right div - for outputs
        result_frame = tk.Frame(self, bg='')  # Set background color to transparent
        result_frame.pack(side=tk.RIGHT, padx=20)

        # Binary output
        binary_output_label = tk.Label(result_frame, text="Binary:")
        binary_output_label.pack()

        # Hexadecimal Output
        hex_output_label = tk.Label(result_frame, text="Hexadecimal:")
        hex_output_label.pack()

        # scrollbar for outputs of step-by-step
        scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
        self.result_text = tk.Text(result_frame, height=17, width=45, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack()

        tk.Label(result_frame).pack()  # Empty label for padding

        # Print to Txt File output
        save_button = tk.Button(result_frame, text="Save to File", command=self.save_to_file)
        save_button.pack()


    def run_simulation(self):
        # Method to run the simulation
        self.result_text.delete(1.0, tk.END)  # Clear previous content

        # Get input and step-by-step value
        test_case = self.input_entry.get()
        step_by_step = self.step_by_step_var.get()

        # Initialize simulator
        simulator = ConversionSimulatorLogic()
        simulator.simulate(test_case, step_by_step)

        # Display simulation completion message
        self.result_text.insert(tk.END, "Simulation Completed!\n")

    def reset_display(self):
        # Method to reset the display
        self.result_text.delete(1.0, tk.END)
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

    def save_to_file(self):
        pass  # Implement save to file logic

if __name__ == "__main__":
    # Run the GUI application
    app = ConversionSimulatorGUI()
    app.mainloop()
