# User Documentation for IS Operation

## 1. Short Program Description
The developed software package is a specialized console system in Python designed for automated body mass index (BMI) calculation. The application allows calculating health metrics in either interactive or batch mode based on user-entered weight and height, providing corresponding WHO medical recommendations. The program features an autonomous administration subsystem that ensures reliable serialization of anonymized anthropometric logs and implements regular backup and emergency disaster recovery algorithms.

## Task Requirements
* Development of console software in Python with data input/output via file and console to calculate: "Body Mass Index (BMI) and provision of corresponding medical recommendations based on user weight and height".
* Development of a backup and recovery algorithm for anonymized anthropometric logs.
* Development of user documentation (Terms of Reference, User Manual [README.md in Russian and English], and technical maintenance regulations) and their commit to GitHub.
* Creation of test cases and verification of core IS modules compliance with the project specifications.

## Technologies
* **Python 3.8+** — Main programming language
* **JSON** — Text format for parameter profiles storage and serialization
* **Shutil & OS** — System modules for maintenance, backup, and file system operations
* **Unittest** — Automated module unit testing framework

## 2. Installation Guide

### System Requirements:
* **Operating System:** Windows 10/11, macOS, or Linux distributions.
* **Interpreter:** Python runtime environment version 3.8 or higher.
* **Access Rights:** Permissions to write files in the target project directory.

### Step-by-Step Installation:
1. Clone the repository or download three source code files (`bmi_func.py`, `bmi_gui.py`, `main.py`) from the repository.
2. Place all three files into a single working folder on your disk (it is recommended to use paths without spaces, e.g., `C:\zadanie\`).
3. Open a terminal or Windows Command Prompt in the created directory.
4. Verify that the Python interpreter is available in your system by executing:
   ```bash
   python --version
   ```
   No additional third-party libraries or packages are required.

## Project Structure
```text
zadanie/
├── bmi_func.py  # Core functional engine for BMI calculations, serialization & backup
├── bmi_gui.py   # Console interactive UI shell for data input/output
├── maine.py  # Main execution module (launch file)
├── test_prog.py  ИСПРАВИТЬ!    # Automated unit tests for code verification
├── TZ.md   ИСПРАВИТЬ!           # Technical Specifications (Customer C-requirements)
└── README.md         # User Documentation (User Guide)
```

## 3. Usage Guide

### Launching the Program:
To initialize the IS, execute the main module launch command in your terminal:
```bash
python maine.py ИСПРАВИТЬ!
```

### Interactive Calculation via Console:
1. Launch the program and choose the interactive input mode from the menu.
2. Enter numeric parameter values as prompted by the system:
   * **User Weight** — in kilograms (e.g., 75.5).
   * **User Height** — in meters (e.g., 1.78).
3. Press Enter to instantly view the calculated BMI value and official WHO medical guidelines.
4. Confirm data saving to record the anonymized entry into the anthropometric log file.

### Batch Processing of JSON Files:
1. Select the batch file processing mode from the interactive menu.
2. Place your input configuration file (e.g., `input.json`) into the root directory of the application.
3. Specify the output file name for saving the results (e.g., `output.json`). Calculations will run in an automated background mode.

Developer: Van I.L
### Administrative Maintenance Regulations (Backup):
* **Creating a Restore Point:** Select the "Create Backup" menu option. The subsystem will automatically copy the anonymized log database into an isolated `backups/` directory under a unique date and timestamp.
* **Emergency Rollback:** In case of accidental data deletion or corruption of the working configuration, select "Restore from Backup". The system will automatically find the latest archive and restore the IS to a stable state.
