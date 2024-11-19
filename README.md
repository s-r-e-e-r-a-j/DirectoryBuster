## Directory Buster
Directory Buster is a GUI based Tool Made with python.this is a simple yet powerful tool for discovering hidden directories and files on a target web server using a wordlist-based approach. It's designed to assist security professionals and enthusiasts with directory brute-forcing to identify potentially vulnerable or hidden resources on a web server.

## Tool Graphical User Interface

![VirtualBox_KALILINUX1_08_11_2024_22_00_28](https://github.com/user-attachments/assets/c7e808b1-ea27-4831-8497-d95e490be0a6)




## Features:
- Enter the target URL to start brute-forcing.
- Choose a wordlist for directory names.
- Option to save found results to a text file.
- Scrolled text boxes to display both found and non-found results.
- Clickable URLs in the "Found Results" section to open them directly in a web browser.
- Option to stop the brute-force process anytime.
## Installation

1 .Install the required dependencies:


`In Kali Linux all the requirements are pre-installed. requirements means packages required for this tool to work.so don't need to install requirements on kali linux`
```bash
   pip3 install -r requirements.txt
```
2. 1.Clone the repository to your local machine
```bash
git clone https://github.com/s-r-e-e-r-a-j/DirectoryBuster.git
```
```bash
   cd DirectoryBuster
```
```bash
   cd DIRECTORYBUSTER
```
3. Run the Tool:
```bash
  python3 directorybuster.py
```
## Requirements
- Python 3.x
- requests (for sending HTTP requests)
- tkinter (for the GUI)
- threading
- webbrowser

  
  `All the requirements are pre-installed in kali linux so don't need to install this things in kali linux`


 ## How to Use
 
- **Set the Target URL**:

Enter the target URL (e.g., http://example.com) in the "Target URL" input field.

- **Select a Wordlist**:

Click the "Browse" button to select a wordlist file. The wordlist file should be a .txt file containing a list of directories to test.
`if you are using kalilinux.All the wordlists for this tool are available on kali linux at this path`
`/usr/share/wordlists/dirbuster`

- **Save Results (Optional)**:

If you want to save the found results, check the "Save found results" checkbox and specify the file location using the "Select Save File" button.

- **Start Directory Busting**:

Click the "Start" button to begin the directory busting process. The tool will start testing directories from the wordlist against the target URL.

- **Found Results**:

The "Found Results" section will display any discovered directories with a clickable URL. Click on a URL to open it directly in your default web browser.

- **Stop Directory Busting**:

Click the "Stop" button anytime to halt the directory busting process.

## Example Usage:
- Enter the target URL http://example.com.
- Choose a wordlist file (e.g., common-directories.txt).
- Optionally select a save path for the results.
- Click "Start" and watch the results populate in real-time.

## Picture

![VirtualBox_KALILINUX1_08_11_2024_22_00_28](https://github.com/user-attachments/assets/7f496402-1321-478b-a960-9b17f91bd82a)


## Troubleshooting

- **Error: No wordlist selected**
Ensure that you have selected a valid wordlist file by clicking the "Browse" button.

- **Error: No target URL entered**
Enter the target URL before clicking "Start".

- **Error: Cannot save results**
Ensure that you have selected a valid file path to save the results.

## License
This tool is licensed under the MIT License. See LICENSE for more details.


