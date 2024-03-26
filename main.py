import tkinter as tk
from conversion import ConversionSimulatorLogic

class ConversionSimulatorGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # initialize GUI
        self.title("CSARCH2 X22 Simulation Project")
        self.geometry("600x400")

        # Fixed window size
        self.resizable(width=False, height=False)

        # create GUI widget
        self.create_widgets()

    def create_widgets(self):
        # main label
        label = tk.Label(self, text="Binary 64 Floating Point Converter", font=("Helvetica", 16))
        label.pack(pady=10)

        # left div - for inputs
        input_frame = tk.Frame(self)
        input_frame.pack(side=tk.LEFT, padx=10)

        # input label and box
        cache_blocks_label = tk.Label(input_frame, text="Input:")
        cache_blocks_label.pack()
        self.cache_blocks_entry = tk.Entry(input_frame)
        self.cache_blocks_entry.pack()

        # checkbox for step-by-step simulation (Optional? -- idk if need natin pakita yung step-by-step tbh)
        self.step_by_step_var = tk.BooleanVar()
        step_by_step_checkbox = tk.Checkbutton(input_frame, text="Step-by-Step", variable=self.step_by_step_var)
        step_by_step_checkbox.pack()

        # convert button -- run simulation
        convert_button = tk.Button(input_frame, text="Convert", command=self.run_simulation)
        convert_button.pack(side=tk.LEFT, padx=10)

        # reset button
        reset_button = tk.Button(input_frame, text="Reset", command=self.reset_display)
        reset_button.pack(side=tk.LEFT, padx=10)

        # right div - for outputs
        result_frame = tk.Frame(self)
        result_frame.pack(side=tk.RIGHT, padx=10)

        # scrollbar for outputs
        scrollbar = tk.Scrollbar(result_frame, orient=tk.VERTICAL)
        self.result_text = tk.Text(result_frame, height=20, width=55, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.pack()

    def run_simulation(self):
        # Method to run the simulation
        self.result_text.delete(1.0, tk.END)  # Clear previous content

        # Get input and step-by-step value
        test_case = self.cache_blocks_entry.get()
        step_by_step = self.step_by_step_var.get()

        # Initialize simulator
        simulator = ConversionSimulatorLogic()
        simulator.simulate(test_case, step_by_step)

        # Display simulation completion message
        self.result_text.insert(tk.END, "Simulation Completed!\n")

    def reset_display(self):
        # Method to reset the display
        self.result_text.delete(1.0, tk.END)
        self.cache_blocks_entry.delete(0, tk.END)
        self.cache_blocks_entry.focus()

if __name__ == "__main__":
    # Run the GUI application
    app = ConversionSimulatorGUI()
    app.mainloop()
