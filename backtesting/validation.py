import pandas as pd

def cv_cutoffs(execution_date, steps, window_size, step_size):
    """
    Parameters
    ----------
    execution_date : pd.Timestamp
        Last day of validation.

    steps : int
        Number of folds.

    window_size : pd.Timedelta
        Future horizon of every fold.

    step_size : pd.Timedelta
        Distance between cutoffs.

    Returns
    -------
    cutoffs: list
        List containing cutoff dates
    """
    cutoffs = []
    cutoff = execution_date

    for step in range(steps):
        if step == 0:
            cutoff -= window_size
        else:
            cutoff -= step_size

        cutoffs.append(cutoff)

    return list(reversed(cutoffs))



def cv_cutoffs_v2(first_val_day, steps, step_size):
    """
    Parameters
    ----------
    first_val_day : pd.Timestamp
        First validation day

    steps : int
        Number of folds.

    step_size : pd.Timedelta
        Distance between cutoffs.


    Returns
    -------
    cutoffs: list
        List containing cutoff dates
    """
    cutoffs = [first_val_day]
    cutoff = first_val_day

    if steps == 0:
      return cutoffs

    else:
      for step in range(steps - 1):
          cutoff += step_size
          cutoffs.append(cutoff)

      return cutoffs

def cv_generator(data, cutoffs, window_size):
    """
    Parameters
    ----------
    data : pd.DataFrame
        A DatetimeIndex index is expected.

    cutoffs : iterable of datetime.datetime or pd.Timestamp
        Cutoff dates

    freq: string
        Frequency strings

    window_size : pd.Timedelta
        Future horizon of every fold.

    Returns
    -------
    generator that returns the tuple (train_df, val_df)
    """
    results = {}

    for cutoff in cutoffs:

      train_df = data[:cutoff]
      val_df = data[cutoff:cutoff + window_size]

      yield (train_df, val_df)
