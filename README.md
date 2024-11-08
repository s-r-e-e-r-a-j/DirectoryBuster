## Directory Buster
Directory Buster is a simple yet powerful tool for discovering hidden directories and files on a target web server using a wordlist-based approach. It's designed to assist security professionals and enthusiasts with directory brute-forcing to identify potentially vulnerable or hidden resources on a web server.

## Features:
- Enter the target URL to start brute-forcing.
- Choose a wordlist for directory names.
- Option to save found results to a text file.
- Scrolled text boxes to display both found and non-found results.
- Clickable URLs in the "Found Results" section to open them directly in a web browser.
- Option to stop the brute-force process anytime.
## Installation
1.Clone the repository to your local machine
```bash
https://github.com/s-r-e-e-r-a-j/DIRECTORYBUSTER-TOOL.git
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

- **Save Results (Optional)**:

If you want to save the found results, check the "Save found results" checkbox and specify the file location using the "Select Save File" button.

- **Start Directory Busting**:

Click the "Start" button to begin the directory busting process. The tool will start testing directories from the wordlist against the target URL.

- **Found Results**:

The "Found Results" section will display any discovered directories with a clickable URL. Click on a URL to open it directly in your default web browser.

- **Stop Directory Busting**:

Click the "Stop" button anytime to halt the directory busting process.
