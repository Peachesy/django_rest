import unittest
import requests

class UserTest(unittest.TestCase):
    '''用户查询测试'''
    def setUp(self) :
        self.base_url = 'http://127.0.0.1:8000/users'
        self.auth = ('admin', 'admin123456')

    def test_user1(self):
        ''' test user admin '''
        r = requests.get(self.base_url+'/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'admin')
        self.assertEqual(result['email'], 'admin@mail.com')

    def test_user2(self):
        ''' test user tom '''
        r = requests.get(self.base_url+'/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'Tom')
        self.assertEqual(result['email'], 'tom@mail.com')

    def test_user3(self):
        ''' test user tom '''
        r = requests.get(self.base_url+'/3/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['username'], 'Jack')
        self.assertEqual(result['email'], 'jack@mail.com')

class GroupsTest(unittest.TestCase):
    '''用户组查询测试'''
    def setUp(self) :
        self.base_url = 'http://127.0.0.1:8000/groups'
        self.auth = ('admin', 'admin123456')

    def test_groups1(self):
        '''test group test'''
        r = requests.get(self.base_url+'/1/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'],'test')

    def test_groups2(self):
        '''test group test'''
        r = requests.get(self.base_url+'/2/', auth=self.auth)
        result = r.json()
        self.assertEqual(result['name'],'developer')

if __name__ == '__main__':
    unittest.main()



