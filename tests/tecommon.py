"""
Common things for rectangify tests
"""
from pathlib  import Path

from rectangify import rectangify

INP_TOP = Path('tests/input')
EXP_TOP = Path('tests/expected')

def make_path_triple(inp_name, out_dirp):
    """Create a 3-tuple of file paths input, expected, output"""
    inp_path = INP_TOP / inp_name
    out_name = Path(inp_name).with_suffix('.csv')
    exp_path = (EXP_TOP / out_name)
    out_path = out_dirp / out_name
    return (inp_path, exp_path, out_path)

def assert_files(fp_result, fp_expected):
    """Asserts that two files are the same"""
    result_txt = fp_result.read_text() 
    expected_txt = fp_expected.read_text()
    assert result_txt == expected_txt

def run_rect_and_assert(inp_name, out_dirp, *rect_args, **rect_kwargs):
    (inpp, expp, outp) = make_path_triple(inp_name, out_dirp)
    rectangify.rectangify(inpp, out=outp, *rect_args, **rect_kwargs)
    assert_files(outp, expp)
    



