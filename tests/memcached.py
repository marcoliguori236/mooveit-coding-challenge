# error message to be asserted against output of memcached commands
err_msg = "CLIENT_ERROR bad data chunk \n ERROR"

'''Class built with the intention of simulating a real Memcached system'''

class Memcached:

    def __init__(self):
        self.storage = dict()

    """Function to handle string byte size"""
    def utf8len(self, s):
        return len(s.encode('utf-8'))    

    """Storage Commands"""    
    def set(self, key, value, byte):
        if byte == self.utf8len(value):
            self.storage[key] = value
            print("STORED")
        else:
            print(err_msg)
            return(err_msg)

    def add(self,key,value, byte):
        if key in self.storage or byte != self.utf8len(value):
            print(err_msg)
            return err_msg
        else:
            self.storage[key] = value
            print("STORED")

    def replace(self, key, value, byte):
        if key in self.storage and byte == self.utf8len(value):
            self.storage[key] = value
            print('STORED')
            return value
        else:
            print(err_msg)
            return err_msg
        

    def append(self, key, value, byte):
        if key in self.storage and byte == self.utf8len(value):
            self.storage[key] += value
            value = self.storage[key]
            print('STORED')
            return value
        else:
            return err_msg
            print(err_msg)    

    def prepend(self, key, value, byte):
        if key in self.storage and byte == self.utf8len(value):
            self.storage[key] = value + self.storage[key]   
            value = self.storage[key]
            print('STORED')  
            return value 
        else:    
            print(err_msg)
            return err_msg

    """cas command is not supported for practical reasons"""        

    """Retrieval Commands"""
    def get(self, key):
        if key in self.storage:
            value = self.storage[key]
            response = f'VALUE {key} \n {value} \n END'
            print(response)
            return value
        else:
            return 'END'    
