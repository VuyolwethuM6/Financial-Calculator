import tkinter as tk
from tkinter import ttk
import math


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def is_valid_positive_number(value):
    return is_valid_number(value) and float(value) >= 0


def is_valid_rate(value):
    return is_valid_positive_number(value) and float(value) <= 100


def calculate_investment(principal, rate, time, interest_type):
    rate /= 100
    if interest_type == "Simple":
        amount = principal * (1 + rate * time)
    elif interest_type == "Compound":
        amount = principal * math.pow(1 + rate, time)
    else:
        amount = 0
    return amount


def calculate_bond(house_value, rate, months):
    rate = (rate / 12) / 100  
    monthly_payment = (rate * house_value) / (1 - math.pow(1 + rate, -months))
    return monthly_payment


def clear_fields():
    # Clear input fields
    entry_principal.delete(0, tk.END)
    entry_rate.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_house_value.delete(0, tk.END)
    entry_rate_bond.delete(0, tk.END)
    entry_months.delete(0, tk.END)

    # Clear result labels
    result_label.config(text="Result:")
    result_label_bond.config(text="Result:")


def on_calculate():
    option = notebook.index(notebook.select())
      
    if option == 0:  # Investment tab
        principal = entry_principal.get()
        rate = entry_rate.get()
        time = entry_time.get()
        interest_type = combo_interest_type.get()

        if not is_valid_positive_number(principal) or not is_valid_rate(rate) or not is_valid_positive_number(time):
            result_label.config(text="Invalid input. Please enter valid numbers.")
            return

        principal = float(principal)
        rate = float(rate)
        time = float(time)

        result = calculate_investment(principal, rate, time, interest_type)
        result_label.config(text=f"Your investment will be worth: R{result:.2f}")

    elif option == 1:  # Bond tab
        house_value = entry_house_value.get()
        rate = entry_rate_bond.get()
        months = entry_months.get()

        if not is_valid_positive_number(house_value) or not is_valid_rate(rate) or not is_valid_positive_number(months):
            result_label_bond.config(text="Invalid input. Please enter valid numbers.")
            return

        house_value = float(house_value)
        rate = float(rate)
        months = float(months)

        result = calculate_bond(house_value, rate, months)
        result_label_bond.config(text=f"Your monthly bond repayment will be: R{result:.2f}")


# Create the main window
root = tk.Tk()
root.title("Financial Calculator")
root.geometry("400x250")  
root.resizable(False, False)  

# Set the font size for the entire application
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12))
style.configure("TEntry", font=("Arial", 12))
style.configure("TCombobox", font=("Arial", 29))

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)

# Create frames for each tab
investment_frame = ttk.Frame(notebook)
bond_frame = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(investment_frame, text="Investment")
notebook.add(bond_frame, text="Bond")
notebook.pack(expand=True, fill="both")

# Investment tab
label_principal = ttk.Label(investment_frame, text="Principal:")
label_rate = ttk.Label(investment_frame, text="Interest Rate (%):")
label_time = ttk.Label(investment_frame, text="Time (years):")
label_interest_type = ttk.Label(investment_frame, text="Interest Type:")

entry_principal = ttk.Entry(investment_frame)
entry_rate = ttk.Entry(investment_frame)
entry_time = ttk.Entry(investment_frame)

combo_interest_type = ttk.Combobox(investment_frame, values=["Simple", "Compound",])
combo_interest_type.set("Simple")

calculate_button = ttk.Button(investment_frame, text="Calculate", command= on_calculate)
result_label = ttk.Label(investment_frame, text="Result:") 

clear_button = ttk.Button(investment_frame, text="Clear", command=clear_fields)
clear_button.grid(row=4, column=0, pady=10)

label_principal.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_rate.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_time.grid(row=2, column=0, padx=5, pady=5, sticky="e")
label_interest_type.grid(row=3, column=0, padx=5, pady=5, sticky="e")

entry_principal.grid(row=0, column=1, padx=5, pady=5)
entry_rate.grid(row=1, column=1, padx=5, pady=5)
entry_time.grid(row=2, column=1, padx=5, pady=5)
combo_interest_type.grid(row=3, column=1, padx=5, pady=5)

calculate_button.grid(row=4, column=1, pady=10)
result_label.grid(row=5, column=0, columnspan=2, pady=5)

# Bond tab
label_house_value = ttk.Label(bond_frame, text="House Value:")
label_rate_bond = ttk.Label(bond_frame, text="Annual Interest Rate (%):")
label_months = ttk.Label(bond_frame, text="Repayment Period (months):")

entry_house_value = ttk.Entry(bond_frame)
entry_rate_bond = ttk.Entry(bond_frame)
entry_months = ttk.Entry(bond_frame)

label_house_value.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_rate_bond.grid(row=1, column=0, padx=5, pady=5, sticky="e")
label_months.grid(row=2, column=0, padx=5, pady=5, sticky="e")

entry_house_value.grid(row=0, column=1, padx=5, pady=5)
entry_rate_bond.grid(row=1, column=1, padx=5, pady=5)
entry_months.grid(row=2, column=1, padx=5, pady=5)

calculate_button_bond = ttk.Button(bond_frame, text="Calculate", command=on_calculate)
result_label_bond = ttk.Label(bond_frame, text="Result:")

clear_button_bond = ttk.Button(bond_frame, text="Clear", command=clear_fields)
clear_button_bond.grid(row=3, column=0, pady=10)

calculate_button_bond.grid(row=3, column=1, pady=10)
result_label_bond.grid(row=4, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()
