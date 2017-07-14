import unittest
import server
import json


class ServerTest(unittest.TestCase):
    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_get_links(self):
        test_url = 'http://www.ebay.com/itm/Google-Home-Chromecast-Video-2nd-Gen-1080p-Bundle-for-99-99-/222571438996'
        response = self.app.get('/getLinks?itemUrl={0}'.format(test_url))

        data = json.loads(response.data)
        self.assertEqual(len(data), 2)
        self.assertRegex(data['cart'], '^https?:\/\/')
        self.assertRegex(data['buy'], '^https?:\/\/')

    def test_get_promos(self):
        response = self.app.get('/promos')
        data = json.loads(response.data)

        self.assertEqual(len(data['promos']), 4)
        for el in data['promos']:
            self.assertEqual(len(el['keywords']), 2)
            self.assertIn('imageUrl', el)


if __name__ == '__main__':
    unittest.main()
