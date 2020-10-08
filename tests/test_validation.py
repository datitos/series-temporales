import sys
sys.path.append('../')

import unittest
import pandas as pd
from backtesting.validation import *


class cv_cutoffs(unittest.TestCase):
    step_size = pd.Timedelta('3D')
    steps = 5
    first_val_day = pd.Timestamp('2020-02-01')
    execution_date = pd.Timestamp('2020-04-15 23:00:00')
    window_size = pd.Timedelta('5D')
    expected_cutoffs = [pd.Timestamp('2020-03-29 23:00:00'),
                        pd.Timestamp('2020-04-01 23:00:00'),
                        pd.Timestamp('2020-04-04 23:00:00'),
                        pd.Timestamp('2020-04-07 23:00:00'),
                        pd.Timestamp('2020-04-10 23:00:00')] 
    cutoffs = cv_cutoffs(execution_date, steps, window_size, step_size)

    def test_cv_cutoffs(self):
        self.assertEqual(len(self.expected_cutoffs), len(self.cutoffs), msg='The sizes of the list does not match')
        self.assertListEqual(self.cutoffs, self.expected_cutoffs, msg= 'The lists do not contain the sames items' )
        

