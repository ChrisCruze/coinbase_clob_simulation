import unittest
import data_load
from clob_sync import CLOBSync

class TestCBSACalc(unittest.TestCase):
	initial_clob,final_clob,messages_data_filtered = data_load.data_load()
	updated_clob = CLOBSync().clob_sync(initial_clob,final_clob,messages_data_filtered)

	def test_bids_equal(self):
		initial_bids = len(final_clob['bids'])
		initial_bids = len(final_clob['bids'])
		self.assertEqual(csv_load.dict_create_from_list_keys(['1','2'],['a','b']),{'a':'1','b':'2'})

if __name__ == '__main__':
    unittest.main()