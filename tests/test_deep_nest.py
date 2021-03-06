from unittest import TestCase, skip
from deep_nest.deep_nest import deep_nest
__author__ = 'L. Ruhlen'
__project__ = 'deep_nest'

class TestDeepNest(TestCase):
    def setUp(self):
        basic_dict = {1: {'A': 'value'},
                      2: {'A': {'i': 'value'},
                          'B':'value'
                          },
                      3: {'A': 'value'}
                      }
        self.test_dict = deep_nest(basic_dict)

    def test_get_item(self):
        tmp = self.test_dict[1, 'A']
        self.assertEquals(tmp, 'value')

        tmp = self.test_dict[2, 'A']
        self.assertEquals(tmp, {'i': 'value'})

        tmp = self.test_dict[2]
        self.assertEquals(tmp, {'A': {'i': 'value'}, 'B':'value'} )

    def test_set_item(self):
        self.test_dict[3,'A'] = 'MOOSE'
        tmp = self.test_dict[3,'A']
        self.assertEquals(tmp, 'MOOSE')

    def test_delete_item(self):
        del self.test_dict[2,'A']
        self.assertEquals(self.test_dict[2], {'B': 'value'})

        del self.test_dict[2, 'B', 'NOT A REAL KEY']
        self.assertEquals(self.test_dict[2], {'B': 'value'})

    def test_insert_new_item(self):
        self.test_dict[1, 'B'] = 'TEST_VAL'
        self.assertEquals(self.test_dict[1,'B'], 'TEST_VAL')

        self.test_dict['BRAND NEW KEY', 12, 'RANDOM STRING'] = 93
        self.assertEquals(self.test_dict['BRAND NEW KEY', 12, 'RANDOM STRING'], 93)

        self.test_dict[3, 'A', 'value'] = 20
        self.assertEquals(self.test_dict[3, 'A', 'value'], 20)

    def test_print_ndict(self):
        print(self.test_dict)

    def test_keys(self):
        tmp = self.test_dict.keys()
        self.assertEquals(tmp, set([1,2,3]))

    def test_to_dict(self):
        tmp = self.test_dict.to_dict()
        self.assertIsInstance(tmp, dict)