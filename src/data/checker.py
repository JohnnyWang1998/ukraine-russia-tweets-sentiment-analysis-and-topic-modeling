import pandas as pd
from typing import List


def check_missing_value(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    Count missing values in specified columns.
    @param df: dataframe
    @param cols: columns to be calculated
    return: summary information
    """
    res = pd.DataFrame(cols, columns=['Feature'])
    na_cnts = [sum(df[col].isna()) for col in cols]
    res['NA Count'] = na_cnts
    res['NA Rate'] = res['NA Count'] / df.shape[0]
    res = res[res['NA Count'] != 0]
    res = res.sort_values(
        by='NA Count', ascending=False).reset_index(drop=True)
    return res


def check_zeros(df: pd.DataFrame, cols: List[str]) -> pd.DataFrame:
    """
    Count specified values in specified columns.
    @param df: dataframe
    @param cols: columns to be calculated
    return: summary information
    """
    res = pd.DataFrame(cols, columns=['Feature'])
    na_cnts = [sum(df[col] == 0) for col in cols]
    res['Value Count'] = na_cnts
    res['Rate'] = res['Value Count'] / df.shape[0]
    res = res[res['Value Count'] != 0]
    res = res.sort_values(
        by='Value Count', ascending=False).reset_index(drop=True)
    return res
