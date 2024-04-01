import pytest
from tests import tecommon as tcn


def test_flights_cols_defaultmode(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_marked.txt', tmp_path)

def test_flights_cols(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_marked.txt', tmp_path,
        convert='COLS')

def test_flights_cols_first(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_first_marked.txt', tmp_path,
        convert='COLS')

def test_flights_cols_no_truncate(tmp_path):
    with pytest.raises(AssertionError):
        tcn.run_rect_and_assert(
            'flights_cols_preambled.txt', tmp_path,
            convert='COLS')

def test_flights_cols_truncate(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_preambled.txt', tmp_path,
        convert='COLS', truncate_before=True)

def test_food_rows(tmp_path):    
    tcn.run_rect_and_assert(
        'food_rows_marked.txt', tmp_path, 
        convert='ROWS')

def test_f2024_rows_custom_marked(tmp_path):
    tcn.run_rect_and_assert(
        'f2024_custom_marked.txt', tmp_path,
        convert='ROWS', marker="My Marker")

def test_f2024_rows_custom_first_marked(tmp_path):
    tcn.run_rect_and_assert(
        'f2024_custom_first_marked.txt', tmp_path,
        convert='ROWS', marker="My Marker")

def test_f2024_rows_custom_trailing_space_marked(tmp_path):
    tcn.run_rect_and_assert(
        'f2024_custom-with-space_marked.txt', tmp_path,
        convert='ROWS', marker="DEPARTURE: ")





