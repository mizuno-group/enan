# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 13:05:34 2019

@author: tadahaya
"""
import unittest
import pandas as pd
import os
import sys
import math

from enan.connect import Connect

class SampleTest(unittest.TestCase):
    CLS_VAL = 'none'

    # called when test class initialization
    @classmethod
    def setUpClass(cls):
        if sys.flags.debug:
            print('> setUpClass method is called.')
        cls.CLS_VAL = '> setUpClass : initialized!'
        if sys.flags.debug:
            print(cls.CLS_VAL)

    # called when test class end
    @classmethod
    def tearDownClass(cls):
        if sys.flags.debug:
            print('> tearDownClass method is called.')
        cls.CLS_VAL = '> tearDownClass : released!'
        if sys.flags.debug:
            print(cls.CLS_VAL)

    # called when a test method runs
    def setUp(self):
        if sys.flags.debug:
            print(os.linesep + '> setUp method is called.')
        self.smpl = Connect()

    # called when a test method ends
    def tearDown(self):
        if sys.flags.debug:
            print(os.linesep + '> tearDown method is called.')

    def _df_checker(self,df):
        if type(df)!=pd.core.frame.DataFrame:
            return False
        elif df.shape[0]==0:
            return False
        else:
            head = df.head(1)
            judge = math.isnan(head.iat[0,0])
            return not judge

    def _sr_checker(self,sr):
        if type(sr)!=pd.core.series.Series:
            return False
        if sr.shape[0]==0:
            return False
        else:
            head = sr.head(1)
            judge = math.isnan(head.iat[0])
            return not judge

    def test_calc(self):
        ### preparation
        ref,obj = self.smpl.generate_test_data()
        self.smpl.fit(ref)

        ### test
        self.assertTrue(self._df_checker(self.smpl.calc(data=obj)))