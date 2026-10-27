import os
import csv
import uuid
import shutil
from datetime import datetime

# Определение путей к директориям данных ИС
DATA_DIR = "data"
JOURNAL_FILE = os.path.join(DATA_DIR, "anthropometric_journal.csv")
REPORT_FILE = os.path.join(DATA_DIR, "report_results.txt")

def init_storage():
    """Инициализация каталогов и заголовков CSV-журнала."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Timestamp", "Weight_kg", "Height_cm", "BMI", "Category", "Risk_Level"])

def calculate_bmi(weight_kg, height_cm):
    """Расчет ИМТ, определение категории и числового уровня риска по ВОЗ."""
    if not isinstance(weight_kg, (int, float)) or not isinstance(height_cm, (int, float)):
        raise TypeError("Параметры веса и роста должны быть числового типа.")
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Вес и рост должны быть строго больше нуля.")
    
    height_m = height_cm / 100.0
    bmi = round(weight_kg / (height_m ** 2), 1)
    
    if bmi < 16.0:
        category = "Выраженный дефицит массы тела"
        risk_level = 3
    elif bmi < 18.5:
        category = "Недостаточная масса тела (дефицит)"
        risk_level = 1
    elif bmi < 25.0:
        category = "Нормальная масса тела"
        risk_level = 0
    elif bmi < 30.0:
        category = "Избыточная масса тела (предожирение)"
        risk_level = 2
    elif bmi < 35.0:
        category = "Ожирение I степени"
        risk_level = 2
    elif bmi < 40.0:
        category = "Ожирение II степени"
        risk_level = 3
    else:
        category = "Ожирение III степени"
        risk_level = 3
        
    return bmi, category, risk_level

def add_to_journal(weight_kg, height_cm, bmi, category, risk_level):
    """Анонимизированное логирование в CSV с генерацией уникального UUID и секунд."""
    init_storage()
    row_id = str(uuid.uuid4())
    # ИСПРАВЛЕНИЕ: Формат времени строго приведен к единому стандарту с СЕКУНДАМИ
    timestamp = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    with open(JOURNAL_FILE, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([row_id, timestamp, weight_kg, height_cm, bmi, category, risk_level])
    return timestamp

def get_journal_records():
    """Чтение CSV и формирование красивых ровных строк для Listbox."""
    init_storage()
    records = []
    if not os.path.exists(JOURNAL_FILE):
        return records
    with open(JOURNAL_FILE, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)  # Пропуск строки заголовков
        for row in reader:
            if len(row) >= 6:
                raw_ts = row[1]
                w = row[2]
                h = row[3]
                bmi = row[4]
                cat = row[5]
                
                # ИСПРАВЛЕНИЕ: Автоматическое приведение старых дат (ГГГГ-ММ-ДД) к новому стандарту
                try:
                    if "-" in raw_ts:
                        dt_obj = datetime.strptime(raw_ts, "%Y-%m-%d %H:%M:%S")
                        ts = dt_obj.strftime("%d.%m.%Y %H:%M:%S")
                    else:
                        ts = raw_ts
                except Exception:
                    ts = raw_ts
                
                # Выравнивание колонок с помощью моноширинных табуляций
                record_str = f"{ts}    {w} кг, {h} см    ИМТ {bmi}    ({cat})"
                records.append(record_str)
    return records

def create_backup():
    """Резервное копирование текущей базы логов."""
    init_storage()
    if not os.path.exists(JOURNAL_FILE):
        raise FileNotFoundError("Рабочий журнал не найден для резервного копирования.")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_filename = f"journal_backup_{timestamp}.csv"
    backup_path = os.path.join(DATA_DIR, backup_filename)
    
    shutil.copy2(JOURNAL_FILE, backup_path)
    return backup_filename

def export_report():
    """Генерация структурированного текстового отчета."""
    init_storage()
    records = get_journal_records()
    with open(REPORT_FILE, mode="w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write("          СВОДНЫЙ АНТРОПОМЕТРИЧЕСКИЙ ОТЧЕТ СИСТЕМЫ\n")
        f.write(f" Дата генерации: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f" Активных логов в базе: {len(records)}\n")
        f.write("=" * 60 + "\n\n")
        for idx, r in enumerate(records, 1):
            f.write(f" Запись №{idx:03d} │ {r}\n")
        f.write("\n" + "=" * 60 + "\n")
    return REPORT_FILE