# Financial-Calculator

Welcome to the Financial Calculator repository! This project is a comprehensive financial tool designed to help you calculate investment worth through both simple and compound interest, as well as facilitate bond calculations for housing investments. Whether you're a finance enthusiast, a student, or someone looking to make informed investment decisions, this calculator provides a user-friendly interface to assist you in understanding the potential returns on your investments.

## Features

- **Simple Interest Calculation:** Estimate your investment's worth based on simple interest rates with ease.

- **Compound Interest Calculation:** Dive deeper into the numbers by exploring the impact of compound interest on your investments over time.

- **Bond Calculator:** For those interested in real estate investments, the bond calculator can help you assess mortgage payments and plan your house financing.

## Getting Started

To explore the inner workings of the financial calculator, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/VuyolwethuM6/financial-calculator.git
   ```

2. Open the project in your preferred code editor.

3. Navigate to the main code file, typically named `financial_calculator.py` or a similar convention.

4. Take a guided tour through the code comments and documentation to understand the logic behind each calculation.

## Usage

The financial calculator is designed to be user-friendly, but understanding the code will empower you to customize and extend its functionalities to suit your specific needs.

1. **Importing Tkinter:**
   ```python
   import tkinter as tk
   from tkinter import ttk
   ```
   - Tkinter is the standard GUI (Graphical User Interface) package for Python.
   - `ttk` provides themed Tkinter widgets, which have a more modern and native look.

2. **Creating the Main Window:**
   ```python
   root = tk.Tk()
   root.title("Financial Calculator")
   ```
   - `Tk()` creates the main window object.
   - `title()` sets the title of the window.

3. **Creating Tabs with `ttk.Notebook`:**
   ```python
   notebook = ttk.Notebook(root)
   ```
   - `ttk.Notebook` is used to create a tabbed interface.

4. **Creating Frames for Each Tab:**
   ```python
   investment_frame = ttk.Frame(notebook)
   bond_frame = ttk.Frame(notebook)
   ```
   - Frames are containers for organizing and grouping widgets.

5. **Adding Tabs to the Notebook:**
   ```python
   notebook.add(investment_frame, text="Investment")
   notebook.add(bond_frame, text="Bond")
   notebook.pack(expand=True, fill="both")
   ```
   - `add()` method adds frames to the notebook with specified tab names.
   - `pack()` method organizes the notebook within the main window.

6. **Creating Labels, Entries, Combobox, and Buttons:**
   - Labels (`ttk.Label`): Display static text.
   - Entries (`ttk.Entry`): Allow user input.
   - Combobox (`ttk.Combobox`): A drop-down list for selecting options.
   - Button (`ttk.Button`): Trigger actions.
   ```python
   label_principal = ttk.Label(investment_frame, text="Principal:")
   entry_principal = ttk.Entry(investment_frame)
   combo_interest_type = ttk.Combobox(investment_frame, values=["Simple", "Compound"])
   calculate_button = ttk.Button(investment_frame, text="Calculate", command=on_calculate)
   ```

7. **Grid Layout for Widgets:**
   - `grid()` method organizes widgets in rows and columns.
   ```python
   label_principal.grid(row=0, column=0, padx=5, pady=5, sticky="e")
   entry_principal.grid(row=0, column=1, padx=5, pady=5)
   ```

8. **Handling Events with Functions:**
   ```python
   def on_calculate():
       option = notebook.index(notebook.select())
       if option == 0:
           # Handle Investment calculation
       elif option == 1:
           # Handle Bond calculation
   ```
   - Functions are defined to handle events, such as button clicks.

9. **Starting the Tkinter Event Loop:**
   ```python
   root.mainloop()
   ```
   - `mainloop()` starts the Tkinter event loop, allowing the GUI to respond to user actions.

These key points cover the basic structure of this Tkinter GUI application. This code provided demonstrates a simple finance calculator with tabs for investment and bond calculations.
