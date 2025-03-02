## DirectoryBuster

DirectoryBuster is a GUI-based directory brute-forcing tool that helps discover hidden directories and files on web servers. It allows penetration testers and security researchers to identify accessible resources by testing a given target URL against a wordlist of potential directory and file names.

---

## Features  

- **Easy-to-Use Interface**:  Simple and user-friendly GUI.  
- **Custom Wordlist**:
  Choose your own wordlist for scanning.  
- **Supports File Extensions**: Check for files with extensions like `.php, .html, .js`.  
-  **Save Results**: Option to save founded results to a file.  
-  **Clickable Links**: Open found URLs directly in a browser.  
-  **Live Updates**:See the scanning progress in real-time.  
-  **Fast Scanning**:Uses multi-threading for better performance.  
-  **Start & Stop Anytime**: Control the scan with start and stop buttons.  
-  **Error Handling**:Handles network issues without crashing.
  
---

## Requirements
- Python 3.x
- requests (for sending HTTP requests)
- tkinter (for the GUI)
- threading
- webbrowser
  
## Installation


1. **Clone the repository to your local machine**
```bash
git clone https://github.com/s-r-e-e-r-a-j/DirectoryBuster.git
```
2. **Navigate to the DirectoryBuster directory**
```bash
cd DirectoryBuster
```

3. **Install the required dependencies:**

```bash
pip3 install -r requirements.txt
```

4. **Navigate to the DIRECTORYBUSTER directory**
  ```bash
cd DIRECTORYBUSTER
```
5. **Install the tool**
  ```bash
sudo python3 install.py
```
Then enter `y` for install

6. **Run the Tool:**
```bash
directorybuster
```

 ## How to Use

### **Set the Target URL**
Type the website URL you want to scan (e.g., `http://example.com`) in the "Target URL" box.

### **Select a Wordlist**
Click the "Browse" button to choose a wordlist file. The wordlist should be a `.txt` file with a list of directory names to test (e.g., `common-directories.txt`).

### **Add Extensions (Optional)**
If you want to test specific file types, type the extensions separated by commas (e.g., `.js,.php,.html`). The tool will check:
- Each word **without extensions** (e.g., `http://example.com/admin`).
- Each word **with each extension** (e.g., `http://example.com/admin.js`, `http://example.com/admin.php`).

### **Save Results (Optional)**
If you want to save the results:
1. Check the "Save found results" box.
2. Click "Select Save File" to choose where to save the results.

### **Start Scanning**
Click the "Start" button to begin scanning. The tool will:
- Test each word in the wordlist **without extensions**.
- Test each word in the wordlist **with each extension** (if added).
- Show the results in real-time.

### **Found Results**
Founded results will appear in the "Found Results" section. Click on any URL to open it in your browser. Found URLs are shown in **blue** and turn **red** after clicking.

### **Stop Scanning**
Click the "Stop" button anytime to stop the scanning process.

## Example Usage

1. **Enter the Target URL**:  
   Type the website URL you want to scan, for example: `http://example.com`.

2. **Choose a Wordlist File**:  
   Click the "Browse" button and select a wordlist file (e.g., `common-directories.txt`).

3. **Add Extensions (Optional)**:  
   If you want to test specific file types, type the extensions separated by commas (e.g., `.js,.php,.html`).

4. **Save Results (Optional)**:  
   Check the "Save found results" box and click "Select Save File" to choose where to save the results.

5. **Start Scanning**:  
   Click the "Start" button. The tool will:
   - Test each word in the wordlist **without extensions**.
   - Test each word in the wordlist **with each extension** (if added).
   - Show the results in real-time.

6. **View Found Results**:  
   Founded results will appear in the "Found Results" section. Click on any URL to open it in your browser.

7. **Stop Scanning**:  
   Click the "Stop" button anytime to stop the scanning process.
   
## Picture

![VirtualBox_KALILINUX1_08_11_2024_22_00_28](https://github.com/user-attachments/assets/7f496402-1321-478b-a960-9b17f91bd82a)



## uninstallation

```bash
cd DirectoryBuster
```
```bash
cd DIRECTORYBUSTER
```
```bash
sudo python3 install.py
```
Then Enter `n` for uninstall


## Troubleshooting

- **Error: No wordlist selected**
Ensure that you have selected a valid wordlist file by clicking the "Browse" button.

- **Error: No target URL entered**
Enter the target URL before clicking "Start".

- **Error: Cannot save results**
Ensure that you have selected a valid file path to save the results.

## License
This tool is licensed under the MIT License. See LICENSE for more details.


