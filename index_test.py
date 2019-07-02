import requests
import unittest


class JDIndexTest(unittest.TestCase):
    """京东首页接口测试"""
    def setUp(self):
        self.url = 'https://app.e.uban360.com/purchase/firstPage/getConfigMsg'
        self.cookie = 'appversion=iOS_6.25.1; deviceId=dbf7b0de5de09b78b3247fb3df58b9de; mobile=13353320708; orgId=267944; orgType=1; sysversion=12.3.1; timeStamp=1562027783000; token=970498392706de84d5b59464c13950ec; userId=10101001188077952; username=%E8%94%A1%E6%85%A7%E5%A8%9C'

    def tearDown(self):
        print(self.result)

    def test_get_JD_personal_index_success(self):
        """成功调京东个人版首页"""
        r = requests.get(self.url, params={'type': 2}, headers={'Cookie': self.cookie})
        self.result = r.json()

        self.assertEqual(self.result['code'], 200)
        self.assertTrue(self.result['success'])
        self.assertIn('skuId', self.result['data']['hotGoodsConfig']['stick'][0])

    def test_get_JD_purchase_index_success(self):
        """成功调京东采购版首页"""
        r = requests.get(self.url, params={'type': 4}, headers={'Cookie': self.cookie})
        self.result = r.json()

        self.assertEqual(self.result['code'], 200)
        self.assertTrue(self.result['success'])
        self.assertIn('skuId', self.result['data']['hotGoodsConfig']['stick'][0])

    def test_get_JD_index_token_is_empty(self):
        """调京东首页，报token is empty"""
        r = requests.get(self.url, params={'type': 2})
        self.result = r.json()

        self.assertEqual(self.result['error']['code'], 40008)
        self.assertFalse(self.result['success'])

    def test_get_JD_inedx_type_is_empty(self):
        """无入参type"""
        r = requests.get(self.url, headers={'Cookie': self.cookie})
        self.result = r.json()

        self.assertTrue(self.result['success'])




