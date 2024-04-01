from tests import tecommon as tcn


def test_flights_items(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_unmarked.txt', tmp_path,
        items=5)

def test_flights_items_from_end(tmp_path):
    tcn.run_rect_and_assert(
        'flights_cols_unmarked.txt', tmp_path,
        items=5, reverse_count=True)
