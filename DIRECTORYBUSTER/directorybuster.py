import tkinter as tk
from tkinter import filedialog, messagebox
import requests
from threading import Thread
import webbrowser

class DirectoryBuster:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Buster")
        self.root.geometry("650x550")
        self.root.configure(bg="#f2f2f2")
        self.root.resizable(False, False)
        self.stop_flag = False  # To control stopping the process

        # Header Frame
        header_frame = tk.Frame(root, bg="#f2f2f2")
        header_frame.pack(pady=10)

        title_label = tk.Label(header_frame, text="Directory Buster", font=("Helvetica", 20, "bold"), fg="#333")
        title_label.grid(row=0, column=0, padx=10)

        # URL Input Frame
        url_frame = tk.Frame(root, bg="#f2f2f2")
        url_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(url_frame, text="Target URL:", font=("Helvetica", 12), bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        self.url_entry = tk.Entry(url_frame, font=("Helvetica", 12), width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=5)

        # Wordlist File Selection Frame
        wordlist_frame = tk.Frame(root, bg="#f2f2f2")
        wordlist_frame.pack(pady=5, padx=20, fill="x")

        tk.Label(wordlist_frame, text="Wordlist File:", font=("Helvetica", 12), bg="#f2f2f2").grid(row=0, column=0, sticky="w")
        self.wordlist_entry = tk.Entry(wordlist_frame, font=("Helvetica", 12), width=30)
        self.wordlist_entry.grid(row=0, column=1, padx=10)
        
        browse_button = tk.Button(wordlist_frame, text="Browse", command=self.browse_file, font=("Helvetica", 10))
        browse_button.grid(row=0, column=2, padx=10)

        # Save Results Option
        save_frame = tk.Frame(root, bg="#f2f2f2")
        save_frame.pack(pady=10, padx=20, fill="x")

        self.save_var = tk.IntVar()
        self.save_checkbox = tk.Checkbutton(save_frame, text="Save found results to file", variable=self.save_var, command=self.toggle_save_option, font=("Helvetica", 12), bg="#f2f2f2")
        self.save_checkbox.grid(row=0, column=0, sticky="w")
        
        self.save_path_entry = tk.Entry(save_frame, font=("Helvetica", 12), width=30, state="disabled")
        self.save_path_entry.grid(row=0, column=1, padx=10)
        self.save_browse_button = tk.Button(save_frame, text="Select File", command=self.select_save_file, font=("Helvetica", 10), state="disabled")
        self.save_browse_button.grid(row=0, column=2, padx=10)

        # Results Text Box with Scrollbar
        results_frame = tk.Frame(root, bg="#f2f2f2")
        results_frame.pack(pady=10, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(results_frame)
        scrollbar.pack(side="right", fill="y")

        self.results_text = tk.Text(results_frame, height=10, width=70, state="disabled", font=("Helvetica", 10), yscrollcommand=scrollbar.set)
        self.results_text.pack(padx=10, pady=10, fill="both", expand=True)
        scrollbar.config(command=self.results_text.yview)

        # Configure tag for URLs
        self.results_text.tag_configure("url", foreground="blue", underline=True)
        self.results_text.tag_bind("url", "<Enter>", self.on_enter_url)
        self.results_text.tag_bind("url", "<Leave>", self.on_leave_url)
        self.results_text.tag_bind("url", "<Button-1>", self.open_url)  # Make URLs clickable

        # Control Buttons (Start and Stop)
        button_frame = tk.Frame(root, bg="#f2f2f2")
        button_frame.pack(pady=15)

        start_button = tk.Button(button_frame, text="Start Directory Buster", font=("Helvetica", 14, "bold"), command=self.start_busting, bg="#4CAF50", fg="white")
        start_button.grid(row=0, column=0, padx=10)

        stop_button = tk.Button(button_frame, text="Stop", font=("Helvetica", 14, "bold"), command=self.stop_busting, bg="#FF5733", fg="white")
        stop_button.grid(row=0, column=1, padx=10)

        # Footer with Copyright Notice
        footer_frame = tk.Frame(root, bg="#f2f2f2")
        footer_frame.pack(side="bottom", pady=10)

        copyright_label = tk.Label(footer_frame, text="This tool is made by Sreeraj", font=("Helvetica", 10, "italic"), bg="#f2f2f2")
        copyright_label.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select Wordlist File", filetypes=[("Text Files", "*.txt")])
        self.wordlist_entry.delete(0, tk.END)
        self.wordlist_entry.insert(0, file_path)

    def select_save_file(self):
        file_path = filedialog.asksaveasfilename(title="Select Save File", defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, file_path)
    
    def toggle_save_option(self):
        if self.save_var.get() == 1:
            self.save_path_entry.config(state="normal")
            self.save_browse_button.config(state="normal")
        else:
            self.save_path_entry.config(state="disabled")
            self.save_browse_button.config(state="disabled")

    def start_busting(self):
        url = self.url_entry.get().strip()
        wordlist_path = self.wordlist_entry.get().strip()
        
        if not url or not wordlist_path:
            messagebox.showwarning("Warning", "Please enter a URL and select a wordlist file.")
            return
        
        if self.save_var.get() == 1 and not self.save_path_entry.get().strip():
            messagebox.showwarning("Warning", "Please select a file to save results.")
            return
        
        self.stop_flag = False  # Reset stop flag

        # Start directory busting in a separate thread
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "Starting directory buster...\n")
        self.results_text.config(state="disabled")
        
        thread = Thread(target=self.bust_directories, args=(url, wordlist_path))
        thread.start()

    def stop_busting(self):
        self.stop_flag = True  # Set flag to stop the busting process

    def bust_directories(self, url, wordlist_path):
        save_to_file = self.save_var.get() == 1
        save_file_path = self.save_path_entry.get().strip() if save_to_file else None

        try:
            if save_to_file:
                with open(save_file_path, "w") as file:
                    file.write("Found directories:\n")
            
            with open(wordlist_path, "r") as file:
                directories = [line.strip() for line in file]
                
            for directory in directories:
                if self.stop_flag:  # Check if stop button has been clicked
                    break

                full_url = f"{url}/{directory}"
                response = requests.get(full_url)
                
                self.results_text.config(state="normal")
                if response.status_code == 200:
                    result_text = f"[FOUND] {full_url}\n"
                    self.results_text.insert(tk.END, result_text, "url")
                    if save_to_file:
                        with open(save_file_path, "a") as file:
                            file.write(result_text)
                else:
                    self.results_text.insert(tk.END, f"[NOT FOUND] {full_url}\n")
                
                self.results_text.config(state="disabled")
                self.results_text.see(tk.END)
        
        except Exception as e:
            self.results_text.config(state="normal")
            self.results_text.insert(tk.END, f"Error: {str(e)}\n")
            self.results_text.config(state="disabled")

    def on_enter_url(self, event):
        self.results_text.config(cursor="hand2")  # Show pointer cursor on hover

    def on_leave_url(self, event):
        self.results_text.config(cursor="")  # Restore default cursor

    def open_url(self, event):
        # Open the clicked URL in the browser
        index = self.results_text.index("@%d,%d" % (event.x, event.y))
        line_text = self.results_text.get(f"{index} linestart", f"{index} lineend").strip()
        if line_text.startswith("[FOUND]"):
            url = line_text.split("[FOUND] ")[1]
            webbrowser.open(url)

# Run the application
# Run the application
root = tk.Tk()
app = DirectoryBuster(root)
root.mainloop()