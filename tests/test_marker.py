from tests import tecommon as tcn


def test_flights_cols_defaultmode(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols.txt', tmp_path)

def test_flights_cols(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols.txt', tmp_path,
        convert='COLS')

def test_flights_cols_no_truncate(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_preambled.txt', tmp_path,
        convert='COLS')

def test_flights_cols_truncate(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_preambled.txt', tmp_path,
        convert='COLS', truncate_before=True)

def test_food_rows(tmp_path):    
    tcn.run_rect_and_assert(
        'food_rows.txt', tmp_path, 
        convert='ROWS')
