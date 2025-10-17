
#This is a replica of the 1D Resist.py but with a Tkinter GUI for data input and export
# Importing the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, filedialog, simpledialog, messagebox
import os
# Creating a class for data collection, export and filtering
class Geo_ResistSurvey:
    def __init__(self):
        self.data = pd.DataFrame(columns=["AB/2", "MN/2", "Resistance", "Current"])
        self.filtered_data = None
        self.fig, self.ax = plt.subplots()
    #Data collection sequence
    def collect_data(self):
        while True:
            ab2 = simpledialog.askfloat("Input", "Enter AB/2:")
            mn2 = simpledialog.askfloat("Input", "Enter MN/2:")
            resistance = simpledialog.askfloat("Input", "Enter Resistance:")
            current = simpledialog.askfloat("Input", "Enter Current:")
            self.data = pd.concat([self.data, pd.DataFrame([[ab2, mn2, resistance, current]], columns=self.data.columns)], ignore_index=True)
            cont = messagebox.askyesno("Continue?", "You wan add more data?")
            if not cont:
                break
    # Data export to file
    def export_to_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.data.to_csv(file_path, index=False)
            messagebox.showinfo("Export", "Data exported successfully!")
    '''Data filtering and plot
    This makes use of a simple filter, by entering the threshold value for the ground resistance data
    It is a plot of the Resistance obtained versus the Electrode Distance (AB/2)
    '''
    def filter_noise(self):
        threshold = simpledialog.askfloat("Filter", "Enter noise threshold for resistance:")
        self.filtered_data = self.data[self.data["Resistance"] > threshold]
        messagebox.showinfo("Filter", "Noise filtering applied!")

    def plot_graph(self):
        if self.filtered_data is None:
            data_to_plot = self.data
        else:
            data_to_plot = self.filtered_data

        self.ax.clear()
        self.ax.set_xscale("log")
        self.ax.set_yscale("log")
        self.ax.scatter(data_to_plot["AB/2"], data_to_plot["Resistance"], label="Observed Data")
        self.ax.set_xlabel("AB/2(metre)")
        self.ax.set_ylabel("App. Resistivity(Ohm-m)")
        self.ax.legend()
        plt.draw()

    def model_data(self):
        depths = []
        resistivities = []
        while True:
            depth = simpledialog.askfloat("Model", "Enter depth:")
            resistivity = simpledialog.askfloat("Model", "Enter resistivity:")
            depths.append(depth)
            resistivities.append(resistivity)
            cont = messagebox.askyesno("Continue?", "Do you want to add more layers?")
            if not cont:
                break

        self.ax.step(depths, resistivities, where='post', label="Modeled Data", color="red")
        self.ax.legend()
        plt.draw()

    def export_graph(self):
        fil0e_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.fig.savefig(file_path)
            messagebox.showinfo("Dey wii me, baba", "Graph exported successfully!")

    def run(self):
        root = Tk()
        root.withdraw()  # This is meant to hide the root window
        while True:
            choice = simpledialog.askstring("Menu", "Choose an option:\n1. Collect Data\n2. Export to CSV\n3. Filter Noise\n4. Plot Graph\n5. Model Data\n6. Export Graph\n7. Exit")
            if choice == "1":
                self.collect_data()
            elif choice == "2":
                self.export_to_csv()
            elif choice == "3":
                self.filter_noise()
            elif choice == "4":
                self.plot_graph()
                plt.show()
            elif choice == "5":
                self.model_data()
            elif choice == "6":
                self.export_graph()
            elif choice == "7":
                break
            else:
                messagebox.showerror("Error", "You gas to start all over baba, you sef don try"
if __name__ == "__main__":
    app = Geo_ResistSurvey()
    app.run()