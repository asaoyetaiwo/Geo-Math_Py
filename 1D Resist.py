#114 141 163 164 040 160 141 164 143 150 040 157 156 040 047 155 141 162 143 150 040 062 060 062 065 047
# The project is still under development. Please report any issues.
# A 1D Geo-resistivity processing and plotting sequence

# A simple HK-filter is used in filtering the noises arising from acquisition process

# Importing the required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import medfilt
import os

# Defining a class to enclose the sequence

class ResistivityModelApp:
    @staticmethod
    def input_data():
        print("Choose data input method:")
        print("1. Manually enter data")
        print("2. Load from .csv or .dat file")
        choice = input("Enter choice (1/2): ").strip()

        if choice == '1':
            data = []
            print("Enter resistivity data (type 'done' to finish):")
            while True:
                value = input("Enter value: ")
                if value.lower() == 'done':
                    break
                try:
                    data.append(float(value))
                except ValueError:
                    print("Invalid input, please enter a number")
            data = np.array(data)
        elif choice == '2':
            file_path = input("Enter file path (.csv or .dat): ").strip()
            try:
                if file_path.endswith('.csv'):
                    data = pd.read_csv(file_path).values.flatten()
                elif file_path.endswith('.dat'):
                    data = np.loadtxt(file_path)
                else:
                    print("Unsupported file format. Try rerun")
                    return None
            except Exception as e:
                print(f"Error reading file: {e}")
                return None
        else:
            print("Invalid choice")
            return None

        try:
            np.savetxt("input_data.txt", data)
            print("Data saved to input_data.txt")
        except Exception:
            pass

        return data

    @staticmethod
    def hk_filter(data, kernel_size=3):
        if data is None:
            return None
        # medfilt will expect an odd kernel; ensure it is odd
        kernel_size = int(kernel_size)
        if kernel_size % 2 == 0:
            kernel_size += 1
        filtered_data = medfilt(data, kernel_size=kernel_size)
        try:
            np.savetxt("filtered_data.txt", filtered_data)
            print("Filtered data saved to filtered_data.txt")
        except Exception:
            pass
        return filtered_data

    @staticmethod
    def model_data():
        print("Modeling data:")
        depth_or_height = input("Enter 'depth' or 'height': ").lower().strip()
        if depth_or_height not in ['depth', 'height']:
            print("Invalid input")
            return None, None

        try:
            layers = int(input("Enter number of layers: "))
        except ValueError:
            print("Invalid number of layers")
            return None, None

        resistivities = []
        for i in range(layers):
            while True:
                try:
                    resistivity = float(input(f"Enter resistivity for layer {i+1}: "))
                    resistivities.append(resistivity)
                    break
                except ValueError:
                    print("Invalid input, please enter a number")
        return depth_or_height, resistivities

    @staticmethod
    def plot_data(original_data, filtered_data, depth_or_height, resistivities):
        plt.figure(figsize=(10, 6))
        if original_data is not None:
            plt.plot(original_data, label="Original Data", color="blue")
        if filtered_data is not None:
            plt.plot(filtered_data, label="Filtered Data", color="green")

        if depth_or_height and resistivities:
            base_len = len(filtered_data) if filtered_data is not None else (len(original_data) if original_data is not None else 1)
            model_x = np.linspace(0, max(base_len - 1, 0), len(resistivities))
            plt.plot(model_x, resistivities, label="Modeled Data", color="red")

        plt.xlabel("Index")
        plt.ylabel("Resistivity")
        plt.title("Modeled Data")
        plt.legend()
        plt.grid()
        plt.savefig("resistivity_plot.png")
        print("Plot saved as resistivity_plot.png")
        plt.show()


def main():
    data = ResistivityModelApp.input_data()
    if data is None:
        return

    filtered_data = ResistivityModelApp.hk_filter(data)
    depth_or_height, resistivities = ResistivityModelApp.model_data()
    if depth_or_height is None:
        return

    ResistivityModelApp.plot_data(data, filtered_data, depth_or_height, resistivities)


if __name__ == "__main__":
    main()