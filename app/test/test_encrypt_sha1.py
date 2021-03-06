import unittest
from app.modules.encrypt_sha1 import encrypt_sha1
from app.modules.error_messages import error_messages


class TestEncryptSHA1(unittest.TestCase):

    # Successful testing, expected result SHA1

    def test_string(self):
        result = encrypt_sha1('test')
        self.assertRegex(result, '[0-9a-f]{0,40}')

    # Expected failures

    def test_int(self):
        result = encrypt_sha1(10)
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_boolean(self):
        result = encrypt_sha1(0.54)
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_list(self):
        result = encrypt_sha1([10, 5.2, '2', True])
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))

    def test_dict(self):
        result = encrypt_sha1({'data': 2, 'name': 'test'})
        self.assertEqual(result, error_messages('MSG_TYPE_ERROR'))


if __name__ == '__main__':
    unittest.main()
