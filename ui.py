# ui.py

from tkinter import *

class LiftCalculatorUI:
    def __init__(self, master, logic):
        self.master = master
        self.logic = logic
        self.current_var = StringVar(value="0")

        # Combined label and text unit      
        self.labels = {
            "force": ("(LF) Lift Force", "N"),
            "area": ("(A) Wing Surface Area", "m²"),
            "density": ("(ρ) Density of Air", "kg/m³"),
            "coefficient": ("(CL) Lift Coefficient", ""),
            "velocity": ("(V) Velocity of Air Flow", "m/s")
            
        }

        # Maps variable ID to which one we're solving for
        self.output_fields = {
            "0": "force",
            "1": "area",
            "2": "density",
            "3": "coefficient",
            "4": "velocity"
        }

        # Dicts for widgets
        self.fields = {}
        self.labels_widgets = {}
        self.units = {}

        self.build_widgets()
        self.set_variable("0") # Set Force to default output

    def build_widgets(self):
        # Variable selection buttons
        Button(self.master, text="Force", command=lambda: self.set_variable("0"), fg='#3886da').grid(column=1, row=0)
        Button(self.master, text="Wing SA", command=lambda: self.set_variable("1"), fg='#3886da').grid(column=2, row=0)
        Button(self.master, text="Density", command=lambda: self.set_variable("2"), fg='#3886da').grid(column=3, row=0)
        Button(self.master, text="Coefficient", command=lambda: self.set_variable("3"), fg='#3886da').grid(column=4, row=0)
        Button(self.master, text="Velocity", command=lambda: self.set_variable("4"), fg='#3886da').grid(column=5, row=0)

        # Equation label
        self.labelEquation = Label(self.master, text="")
        self.labelEquation.place(relx=0.85, rely=0.2, anchor=NE)

        self.input_positions()

        self.output_positions()

        # Calculate button
        Button(self.master, text="Calculate", fg="red", command=self.calculate).place(relx=0.5, rely=0.9, anchor=S)

    def input_positions(self):
        for idx in range(4):
            row = 1 + idx * 2
            label = Label(self.master)
            label.grid(column=0, row=row)
            entry = Entry(self.master, width=22, bg="#3886da", fg="#ffffff")
            entry.grid(column=0, row=row + 1)
            unit = Label(self.master)
            unit.grid(column=1, row=row + 1)

            self.labels_widgets[f"input{idx}"] = label
            self.fields[f"input{idx}"] = entry
            self.units[f"input{idx}"] = unit

    def output_positions(self):
        self.labelOutput = Label(self.master)
        self.labelOutput.place(relx=0.5, rely=0.75, anchor=S)
        self.outputEntry = Entry(self.master, width=20)
        self.outputEntry.place(relx=0.5, rely=0.8, anchor=S)
        self.unitOutput = Label(self.master)
        self.unitOutput.place(relx=0.65, rely=0.8, anchor=S)

    def set_variable(self, var):
        self.current_var.set(var)
        self.labelEquation.config(text=self.logic.get_equation_text(var))

        # Determine which variable is the output
        solve_for = self.output_fields[var]
        input_vars = [k for k in self.labels if k != solve_for]

        # Clear all fields on tab switch
        for entry in self.fields.values():
            entry.delete(0, END)
        self.outputEntry.delete(0, END)
        self.unitOutput.config(text="")

        # Update input field labels and units
        for idx, var_name in enumerate(input_vars):
            label_text, unit = self.labels[var_name]
            self.labels_widgets[f"input{idx}"].config(text=label_text)
            self.units[f"input{idx}"].config(text=unit)
            self.fields[f"input{idx}"].config(bg='#3886da', fg='#ffffff')

        # Update output label and unit
        output_text, output_unit = self.labels[solve_for]
        self.labelOutput.config(text=output_text)
        self.unitOutput.config(text=output_unit)


    def calculate(self):

        # 
        var = self.current_var.get()
        inputs = [
            self.fields["input0"],
            self.fields["input1"],
            self.fields["input2"],
            self.fields["input3"]
        ]
        result = self.logic.calculate(var, inputs)

        # Replaces old output with updated value
        self.outputEntry.delete(0, END)
        self.outputEntry.insert(0, f"{result:.2f}" if isinstance(result, float) else result)