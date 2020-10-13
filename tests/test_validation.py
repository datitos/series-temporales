import sys
sys.path.append('../')


import unittest
import pandas as pd
import numpy as np
from backtesting.validation import *

import datetime

date_today = datetime.datetime.now()
idx_day = pd.date_range(date_today, date_today + datetime.timedelta(364), freq='D')
random_df_day = pd.DataFrame(np.random.random(365), index = idx_day)


class TestCvCutoffs(unittest.TestCase):
    # dti = pd.date_range('2018-01-01', periods=3, freq='H')
    step_size = pd.Timedelta('3D')
    steps = 5
    first_val_day = pd.Timestamp('2020-02-01')
    execution_date = pd.Timestamp('2020-04-15 23:00:00')
    future_horizon = pd.Timedelta('5D')
    expected_cutoffs = [pd.Timestamp('2020-03-29 23:00:00'),
                        pd.Timestamp('2020-04-01 23:00:00'),
                        pd.Timestamp('2020-04-04 23:00:00'),
                        pd.Timestamp('2020-04-07 23:00:00'),
                        pd.Timestamp('2020-04-10 23:00:00')]
    expected_cutoffs_v2 = [pd.Timestamp('2020-02-01 00:00:00'),
                            pd.Timestamp('2020-02-04 00:00:00'),
                            pd.Timestamp('2020-02-07 00:00:00'),
                            pd.Timestamp('2020-02-10 00:00:00'),
                            pd.Timestamp('2020-02-13 00:00:00')]
    cutoffs = cv_cutoffs(execution_date, steps, future_horizon, step_size)
    cutoffs_v2 = cv_cutoffs_v2(first_val_day, steps, step_size)

    df = pd.read_csv('../datasets/test_dataset.csv', index_col = 0, parse_dates = True)
    _, train_df, valid_df = next(cv_generator(df, expected_cutoffs, future_horizon))

    # no escribir v2
    # no test one step
    def test_many_steps(self):
        many_steps = 5

        self.assertListEqual(
            cv_cutoffs(
                last_timestamp=pd.Timestamp('2020-10-08'),
                steps=many_steps,
                future_horizon=pd.Timedelta(3, 'D'),
                step_size=pd.Timedelta(5, 'D'),
            ),
            [
                pd.Timestamp('2020-09-15'),
                pd.Timestamp('2020-09-20'),
                pd.Timestamp('2020-09-25'),
                pd.Timestamp('2020-09-30'),
                pd.Timestamp('2020-10-05'),
            ],
            msg = 'Daily cutoff lists differ'
        )

        self.assertListEqual(
            cv_cutoffs(
                last_timestamp=pd.Timestamp('2020-10-08 00:00:00'),
                steps=many_steps,
                future_horizon=pd.Timedelta(3, 'H'),
                step_size=pd.Timedelta(5, 'H'),
            ),
            [
                pd.Timestamp('2020-10-07 01:00:00'),
                pd.Timestamp('2020-10-07 06:00:00'),
                pd.Timestamp('2020-10-07 11:00:00'),
                pd.Timestamp('2020-10-07 16:00:00'),
                pd.Timestamp('2020-10-07 21:00:00'),
            ],
            msg = 'Hourly cutoff lists differ'
        )

        self.assertListEqual(
            cv_cutoffs(
                last_timestamp=pd.Timestamp('2020-10-08 00:00:00'),
                steps=many_steps,
                future_horizon=pd.Timedelta(3, 'W'),
                step_size=pd.Timedelta(2, 'W'),
            ),
            [
                pd.Timestamp('2020-07-23 00:00:00'),
                pd.Timestamp('2020-08-06 00:00:00'),
                pd.Timestamp('2020-08-20 00:00:00'),
                pd.Timestamp('2020-09-03 00:00:00'),
                pd.Timestamp('2020-09-17 00:00:00'),
            ],
            msg = 'Weekly cutoff lists differ'
        )


    #ratio idea
    def test_generator_hour(self):
        self.assertEqual(len(self.train_df), len(self.df[:self.expected_cutoffs[0]]), msg='The sizes of the datasets does not match')
        self.assertEqual(len(self.valid_df), len(self.df[self.expected_cutoffs[0]:self.expected_cutoffs[0] + self.window_size]), msg='The size of the datasets does not match')
