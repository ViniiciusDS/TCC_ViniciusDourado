import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
import numpy as np
import pandas as pd
from scipy.stats import ttest_rel
from forca_bruta import forcabruta
from alggenetico import alggenetico
from simulatedAnnealing import simulated_annealing


class TCCApp:
    def __init__(self, master):
        self.master = master
        self.master.title("TCC Program")

        # Variables for GUI elements
        self.selected_matrix = tk.StringVar()
        self.num_cities = tk.StringVar()
        self.run_forca_bruta = tk.IntVar()
        self.run_alg_genetico = tk.IntVar()
        self.run_simulated_annealing = tk.IntVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Frame for input options
        frame_inputs = ttk.Frame(self.master)
        frame_inputs.pack(pady=10)

        # Label and Dropdown for selecting matrix
        label_matrix = ttk.Label(frame_inputs, text="Select Matrix:")
        label_matrix.grid(row=0, column=0, padx=5, pady=5)
        dropdown_matrix = ttk.Combobox(
            frame_inputs, textvariable=self.selected_matrix)
        # Add your matrix names here
        dropdown_matrix["values"] = ("Matrix1", "Matrix2")
        dropdown_matrix.grid(row=0, column=1, padx=5, pady=5)
        dropdown_matrix.set("Matrix1")

        # Label and Entry for number of cities
        label_num_cities = ttk.Label(frame_inputs, text="Number of Cities:")
        label_num_cities.grid(row=1, column=0, padx=5, pady=5)
        entry_num_cities = ttk.Entry(
            frame_inputs, textvariable=self.num_cities)
        entry_num_cities.grid(row=1, column=1, padx=5, pady=5)

        # Checkbuttons for selecting methods to run
        checkbutton_forca_bruta = ttk.Checkbutton(
            frame_inputs, text="Run Força Bruta", variable=self.run_forca_bruta)
        checkbutton_forca_bruta.grid(row=2, column=0, padx=5, pady=5)
        checkbutton_alg_genetico = ttk.Checkbutton(
            frame_inputs, text="Run Algoritmo Genético", variable=self.run_alg_genetico)
        checkbutton_alg_genetico.grid(row=2, column=1, padx=5, pady=5)
        checkbutton_simulated_annealing = ttk.Checkbutton(
            frame_inputs, text="Run Simulated Annealing", variable=self.run_simulated_annealing)
        checkbutton_simulated_annealing.grid(row=2, column=2, padx=5, pady=5)

        # Button to start the calculations
        button_run = ttk.Button(frame_inputs, text="Run",
                                command=self.run_calculations)
        button_run.grid(row=3, column=0, columnspan=3, pady=10)

        # Frame for displaying results
        frame_results = ttk.Frame(self.master)
        frame_results.pack(pady=10)

        # Create a Figure to display matplotlib plot
        self.figure = Figure(figsize=(6, 4), tight_layout=True)
        self.subplot = self.figure.add_subplot(111)
        self.subplot.set_xlabel("Number of Cities")
        self.subplot.set_ylabel("Execution Time")

        # Create a canvas to embed the plot in tkinter
        self.canvas = FigureCanvasTkAgg(self.figure, master=frame_results)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def run_calculations(self):
        # Get input values
        selected_matrix = self.selected_matrix.get()
        num_cities = int(self.num_cities.get())
        run_forca_bruta = self.run_forca_bruta.get()
        run_alg_genetico = self.run_alg_genetico.get()
        run_simulated_annealing = self.run_simulated_annealing.get()

        # TODO: Load matrices and execute the selected methods
        # ...

        # For demonstration purposes, let's assume you have results as below
        num_cities_vec = np.arange(4, 12)
        # Replace this with your actual results
        tab_resultados_tempo = np.random.rand(8, 3)

        # Update the plot
        self.update_plot(num_cities_vec, tab_resultados_tempo)

    def update_plot(self, num_cities_vec, tab_resultados_tempo):
        self.subplot.clear()

        # Plotting execution time for each method
        if self.run_forca_bruta.get():
            self.subplot.plot(
                num_cities_vec, tab_resultados_tempo[:, 0], '-o', label='Força Bruta', linewidth=5)
        if self.run_alg_genetico.get():
            self.subplot.plot(
                num_cities_vec, tab_resultados_tempo[:, 1], '-o', label='Algoritmo Genético', linewidth=5)
        if self.run_simulated_annealing.get():
            self.subplot.plot(
                num_cities_vec, tab_resultados_tempo[:, 2], '-o', label='Simulated Annealing', linewidth=5)

        # Update the legend, labels, etc.
        self.subplot.set_xlabel("Number of Cities")
        self.subplot.set_ylabel("Execution Time")
        self.subplot.legend(loc='upper left')
        self.subplot.grid(True)

        # Draw the updated plot on the canvas
        self.canvas.draw()


def main():
    root = tk.Tk()
    app = TCCApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
