## DirectoryBuster
DirectoryBuster is a GUI-based directory brute-forcing tool designed to help penetration testers and security researchers discover hidden directories and files on web servers. By testing a target URL against a wordlist of potential directory and file names, it identifies accessible resources that may pose security risks.

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

1. **Enter Target URL**  
   - Example: `https://example.com`

2. **Select a Wordlist**  
   - Click the **"Browse"** button and choose a `.txt` file containing directory names

3. **(Optional) Add File Extensions**  
   - Example: `.php,.html,.js` (comma-separated).
4. **(optional) choose threads by sliding**
   - default is 10
6. **(Optional) Enable Save Results**  
   - Check the **"Save found results"** box and select a file to save the output.

7. **Start Scanning**  
   - Click the **"Start"** button to begin the scan.  
   - The Tool will  Test each word in the wordlist **without extensions**.
   - The Tool will Test each word in the wordlist **with each extension** (if added).
   - Show the results in real-time.

8. **Open Found Links**  
   - Click on any found URL to open it in your default browser.

9. **Stop Scanning**  
   - Click the **"Stop"** button to cancel the scan at any time.
     

  
## Example Usage

1. **Enter the Target URL**:  
   Type the website URL you want to scan, for example: `https://example.com`.

2. **Choose a Wordlist File**:  
   Click the "Browse" button and select a wordlist file (e.g., `common-directories.txt`).

3. **Add Extensions (Optional)**:  
   If you want to test specific file types, type the extensions separated by commas (e.g., `.js,.php,.html`).
4. **choose Threads(optional)**:
   choose threads by sliding the slide bar default is 10 max threads is 50
6. **Save Results (Optional)**:  
   Check the "Save found results" box and click "Select Save File" to choose where to save the results.

7. **Start Scanning**:  
   Click the "Start" button. The tool will:
   - Test each word in the wordlist **without extensions**.
   - Test each word in the wordlist **with each extension** (if added).
   - Show the results in real-time.

8. **View Found Results**:  
   Founded results will appear in the "Found Results" section. Click on any URL to open it in your browser.

9. **Stop Scanning**:  
   Click the "Stop" button anytime to stop the scanning process.
   
## Picture


![VirtualBox_klinux17_15_05_2025_01_20_26](https://github.com/user-attachments/assets/02ce28a4-16a1-4f35-8be2-49fe2d39a07e)




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


