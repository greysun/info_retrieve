# import sys
# sys.path.append('../..')
from GoldenRetriever.src.utils import clean_txt

def test_clean_txt():
    assert clean_txt(['this\nand that.. '])==['this. and that.']