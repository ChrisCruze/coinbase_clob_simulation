import unittest
import data_load

class TestCBSACalc(unittest.TestCase):
	initial_clob,final_clob,messages_data_filtered = data_load.data_load()
	def test_dict_create_from_list_keys(self):
		self.assertEqual(csv_load.dict_create_from_list_keys(['1','2'],['a','b']),{'a':'1','b':'2'})

initial_clob,final_clob,messages_data_filtered = data_load.data_load()
# if __name__ == '__main__':
#     unittest.main()