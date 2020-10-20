import unittest
# import json
# from flask import request, jsonify
from myservice import app

app.testing = True

# TODO: Extend these component tests for the calc view
#       and THEN implement all 4 operations!
# DO NOT REMOVE EXISTING TESTS!


class TestCalc(unittest.TestCase):

    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=3&n=5').get_json()
        self.assertEqual(reply['result'], '8')

    def test_add_integers_positive(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=1&n=2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_add_integers_negative(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=-1&n=-2').get_json()
        self.assertEqual(reply['result'], '-3')

    # --------------------------------------------
    # from here
    def test_add_integers_pos_neg(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=1&n=-2').get_json()
        self.assertEqual(reply['result'], '-1')

    def test_add_integers_neg_pos(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/sum?m=-1&n=2').get_json()
        self.assertEqual(reply['result'], '1')
    # --------------------------------------------

    def test_div1(self):
        tested_app = app.test_client()
        self.assertRaises(ZeroDivisionError, tested_app.get, '/calc/div?m=3&n=0')

    def test_divide_integers_positive(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=6&n=3').get_json()
        self.assertEqual(reply['result'], '2')

    def test_divide_integers_positive2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=7&n=3').get_json()
        self.assertEqual(reply['result'], '2')

    def test_divide_integers_negative(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=-6&n=-2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_divide_integers_negative2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=-7&n=-2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_divide_integers_pos_neg(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=6&n=-2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_divide_integers_pos_neg2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=9&n=-2').get_json()
        self.assertEqual(reply['result'], '-4')

    def test_divide_integers_neg_pos(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=-6&n=2').get_json()
        self.assertEqual(reply['result'], '-3')

    def test_divide_integers_neg_pos2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/div?m=-7&n=2').get_json()
        self.assertEqual(reply['result'], '-3')
    # --------------------------------------------

    def test_multiply_integers_positive(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=6&n=3').get_json()
        self.assertEqual(reply['result'], '18')

    def test_multiply_integers_positive2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=7&n=3').get_json()
        self.assertEqual(reply['result'], '21')

    def test_multiply_integers_negative(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-6&n=-2').get_json()
        self.assertEqual(reply['result'], '12')

    def test_multiply_integers_negative2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-7&n=-2').get_json()
        self.assertEqual(reply['result'], '14')

    def test_multiply_integers_pos_neg(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=6&n=-2').get_json()
        self.assertEqual(reply['result'], '-12')

    def test_multiply_integers_pos_neg2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=9&n=-2').get_json()
        self.assertEqual(reply['result'], '-18')

    def test_multiply_integers_neg_pos(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-6&n=2').get_json()
        self.assertEqual(reply['result'], '-12')

    def test_multiply_integers_neg_pos2(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=-7&n=2').get_json()
        self.assertEqual(reply['result'], '-14')

    def test_multiply_zero(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/multiply?m=0&n=2').get_json()
        self.assertEqual(reply['result'], '0')
    # --------------------------------------------

    def test_subtract_integers_positive(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/subtract?m=1&n=2').get_json()
        self.assertEqual(reply['result'], '-1')

    def test_subtract_integers_negative(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/subtract?m=-1&n=-2').get_json()
        self.assertEqual(reply['result'], '1')

    def test_subtract_integers_pos_neg(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/subtract?m=1&n=-2').get_json()
        self.assertEqual(reply['result'], '3')

    def test_subtract_integers_neg_pos(self):
        tested_app = app.test_client()
        reply = tested_app.get('/calc/subtract?m=-1&n=2').get_json()
        self.assertEqual(reply['result'], '-3')
