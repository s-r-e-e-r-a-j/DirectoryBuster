## Directory Buster

**Directory Buster** is a Python-based directory brute-forcing tool with a user-friendly GUI. It helps discover hidden directories and files on a web server by attempting various directory names from a wordlist.  this tool is easy to set up and operate
## Tool Graphical User Interface

![Screenshot 2024-11-08 010145](https://github.com/user-attachments/assets/3f052ea9-e517-4278-a82f-6dbfe92ee1fe)


## Features
- **Simple GUI**: Easy-to-use interface for URL input and wordlist selection.
- **Save Results Option**: Option to save found directories to a file.
- **Real-Time Display**: Shows found and not found directories as the scan progresses
- **Clickable URLs**: Found URLs can be clicked to open directly in a web browser.
Stop Functionality: Stop the scan anytime with the stop button.
- **Hover Effects**: Cursor changes to a pointer on hover over URLs, with highlighted URLs.
 
## Requirements

- **Python 3.x**
- **requests library**
 
## Installation

1. Clone this repository:
```bash
git clone https://github.com/s-r-e-e-r-a-j/DIRECTORYBUSTER-TOOL.git
```
```bash
cd DIRECTORYBUSTER-TOOL
```
2. Go to the project folder:
```bash
cd DIRECTORYBUSTER
```
3.Install dependencies:
```bash
pip3 install requests
```
## Usage

1.Run the tool:

```bash
python3 directorybuster.py
```
2. Enter the Target URL and choose a Wordlist File (e.g., a .txt file with potential directories)
3. 

All Wordlists for this tool are available at this path in kali linux `/usr/share/wordlists/dirbuster`

3. (Optional) To save results, check Save found results to file and select a save location


4.Click Start Directory Buster to initiate scanning


5. Click Stop to stop scanning anytime.


6. View results in the output area. Click any found URL to open it in your default web browser.


  ## License
  This project is licensed under the MIT License. See the LICENSE file for details.
  
## Credits
Created by Sreeraj
