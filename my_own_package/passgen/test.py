import unittest
import generator


class TestResult(unittest.TestCase):
    def test_type(self):
        with self.assertRaises(TypeError):
            generator.get_generated_password(12)

    def test_hash(self):
        a = generator.get_generated_password(12, True, True, True, '1')
        b = generator.get_generated_password(12, True, True, True, '1')
        self.assertNotEqual(a, b)


if __name__ == '__main__':
    unittest.main()
