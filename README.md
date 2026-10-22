# Body Mass Index (BMI) Calculation

A software package with a graphical interface for automated calculation of body mass index (BMI), maintaining an anonymized measurement log, and issuing WHO medical recommendations.

---

## EN — User Documentation for IS Operation

### 1. Brief Program Description
The developed software package is a specialized system written in Python, equipped with a graphical user interface (GUI). The application allows you to interactively calculate health indicators based on the user‑entered weight (kg) and height (cm), providing the corresponding official WHO medical recommendations. 

The program is equipped with an administration subsystem that ensures reliable serialization of anonymized anthropometric logs in CSV format and also implements algorithms for their regular backup and disaster recovery.

### Project goals and objectives
* **Software development:**Creating a program in Python with a graphical interface to calculate the body mass index (BMI) and automatically generate recommendations based on anthropometric data (weight in kilograms, height in centimeters).**
* **Storage and administration system:** Developing an algorithm for anonymized logging (using unique UUIDs) to CSV files, as well as backup and recovery procedures for the data.
* **Documentation:**Compilation of a complete set of technical and user documentation (Technical Specification, User Manual [README.md in Russian and English], and Maintenance Procedure) for storage in the GitHub repository.
* **Verification:** Compilation of test cases and conducting automated regression testing of key IS modules to ensure compliance with the technical specification.

### Technologies
* **Python 3.8+** — the main programming language.
* **Tkinter** — building a graphical user interface (GUI).
* **CSV** — a format for structured storage of anonymized measurement logs.
* **Shutil and OS** — modules for maintenance, backup, and direct interaction with the file system.
* **Unittest** — a framework for automated testing of module functionality.

---

### 2. Installation guide

#### System requirements:
* **Operating system:** Windows 10/11, macOS, or Linux distributions.
* **Interpreter:** Python runtime environment version 3.8 or higher.
* **Permissions:** The operating system has permission to read and write files to the project’s target directory.

#### Step‑by‑step installation process:
1. Clone the repository or download the project source files:
   ```bash
   git clone https://github.com
   cd bmi-calculator
   ```
2. Place the files in a common working folder on the computer’s disk (it is recommended to use a path without Cyrillic characters and spaces in the names, for example: `C:\bmi_project\`).
3. Open the terminal or command line in the created directory with the files.
4. Check the availability of the Python interpreter in the system by running the command:
   ```bash
   python --version
   ```
   *No additional installation of third‑party libraries and packages is required; only built‑in modules are used.*

---

### Project structure
The actual file structure of the software complex in the repository:
```text
bmi-calculator/
├── data/
│   ├── anthropometric_journal.csv     # Measurement journal (created automatically)
│   ├── journal_backup_...csv          # Internal backup files
│   └── report_results.txt             # Exportable text reports
├── bmi_func.py                        # Functional core (calculations, CSV logic, backup)
├── bmi_gui.py                         # Tkinter-based graphical user interface
├── main.py                            # Main execution module (entry point to the system)
├── test_bmi_func.py                   # Automated unit tests for code verification
├── README.md                          # Bilingual user documentation (current file)
├── TZ.md                              # Technical specification (customer requirements)
└── maintenance_regulations.md         # IS maintenance regulations (MR)
```

---

### 3. User manual

#### Launching the software complex:
To initialize the IS graphical interface, run the following command in the terminal to launch the main startup module:
```bash
python main.py
```

#### Interactive calculation in the graphical user interface (GUI):
1. In the program window, find the input fields for anthropometric parameters.
2. Enter the numerical values:
   * **User weight** — in kilograms (for example: `70`).
   * **User height** — in centimeters (for example: `175`).
3. Click the **“Calculate”** button — the panel will instantly display the exact BMI value, the weight status category according to the WHO classification, and personal recommendations.
4. Click the **“Add to journal”** button to record the anonymized entry (it will be automatically assigned a UUID) in the `data/anthropometric_journal.csv` file.
5. To create a manual recovery point, click **“Backup journal”** The copy will be saved in the `data/` folder with a date and time stamp.
6. To export the text results, click **“Export report”**.

#### Restoring data from a backup:
In case of accidental deletion, damage, or loss of the working journal:
1. Go to the `data/` directory.
2. Find the latest current backup file in the format `journal_backup_YYYYMMDD_HHMMSS.csv`.
3. Rename it or copy it under the name `anthropometric_journal.csv` (replacing the damaged file).

---

### 4. Testing
Since the automated test file `test_bmi_func.py` is located in the project’s root directory, running comprehensive regression testing of the modules to ensure they meet the technical requirements is done using the following command:
```bash
python -m unittest test_bmi_func.py -v
```

---

Developer: Van I. L.
