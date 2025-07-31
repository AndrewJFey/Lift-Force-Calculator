# logic.py

import math

class LiftCalculatorLogic:

    # Defines the equations for each variable being solved for
    @staticmethod
    def get_equation_text(var):
        equations = {
            "0": "LF = 1/2 * A * ρ * CL * V²",
            "1": "A = 2 * LF / (ρ * CL * V²)",
            "2": "ρ = 2 * LF / (A * CL * V²)",
            "3": "CL = 2 * LF / (A * ρ * V²)",
            "4": "V = sqrt(2 * LF / (A * ρ * CL))",
        }
        # Returns value of active variable
        return equations.get(var, "")

    # Calculation logic
    @staticmethod
    def calculate(var, input_fields):
        try:
            # Sorts all inputs and converts them to float
            values = [float(field.get()) for field in input_fields]

            equation_for_output = [
                lambda vals: 0.5 * vals[0] * vals[1] * vals[2] * vals[3] ** 2,
                lambda vals: (2 * vals[0]) / (vals[1] * vals[2] * vals[3] ** 2),
                lambda vals: (2 * vals[0]) / (vals[1] * vals[2] * vals[3] ** 2),
                lambda vals: (2 * vals[0]) / (vals[1] * vals[2] * vals[3] ** 2),
                lambda vals: math.sqrt((2 * vals[0]) / (vals[1] * vals[2] * vals[3]))
            ]

            return equation_for_output[int(var)](values)
        

        # Error handling
        except ValueError:
            return "Invalid"
        except ZeroDivisionError:
            return "Divide by zero"