import unittest
from flask import current_app
from app import create_app

class TestApp(unittest.TestCase):

  def setUp(self):
    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()

  def tearDown(self):
    self.app_context.pop()

  def test_app(self):
    self.assertIsNone(current_app) #Testea si hay conexión

if __name__ == '__main__':
  unittest.main()
