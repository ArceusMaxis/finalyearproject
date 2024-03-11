import tkinter as tk
from tkinter import ttk, filedialog, messagebox, IntVar
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time
import os
import binascii

class FileAnalysisTool:
    def __init__(self, root):
        self.root = root
        self.root.title("File Analysis Tool")

        self.file_analysis_frame = ttk.Frame(root)
        self.file_analysis_frame.pack(pady=10)

        self.file_path_entry = ttk.Entry(self.file_analysis_frame, width=40)
        self.file_path_entry.grid(row=0, column=0, padx=10)

        self.browse_button = ttk.Button(self.file_analysis_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=1)

        self.analyze_button = ttk.Button(self.file_analysis_frame, text="Analyze File", command=self.analyze_file)
        self.analyze_button.grid(row=0, column=2, padx=10)

        self.results_text = tk.Text(root, height=10, width=80, state=tk.DISABLED)
        self.results_text.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path_entry.delete(0, tk.END)
        self.file_path_entry.insert(0, file_path)

    def analyze_file(self):
        file_path = self.file_path_entry.get()

        if not os.path.isfile(file_path):
            messagebox.showerror("Error", "Invalid file path.")
            return

        try:
            file_size = os.path.getsize(file_path)
            creation_time = os.path.getctime(file_path)
            modification_time = os.path.getmtime(file_path)

            with open(file_path, 'rb') as file:
                hex_preview = binascii.hexlify(file.read(64)).decode('utf-8')

            # Display results
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"File Analysis for: {file_path}\n\n")
            self.results_text.insert(tk.END, f"Size: {file_size} bytes\n")
            self.results_text.insert(tk.END, f"Creation Time: {creation_time}\n")
            self.results_text.insert(tk.END, f"Modification Time: {modification_time}\n\n")
            self.results_text.insert(tk.END, "Hexadecimal Preview (first 64 bytes):\n")
            self.results_text.insert(tk.END, hex_preview + "\n")
            self.results_text.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


class MLApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Elasticized AutoML System Snapshot")

        self.compilation_duration = tk.StringVar(value="2") 
        self.graph_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        self.line_styles = ['-', '--', '-.', ':']
        self.real_time_update_vars = [IntVar(value=1), IntVar(value=1)]  
        self.datasets = [None, None]

        self.graph_frame = ttk.Frame(root)
        self.graph_frame.pack(pady=10)

        self.controls_frame = ttk.Frame(root)

        self.controls_frame.pack(pady=10)
        self.figure, self.axarr = plt.subplots(2, 2, figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i in range(2):
            for j in range(2):
                self.axarr[i, j].set_title(f'ML Subsystem {i * 2 + j + 1}')
                self.axarr[i, j].set_xlabel('Time')
                self.axarr[i, j].set_ylabel('Instructions/Interactions')

        self.load_data_buttons = []
        for i in range(2):
            self.load_data_textbox = tk.Text(self.controls_frame, height=10, width=40)
            self.load_data_textbox.grid(row=0, column=i * 2)
            self.load_data_buttons.append(ttk.Button(self.controls_frame, text=f"Load Data {i + 1}", command=lambda index=i: self.load_data(index)))
            self.load_data_buttons[i].grid(row=1, column=i * 2)

            ttk.Checkbutton(self.controls_frame, text=f"Real-time Update", variable=self.real_time_update_vars[i]).grid(row=2, column=i * 2, pady=5)

        self.compile_button = ttk.Button(self.controls_frame, text="Compile Now", command=self.compile_now)
        self.compile_button.grid(row=1, column=4, pady=10)
        self.duration_label = ttk.Label(self.controls_frame, text="Compilation Duration (seconds):")
        self.duration_label.grid(row=0, column=4, pady=5)
        self.duration_entry = ttk.Entry(self.controls_frame, textvariable=self.compilation_duration, width=5)
        self.duration_entry.grid(row=1, column=5, pady=5)
        self.file_analysis_tool = FileAnalysisTool(root)
        self.logs_text = tk.Text(root, height=10, width=80, state=tk.DISABLED)
        self.logs_text.pack(pady=10)

        self.save_button = ttk.Button(root, text="Save Graph", command=self.save_graph)
        self.save_button.pack()
        self.update_graphs()

    def update_graphs(self):
        for i in range(2):
            for j in range(2):
                x = range(10)
                y = [random.randint(0, 100) for _ in x]

                self.axarr[i, j].clear()
                self.axarr[i, j].plot(x, y, color=self.graph_colors[i * 2 + j % 7], linestyle=self.line_styles[j % 4])
                self.axarr[i, j].set_title(f'Graph {i * 2 + j + 1}')
                self.axarr[i, j].set_xlabel('Time')
                self.axarr[i, j].set_ylabel('Value')

        self.canvas.draw()
        self.root.after(1000, self.update_graphs)

    def load_data(self, index):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                self.datasets[index] = pd.read_csv(file_path)
                self.load_data_textbox.delete(1.0, tk.END)
                self.load_data_textbox.insert(tk.END, self.datasets[index].to_string(index=False))
            except FileNotFoundError:
                self.load_data_textbox.delete(1.0, tk.END)
                self.load_data_textbox.insert(tk.END, "File not found!")

    def compile_now(self):
        self.compile_button.config(state=tk.DISABLED)

        loading_time = int(self.compilation_duration.get())
        self.show_loading_bar(loading_time)

    def show_loading_bar(self, loading_time):
        loading_window = tk.Toplevel(self.root)
        loading_window.title("Compiling.............................................")

        progress_bar = ttk.Progressbar(loading_window, length=200, mode='determinate', maximum=loading_time)
        progress_bar.pack(padx=10, pady=10)
        for i in range(loading_time + 1):
            progress_bar['value'] = i
            loading_window.update_idletasks()
            time.sleep(1)
        loading_window.destroy()
        self.compile_button.config(state=tk.NORMAL)
        self.logs_text.config(state=tk.NORMAL)
        self.logs_text.insert(tk.END, f"Compilation complete. Duration: {loading_time} seconds\n")
        self.logs_text.config(state=tk.DISABLED)
        self.logs_text.see(tk.END)

    def save_graph(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            try:
                self.figure.savefig(file_path)
                messagebox.showinfo("Success", "Graph saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MLApplication(root)
    root.mainloop()
