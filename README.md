# Пользовательская документация по эксплуатации ИС

## 1. Краткое описание программы
Разработанный программный комплекс представляет собой специализированную консольную систему на языке Python, предназначенную для автоматизированного расчета индекса массы тела (ИМТ). Приложение позволяет в интерактивном или пакетном режиме вычислять показатели здоровья на основе введенных пользователем веса и роста, выдавая соответствующие медицинские рекомендации ВОЗ. Программа оснащена автономной подсистемой администрирования, которая обеспечивает надежную сериализацию анонимизированных антропометрических журналов и реализует алгоритмы их регулярного резервного копирования и аварийного восстановления.

## Задание
* Создание консольной программы на языке Python с возможным вводом и выводом данных через файл и через консоль для нахождения: «Индекса массы тела (ИМТ) и выдачи соответствующих медицинских рекомендаций на основе введенных пользователем веса и роста».
* Разработка алгоритма резервного копирования и восстановления анонимизированных антропометрических журналов для ПО.
* Разработка пользовательской документации (ТЗ, руководства пользователя [README.md на русском и английском языках] и регламента технического обслуживания) и их фиксация с проектом в GitHub.
* Составить тест-кейсы и проверить работоспособность ключевых модулей ИС на соответствие техническому заданию.

## Технологии
* **Python 3.8+** — Основной язык программирования
* **JSON** — Текстовый формат обмена и хранения профилей параметров
* **Shutil и OS** — Модули сопровождения, бэкапа и работы с файловой системой
* **Unittest** — Фреймворк автоматизированного тестирования модулей

## 2. Гайд по установке

### Системные требования:
* **Операционная система:** Windows 10/11, macOS или дистрибутивы Linux.
* **Интерпретатор:** Среда выполнения Python версии 3.8 или выше.
* **Права доступа:** Разрешение на запись файлов в целевую директорию проекта.

### Пошаговый процесс установки:
1. Клонируйте репозиторий или скачайте три исходных файла программного кода (`bmi_func.py`, `bmi_gui.py`, `main.py`) с репозитория.
2. Поместите все три файла в одну общую рабочую папку на диске компьютера (рекомендуется использовать путь без русских букв и пробелов в названии, например: `C:\zadanie\`).
3. Откройте терминал или командную строку Windows в созданной директории с файлами.
4. Убедитесь, что интерпретатор Python доступен в системе, выполнив команду:
   ```bash
   python --version
   ```
   Дополнительная установка сторонних библиотек и пакетов не требуется.

## Структура проекта
```text
zadanie/
├── bmi_func.py  # Функциональное ядро расчетов ИМТ, сериализации и бэкапа
├── bmi_gui.py   # Консольная интерактивная оболочка ввода-вывода данных
├── maine.py  # Главный исполнительный модуль (пусковой файл ИС)
├── test_prog.py  ИСПРАВИТЬ!    # Автоматизированные unit-тесты верификации кода
├── TZ.md   ИСПРАВИТЬ!           # Техническое задание (C-требования заказчика)
└── README.md         # Пользовательская документация (Руководство пользователя)
```

## 3. Гайд по использованию

### Запуск программного комплекса:
Для инициализации ИС выполните в терминале команду запуска главного исполнительного модуля:
```bash
python maine.py ИСПРАВИТЬ!
```

### Интерактивный расчет в консоли:
1. Запустите программу и выберите режим интерактивного ввода параметров.
2. Введите числовые значения параметров по запросу системы:
   * **Вес пользователя** — в килограммах (например: 75.5).
   * **Рост пользователя** — в метрах (например: 1.78).
3. Нажмите Enter для мгновенного вывода значения ИМТ и официальной медицинской рекомендации ВОЗ.
4. Подтвердите сохранение записи, чтобы зафиксировать анонимизированные данные в антропометрическом журнале.

### Пакетный режим обработки файлов JSON:
1. Выберите в интерактивном меню пакетный режим обработки файлов.
2. Поместите входной файл настроек параметров (например, `input.json`) в корневой каталог программы.
3. Укажите имя файла для сохранения результатов (например, `output.json`). Вычисления пройдут в автоматическом фоновом режиме.

### Административный регламент сопровождения (Бэкап):
* **Создание точки восстановления:** Выберите пункт меню «Создать резервную копию (Бэкап)». Подсистема автоматически скопирует базу данных анонимизированных журналов в изолированный каталог `backups/` под уникальным штампом даты и времени.
* **Аварийный откат:** При случайном удалении или повреждении рабочей конфигурации выберите пункт меню «Восстановить из бэкапа». Система самостоятельно найдет последний свежий архив и вернет ИС к стабильному состоянию.

# User Documentation for IS Operation (Variant 23)

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

### Administrative Maintenance Regulations (Backup):
* **Creating a Restore Point:** Select the "Create Backup" menu option. The subsystem will automatically copy the anonymized log database into an isolated `backups/` directory under a unique date and timestamp.
* **Emergency Rollback:** In case of accidental data deletion or corruption of the working configuration, select "Restore from Backup". The system will automatically find the latest archive and restore the IS to a stable state.
