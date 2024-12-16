import logging
import unittest
from module_12_4 import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='utf-8', format="%(asctime)s | %(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r1 = Runner('r1', -3)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            r2 = Runner((1, 2))
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = Runner('r3')
        r4 = Runner('r4')
        for _ in range(10):
            r3.run()
            r4.walk()
        self.assertNotEqual(r3.distance, r4.distance)

if __name__ == '__main__':
    unittest.main()