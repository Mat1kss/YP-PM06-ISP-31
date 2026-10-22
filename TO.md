> ### NAVIGATION/НАВИГАЦИЯ
> 🇷🇺 **[Русское руководство](README.RU.md)** │ en **[English User Guide](README.md)** │ **[Техническое задание (TZ.txt)](TZ.txt)** │ **Регламент ТО (TO.md)**

---

# TECHNICAL MAINTENANCE (TM) PROTOCOL

**Information System: "Body Mass Index (BMI) Calculation with Anonymized Log Maintenance"**

---

## 1. Overview and General Provisions

### 1.1. Purpose of the Document
This protocol defines the procedures, frequency, scope of work, and areas of responsibility for the technical maintenance of the "Body Mass Index (BMI) Calculation" information system (hereinafter referred to as the "IS"). The implementation of this protocol is intended to minimize IS downtime, prevent the loss of anonymized anthropometric data, and ensure the security and operational stability of the software suite.

### 1.2. Scope
The rules set forth in this protocol apply to the software and hardware components utilized by the IS:

* **Hardware:** Personal computer (workstation) with x86-64 architecture and standard input/output devices.
* **Software:** Operating system (Windows 10/11, macOS, or Linux), Python interpreter (version 3.8 or higher), and standard libraries (`tkinter`, `csv`, `shutil`, `os`, `unittest`).
* **File Structure:** IS working directories (`data/`, `backups/`), executable modules (`main.py`, `bmi_gui.py`, `bmi_func.py`), and log files (`.csv`).

### 1.3. Roles and Responsibilities

* **User (Operator):** An individual (e.g., a fitness trainer or healthcare professional) responsible for accessing the IS, entering data, and initiating maintenance operations via the graphical user interface. * **Support Specialist (Technician):** Responsible for installing updates, verifying software authenticity, restoring data from backups in the event of a failure, and maintaining the network.

---

## 2. Maintenance Procedures (Tech Sheets)

All maintenance tasks are divided into two categories: **scheduled (preventive) maintenance** and **unscheduled (emergency/corrective) maintenance**.

### 2.1. Scheduled (Preventive) Maintenance

| No. | Operation Name | Frequency | Type | Step-by-step Procedure and Expected Result | Tools Used |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | BMI calculation check and interface verification | Daily | Scheduled | 1. Launch `main.py`. <br>2. Enter test data (weight 70, height 175). <br>3. Verify that the BMI = 22.9 (Normal). <br>**Expected result:** The interface displays correctly without errors. | `main.py`, `bmi_gui.py` |
| **2** | Backing up measurement logs | Daily | Scheduled | 1. Click the "Backup Log" button. <br>2. Confirm that a file with a timestamp appears in the `backups/` folder. <br>**Expected result:** A valid file copy is created. | `bmi_func.py`, `shutil` |
| **3** | Verifying anonymity of measurement logs | Weekly | Scheduled | 1. Open `data/anthropometric_journal.csv`. <br>2. Confirm the presence of a UUID and the absence of full names or passport/ID details. <br>**Expected result:** No personal data is identified. | Text editor / Excel |
| **4** | Verification and review of backups | Monthly | Scheduled | 1. Check the `backups/` directory. <br>2. Delete backups older than 3 months. <br>3. Verify that the most recent files can be opened. <br>**Expected result:** No disk overflow occurs. | OS File Explorer |
| **5** | Running regression tests | Monthly | Scheduled | 1. Open the terminal. <br>2. Execute: `python -m unittest discover -s tests -v`. <br>**Expected result:** All 12 tests pass (OK); no discrepancies with the technical specifications. | `unittest`, terminal |
| **6** | Software updates | Annually (or upon release) | Scheduled | 1. Download the new version from the GitHub repository. <br>2. Replace the files `bmi_func.py` and `bmi_gui.py`. <br>**Expected result:** Update completed without loss of log data. | Git, GitHub |

### 2.2. Unscheduled (Emergency) Maintenance

| No. | Operation Name | Frequency | Maintenance Type | Step-by-step Procedure and Expected Result | Tools Used |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | Restoring the log from a backup | In case of failure / data loss | Unscheduled | 1. Open the `backups/` folder. <br>2. Locate the most recent valid `.csv` file. <br>3. Copy it to the `data/` folder, replacing the corrupted file. <br>**Expected result:** Information system functionality restored. | OS File Explorer |
| **2** | Resolving data entry errors (Validation) | Upon occurrence of an error | Unscheduled | 1. A warning appears if negative values ​​or zero are entered. <br>2. Verify the correctness of the input (cm/kg). <br>**Expected result:** The program does not freeze and displays an error message. | `bmi_func.py` |
| **3** | Diagnosing software startup failure | In case of failure | Unscheduled | 1. Open the command line. <br>2. Run `python main.py` to display the error in the console. <br>3. Check the Python version (`python --version`). <br>**Expected result:** The cause of the failure is identified and resolved. | Command line, Python |
| **4** | Restoring GUI functionality | If the interface freezes | Unscheduled | 1. Terminate the process via Task Manager. <br>2. Check for available RAM (at least 50 MB required). <br>3. Restart `main.py`. <br>**Expected result:** The interface functions as intended. | OS Task Manager |

---

## 3. Quality Control and Reporting

### 3.1. Control Parameters
The effectiveness of maintenance (technical support) is evaluated based on the following metrics:

* **IS Availability Factor:** Uptime must be at least **99%** of total operating time.
* **Recovery Speed:** The time from a failure to full restoration from a backup must not exceed **15 minutes**.
* **Data Integrity:** Loss of log entries during standard backup procedures is unacceptable (**0% loss**).
* **Performance:** RAM consumption must not exceed **50 MB** (in accordance with the Technical Specifications, item 7).

---

**Developer:** Van I. L.

---

# РЕГЛАМЕНТ ТЕХНИЧЕСКОГО ОБСЛУЖИВАНИЯ (ТО)

**Информационной системы «Расчет индекса массы тела (ИМТ) с ведением анонимизированного журнала»**

---

## 1. Паспортная часть и общие положения

### 1.1. Назначение документа
Настоящий регламент определяет порядок, периодичность, содержание работ и зоны ответственности специалистов при техническом обслуживании информационной системы (далее — ИС) «Расчет индекса массы тела». Внедрение регламента направлено на минимизацию времени простоев ИС, предотвращение потери анонимизированных антропометрических данных, обеспечение безопасности и стабильности работы программного комплекса.

### 1.2. Область применения
Правила настоящего регламента распространяются на программное и аппаратное обеспечение, задействованное в работе ИС:

* **Аппаратное обеспечение:** Персональный компьютер (рабочая станция) с архитектурой x86-64, стандартные устройства ввода-вывода.
* **Программное обеспечение:** Операционная система (Windows 10/11, macOS, Linux), интерпретатор Python версии 3.8 и выше, стандартные библиотеки (`tkinter`, `csv`, `shutil`, `os`, `unittest`).
* **Файловая структура:** Рабочие директории ИС (`data/`, `backups/`), исполняемые модули (`main.py`, `bmi_gui.py`, `bmi_func.py`), файлы журналов (`.csv`).

### 1.3. Роли участников

* **Пользователь (Оператор):** Сотрудник (фитнес-тренер, медработник), осуществляющий эксплуатацию ИС, ввод данных и запуск регламентных операций через графический интерфейс.
* **Специалист по сопровождению (Техник):** Ответственный за установку обновлений, проверку целостности ПО, восстановление данных из резервных копий при сбоях и ведение отчетности.

---

## 2. Технологические карты ТО

Все работы по ТО разделены на два вида: **плановое (профилактическое) ТО** и **внеплановое (аварийное) ТО**.

### 2.1. Плановое (профилактическое) ТО

| № | Наименование операции | Периодичность | Вид ТО | Пошаговый алгоритм и ожидаемый результат | Используемые инструменты |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | Контрольный расчет ИМТ и проверка интерфейса | Ежедневно | Плановое | 1. Запустить `main.py`. <br>2. Ввести тестовые данные (вес 70, рост 175). <br>3. Убедиться, что ИМТ = 22.9 (Норма). <br>**Ожидаемый результат:** корректный вывод интерфейса без ошибок. | `main.py`, `bmi_gui.py` |
| **2** | Резервное копирование журнала измерений | Ежедневно | Плановое | 1. Нажать кнопку «Резервная копия журнала». <br>2. Проверить появление файла в папке `backups/` с меткой времени. <br>**Ожидаемый результат:** создан валидный файл копии. | `bmi_func.py`, `shutil` |
| **3** | Проверка журнала измерений на анонимность | Еженедельно | Плановое | 1. Открыть `data/anthropometric_journal.csv`. <br>2. Убедиться в наличии UUID, отсутствии ФИО и паспортных данных. <br>**Ожидаемый результат:** персональные данные не сохраняются. | Текстовый редактор / Excel |
| **4** | Проверка целостности и ревизия резервных копий | Ежемесячно | Плановое | 1. Просмотреть каталог `backups/`. <br>2. Удалить устаревшие копии (старше 3 месяцев). <br>3. Проверить открытие последней копии. <br>**Ожидаемый результат:** переполнение диска не допущено. | Проводник ОС |
| **5** | Запуск регрессионного тестирования | Ежемесячно | Плановое | 1. Открыть терминал. <br>2. Выполнить: `python -m unittest discover -s tests -v`. <br>**Ожидаемый результат:** все 12 тестов (ОК), расхождений с ТЗ нет. | `unittest`, терминал |
| **6** | Обновление программного обеспечения | Ежегодно (или по мере выхода) | Плановое | 1. Скачать новую версию из репозитория GitHub. <br>2. Заменить файлы `bmi_func.py`, `bmi_gui.py`. <br>**Ожидаемый результат:** обновление без потери журналов данных. | Git, GitHub |

### 2.2. Внеплановое (аварийное) ТО

| № | Наименование операции | Периодичность | Вид ТО | Пошаговый алгоритм и ожидаемый результат | Используемые инструменты |
| :-: | :--- | :--- | :--- | :--- | :--- |
| **1** | Восстановление журнала из резервной копии | При сбое / потере данных | Внеплановое | 1. Открыть папку `backups/`. <br>2. Найти последний актуальный `.csv` файл. <br>3. Скопировать его в папку `data/`, заменив поврежденный файл. <br>**Ожидаемый результат:** работоспособность ИС восстановлена. | Проводник ОС |
| **2** | Устранение ошибок ввода данных (Валидация) | При возникновении ошибки | Внеплановое | 1. При вводе отрицательных значений или нуля появляется предупреждение. <br>2. Проверить корректность ввода (см/кг). <br>**Ожидаемый результат:** программа не зависает, выдает сообщение об ошибке. | `bmi_func.py` |
| **3** | Диагностика отказа запуска ПО | При отказе | Внеплановое | 1. Открыть командную строку. <br>2. Запустить `python main.py` для вывода ошибки в консоль. <br>3. Проверить версию Python (`python --version`). <br>**Ожидаемый результат:** выявлена и устранена причина сбоя. | Командная строка, Python |
| **4** | Восстановление работоспособности GUI | При зависании интерфейса | Внеплановое | 1. Завершить процесс через Диспетчер задач. <br>2. Проверить наличие свободной оперативной памяти (не более 50 МБ). <br>3. Перезапустить `main.py`. <br>**Ожидаемый результат:** интерфейс работает штатно. | Диспетчер задач ОС |

---

## 3. Контроль качества и отчетность

### 3.1. Параметры контроля
Эффективность ТО оценивается по следующим метрикам:

* **Коэффициент доступности ИС:** время бесперебойной работы должно составлять не менее **99%** рабочего времени.
* **Скорость восстановления:** время от момента сбоя до полного восстановления из резервной копии не должно превышать **15 минут**.
* **Целостность данных:** потеря записей журнала при штатном резервном копировании недопустима (**0% потерь**).
* **Производительность:** потребление оперативной памяти не должно превышать **50 МБ** (согласно ТЗ п.7).

---

**Разработчик:** Ван И. Л.
