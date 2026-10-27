import unittest
import os
import bmi_func as core

class TestBmiFullSystem(unittest.TestCase):

    # ГРУППА 1: Тестирование вычислений ИМТ и категорий ВОЗ (5 тест-кейсов)
    def test_calc_normal(self):
        """Тест 1.1: Проверка нормального веса человека (ИМТ 22.9, Риск 0)"""
        bmi, cat, risk = core.calculate_bmi(70, 175)
        self.assertEqual(bmi, 22.9)
        self.assertEqual(cat, "Нормальная масса тела")
        self.assertEqual(risk, 0)

    def test_calc_underweight(self):
        """Тест 1.2: Проверка дефицита массы тела (ИМТ 17.3, Риск 1)"""
        bmi, cat, risk = core.calculate_bmi(50, 170)
        self.assertEqual(bmi, 17.3)
        self.assertEqual(cat, "Недостаточная масса тела (дефицит)")
        self.assertEqual(risk, 1)

    def test_calc_overweight(self):
        """Тест 1.3: Проверка предожирения (ИМТ 27.8, Риск 2)"""
        bmi, cat, risk = core.calculate_bmi(85, 175)
        self.assertEqual(bmi, 27.8)
        self.assertEqual(cat, "Избыточная масса тела (предожирение)")
        self.assertEqual(risk, 2)

    def test_calc_obesity_1(self):
        """Тест 1.4: Проверка ожирения I степени (ИМТ 32.9, Риск 2)"""
        bmi, cat, risk = core.calculate_bmi(95, 170)
        self.assertEqual(bmi, 32.9)
        self.assertEqual(cat, "Ожирение I степени")
        self.assertEqual(risk, 2)

    def test_calc_obesity_3(self):
        """Теst 1.5: Проверка тяжелого ожирения III степени (ИМТ 45.0, Риск 3)"""
        bmi, cat, risk = core.calculate_bmi(130, 170)
        self.assertEqual(bmi, 45.0)
        self.assertEqual(cat, "Ожирение III степени")
        self.assertEqual(risk, 3)


    # ГРУППА 2: Тестирование валидации параметров и защиты от неверного ввода (5 тест-кейсов)
    def test_validation_zero_weight(self):
        """Тест 2.1: Блокировка нулевого веса (ValueError)"""
        with self.assertRaises(ValueError):
            core.calculate_bmi(0, 175)

    def test_validation_negative_height(self):
        """Тест 2.2: Блокировка отрицательного роста (ValueError)"""
        with self.assertRaises(ValueError):
            core.calculate_bmi(70, -175)

    def test_validation_string_weight(self):
        """Тест 2.3: Блокировка строковых символов в поле веса (TypeError)"""
        with self.assertRaises(TypeError):
            core.calculate_bmi("70", 175)

    def test_validation_string_height(self):
        """Тест 2.4: Блокировка строковых символов в поле роста (TypeError)"""
        with self.assertRaises(TypeError):
            core.calculate_bmi(70, "175")

    def test_validation_none_values(self):
        """Тест 2.5: Блокировка передачи пустых объектов None (TypeError)"""
        with self.assertRaises(TypeError):
            core.calculate_bmi(None, None)

    # ГРУППА 3: Тестирование подсистемы анонимного логирования (5 тест-кейсов)
    def test_log_file_creation(self):
        """Тест 3.1: Проверка автоматического создания файла базы логов"""
        core.init_storage()
        self.assertTrue(os.path.exists(core.JOURNAL_FILE))

    def test_log_execution_success(self):
        """Тест 3.2: Проверка успешного возврата временной метки записи лога"""
        ts = core.add_to_journal(70, 175, 22.9, "Нормальная масса тела")
        self.assertNotEqual(ts, "")

    def test_log_timestamp_presence(self):
        """Тест 3.3: Проверка автоматической генерации штампа времени лога"""
        ts = core.add_to_journal(70, 175, 22.9, "Нормальная масса тела")
        self.assertTrue(len(ts) > 0)

    def test_log_anonymization_uuid(self):
        """Тест 3.4: Верификация структуры возвращаемого списка логов"""
        records = core.get_journal_records()
        self.assertIsInstance(records, list)

    def test_log_reader_stability(self):
        """Тест 3.5: Проверка отказоустойчивости парсера базы при чтении"""
        try:
            core.get_journal_records()
            flag = True
        except Exception:
            flag = False
        self.assertTrue(flag)

    # =========================================================================
    # ГРУППА 4: Тестирование резервного копирования и отчетов (5 тест-кейсов)
    # =========================================================================
    def test_sys_backup_creation(self):
        """Тест 4.1: Проверка физического копирования бэкапа методом shutil"""
        filename = core.create_backup()
        backup_path = os.path.join(core.DATA_DIR, filename)
        self.assertTrue(os.path.exists(backup_path))

    def test_sys_backup_extension(self):
        """Тест 4.2: Проверка валидности формата расширения бэкапа (.csv)"""
        filename = core.create_backup()
        self.assertTrue(filename.endswith(".csv"))

    def test_sys_report_creation(self):
        """Тест 4.3: Проверка физического развертывания текстового отчета"""
        filepath = core.export_report()
        self.assertTrue(os.path.exists(filepath))

    def test_sys_report_name(self):
        """Тест 4.4: Проверка точного имени экспортируемого файла по ТЗ"""
        filepath = core.export_report()
        self.assertEqual(os.path.basename(filepath), "report_results.txt")

    def test_sys_directory_persistence(self):
        """Тест 4.5: Проверка существования изолированной папки хранения data/"""
        core.init_storage()
        self.assertTrue(os.path.isdir(core.DATA_DIR))

if __name__ == "__main__":
    unittest.main()
