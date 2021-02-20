# import testing module and memcached class
import unittest
import memcached
# initialize a memcached object to perform tests
cache = memcached.Memcached()

err_msg = "CLIENT_ERROR bad data chunk \n ERROR"

"""Function to handle string byte size"""
def utf8len(s):
    return len(s.encode('utf-8'))  

class TestMemcached(unittest.TestCase):
  
    def test_set(self):
        # test whether key-value pair is correctly stored
        cache.set('test_key', 'test_value', utf8len('test_value'))
        self.assertEqual('test_value', cache.storage['test_key'])
        # test whether byte lenght correctly filters wrong storages
        response = cache.set('test_key0', 'test_value0', 0)
        self.assertEqual(response, err_msg)

    def test_add(self):
        # test whether key-value pair is correctly added
        cache.set('test_key0', 'test_value0', utf8len('test_value0'))
        cache.add('test_key1', 'test_value1', utf8len('test_value1'))
        self.assertEqual('test_value1', cache.storage['test_key1'])
        # test whether adding to existing key throws error message
        response = cache.add('test_key0', 'test_value2', utf8len('test_value2'))
        self.assertEqual(err_msg, response)
        # test byte size 
        response_byte = cache.add('test_key2', 'test_value2', 0)
        self.assertEqual(response_byte, err_msg)

    def test_replace(self):
        # test whether value is correctly replaced by new value
        cache.set('test_key', 'test_value', utf8len('test_value'))
        value = cache.replace('test_key', 'new_test_value', utf8len('new_test_value')) 
        self.assertEqual('new_test_value', value)  
        # test whether passing non-existent value to replace function correctly throws error 
        response_argument = cache.replace('non_existent_test_key', 'new_test_value', utf8len('new_test_value'))
        self.assertEqual(response_argument, err_msg)
        response_byte = cache.replace('test_key', 'new_test_value', 0) 
        self.assertEqual(response_byte, err_msg)

    def test_append(self):
        # test whether append command correctly appends value to end of value
        cache.set('test_key', 'test_value', utf8len('test_value'))
        response = cache.append('test_key', 'append_value', utf8len('append_value'))
        self.assertEqual(response, 'test_value' + 'append_value')
        # test byte size and key storage controls
        response_argument = cache.append('non_existent_test_key', 'append_value', utf8len('append_value'))
        self.assertEqual(response_argument, err_msg)
        response_byte = cache.append('test_key', 'append_value', 0)
        self.assertEqual(response_byte, err_msg)

    def test_prepend(self):
        # test whether prepend command correctly appends value to end of value
        cache.set('test_key', 'test_value', utf8len('test_value'))
        response = cache.prepend('test_key', 'append_value', utf8len('append_value'))
        self.assertEqual(response, 'append_value' + 'test_value')
        # test byte size and key storage controls
        response_argument = cache.prepend('non_existent_test_key', 'append_value', utf8len('append_value'))
        self.assertEqual(response_argument, err_msg)
        response_byte = cache.prepend('test_key', 'append_value', 0)
        self.assertEqual(response_byte, err_msg)
        

    def test_get(self):
        # test whether memcached response to get is correct
        cache.set('test_key', 'test_value', utf8len('test_value'))
        response =  cache.get('test_key')  
        self.assertEqual('test_value', response)
        # test get command on non-existent key
        self.assertEqual(cache.get('nonexistent_key'), 'END')  
     


if __name__ == '__main__':
    unittest.main()

