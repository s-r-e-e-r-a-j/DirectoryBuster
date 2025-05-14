# Developer: Sreeraj
# https://github.com/s-r-e-e-r-a-j

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import requests
import threading
import webbrowser
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

class DirectoryBuster:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Buster")
        
        # Set up proper shutdown handling
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Center the window on the screen with adjusted height
        window_width = 600
        window_height = 770
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Style Variables
        label_font = ("Helvetica", 12)
        header_font = ("Helvetica", 18, "bold")
        subtext_font = ("Helvetica", 10, "italic")
        
        # Header
        header_frame = tk.Frame(self.root)
        header_frame.pack(pady=10)
        tk.Label(header_frame, text="Directory Buster", font=header_font).pack()
        tk.Label(header_frame, text="This tool is made by Sreeraj", font=subtext_font).pack()

        # Frame for Target URL
        url_frame = tk.Frame(self.root)
        url_frame.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(url_frame, text="Target URL:", font=label_font).grid(row=0, column=0, sticky=tk.W)
        self.url_entry = tk.Entry(url_frame, width=50)
        self.url_entry.grid(row=0, column=1, padx=5)

        # Frame for Wordlist Selection
        wordlist_frame = tk.Frame(self.root)
        wordlist_frame.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(wordlist_frame, text="Wordlist:", font=label_font).grid(row=0, column=0, sticky=tk.W)
        self.wordlist_entry = tk.Entry(wordlist_frame, width=40)
        self.wordlist_entry.grid(row=0, column=1, padx=5)
        tk.Button(wordlist_frame, text="Browse", command=self.select_wordlist).grid(row=0, column=2, padx=5)

        # Frame for Extensions Input
        extensions_frame = tk.Frame(self.root)
        extensions_frame.pack(pady=10, fill=tk.X, padx=20)
        tk.Label(extensions_frame, text="Extensions (e.g., .js,.php,.html):", font=label_font).grid(row=0, column=0, sticky=tk.W)
        self.extensions_entry = tk.Entry(extensions_frame, width=50)
        self.extensions_entry.grid(row=0, column=1, padx=5)

        # Frame for Threads Option
        threads_frame = tk.Frame(self.root)
        threads_frame.pack(pady=5, fill=tk.X, padx=20)
        tk.Label(threads_frame, text="Threads:", font=label_font).grid(row=0, column=0, sticky=tk.W)
        self.threads_slider = tk.Scale(threads_frame, from_=1, to=50, orient=tk.HORIZONTAL)
        self.threads_slider.set(10)
        self.threads_slider.grid(row=0, column=1, sticky=tk.W, padx=5)

        # Save Results Option
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=5, fill=tk.X, padx=20)
        self.save_results = tk.BooleanVar()
        tk.Checkbutton(options_frame, text="Save found results", variable=self.save_results, font=label_font, command=self.toggle_save_path).grid(row=0, column=0, sticky=tk.W)
        
        # File Path Entry for Saving Results
        save_path_frame = tk.Frame(self.root)
        save_path_frame.pack(pady=5, fill=tk.X, padx=20)
        self.save_path_entry = tk.Entry(save_path_frame, width=40, state=tk.DISABLED)
        self.save_path_entry.grid(row=0, column=0, padx=5)
        self.save_file_button = tk.Button(save_path_frame, text="Select Save File", command=self.select_save_path, state=tk.DISABLED)
        self.save_file_button.grid(row=0, column=1, padx=5)

        # Displaying All Results
        results_label = tk.Label(self.root, text="All Results:", font=label_font)
        results_label.pack(pady=(10, 0))
        self.all_results_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=10, width=70)
        self.all_results_text.pack(pady=(0, 10), padx=20)

        # Displaying Found Results
        found_results_label = tk.Label(self.root, text="Found Results (click URL to open in browser):", font=label_font)
        found_results_label.pack(pady=(10, 0))
        self.found_results_text = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, height=5, width=70)
        self.found_results_text.pack(pady=(0, 10), padx=20)
        self.found_results_text.config(cursor="hand2")
        self.found_results_text.bind("<Button-1>", self.open_in_browser)

        # Start and Stop Buttons
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=20)

        self.start_button = tk.Button(buttons_frame, text="Start", command=self.start_busting, bg="green", fg="white", width=15, height=2)
        self.start_button.grid(row=0, column=0, padx=20)

        self.stop_button = tk.Button(buttons_frame, text="Stop", command=self.stop_busting, state=tk.DISABLED, bg="red", fg="white", width=15, height=2)
        self.stop_button.grid(row=0, column=1, padx=20)

        # Thread management variables
        self.is_busting = False
        self.thread = None
        self.executor = None

        # List of user agents
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/91.0.864.59",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/91.0.4472.124 Safari/537.36"
        ]

    def on_close(self):
        """Handle window close event"""
        self.stop_busting()
        self.root.destroy()

    def select_wordlist(self):
        filepath = filedialog.askopenfilename(title="Select Wordlist", filetypes=[("Text files", "*.txt")])
        if filepath:
            self.wordlist_entry.delete(0, tk.END)
            self.wordlist_entry.insert(0, filepath)

    def toggle_save_path(self):
        if self.save_results.get():
            self.save_path_entry.config(state=tk.NORMAL)
            self.save_file_button.config(state=tk.NORMAL)
        else:
            self.save_path_entry.config(state=tk.DISABLED)
            self.save_file_button.config(state=tk.DISABLED)

    def select_save_path(self):
        filepath = filedialog.asksaveasfilename(title="Select Save File", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filepath:
            self.save_path_entry.delete(0, tk.END)
            self.save_path_entry.insert(0, filepath)

    def start_busting(self):
        wordlist_path = self.wordlist_entry.get()
        target_url = self.url_entry.get()
        extensions = self.extensions_entry.get().strip()

        if not wordlist_path:
            messagebox.showerror("Error", "Please select a wordlist")
            return
        if not target_url:
            messagebox.showerror("Error", "Please enter a target URL")
            return

        self.start_button.config(bg="lightgreen")
        self.is_busting = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.stop_button.config(bg="red")
        
        self.thread = threading.Thread(target=self.directory_busting, args=(target_url, wordlist_path, extensions))
        self.thread.daemon = True  # Make the thread a daemon so it exits when main thread exits
        self.thread.start()

    def stop_busting(self):
        """Stop all running threads and cleanup"""
        self.stop_button.config(bg="darkred")
        self.is_busting = False
        
        # Shutdown the executor if it exists
        if self.executor:
            self.executor.shutdown(wait=False)
            self.executor = None
            
        # Reset UI
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def directory_busting(self, target_url, wordlist_path, extensions):
        found_results = []
        self.all_results_text.delete(1.0, tk.END)
        self.found_results_text.delete(1.0, tk.END)

        try:
            with open(wordlist_path, "r") as file:
                directories = [line.strip() for line in file if line.strip()]

            # Create a ThreadPoolExecutor with the selected number of threads
            with ThreadPoolExecutor(max_workers=self.threads_slider.get()) as executor:
                self.executor = executor
                futures = []

                for directory in directories:
                    if not self.is_busting:
                        break

                    # Submit tasks for testing without extension
                    url_without_extension = f"{target_url.rstrip('/')}/{directory}"
                    futures.append(executor.submit(self.test_url_worker, url_without_extension, found_results))

                    # Submit tasks for testing with each extension if provided
                    if extensions:
                        for ext in extensions.split(","):
                            ext = ext.strip()
                            if not ext:
                                continue
                            url_with_extension = f"{target_url.rstrip('/')}/{directory}{ext}"
                            futures.append(executor.submit(self.test_url_worker, url_with_extension, found_results))

                # Wait for all tasks to complete
                for future in as_completed(futures):
                    if not self.is_busting:
                        break
                    try:
                        future.result()
                    except Exception as e:
                        self.all_results_text.insert(tk.END, f"Error in worker thread: {e}\n")

        except Exception as e:
            self.all_results_text.insert(tk.END, f"Error: {e}\n")
        finally:
            # Save results if option is checked and path is provided
            save_path = self.save_path_entry.get()
            if self.save_results.get() and save_path and found_results:
                try:
                    with open(save_path, "w") as file:
                        for result in found_results:
                            file.write(result + "\n")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save results: {e}")

            self.is_busting = False
            self.start_button.config(state=tk.NORMAL, bg="green")
            self.stop_button.config(state=tk.DISABLED, bg="red")

    def test_url_worker(self, url, found_results):
        if not self.is_busting:
            return

        self.all_results_text.insert(tk.END, f"Testing: {url}\n")
        self.all_results_text.see(tk.END)

        try:
            headers = {"User-Agent": random.choice(self.user_agents)}
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                found_results.append(url)
                self.found_results_text.insert(tk.END, url + "\n")
                self.found_results_text.tag_add(url, "end-2l", "end-1c")
                self.found_results_text.tag_config(url, foreground="blue", underline=1)
        except requests.RequestException as e:
            self.all_results_text.insert(tk.END, f"Error testing {url}: {e}\n")

    def open_in_browser(self, event):
        try:
            index = self.found_results_text.index("@%s,%s" % (event.x, event.y))
            url = self.found_results_text.get(f"{index} linestart", f"{index} lineend").strip()
            if url.startswith("http"):
                webbrowser.open(url)
                self.found_results_text.tag_config(url, foreground="red")
        except Exception as e:
            print(f"Error opening URL: {e}")

# Run the application
root = tk.Tk()
app = DirectoryBuster(root)
root.mainloop()
