
import pytest
from gene_finder import read_data, clean_data, \
    create_lookup, find_gene

# just using the sample data as the mock since
# I don't have any other
path_to_mock_vcf = "input_tiny.vcf"


# Fixture to save time - a little uneccesary but maybe
# useful if we were going to write some more tests
@pytest.fixture()
def mock_data():
    lines = read_data(path_to_mock_vcf)
    data = clean_data(lines)
    lookup_table = create_lookup(data)
    return {'lines': lines, 'data': data, \
        'lookup_table': lookup_table}


def test_read_data_outputs_list_of_strings():
    """Reading the vcf should return a list of strings"""

    lines = read_data(path_to_mock_vcf)

    assert type(lines[1]) == str

def test_clean_data_returns_10_columns(mock_data):
    """Assuming vcfs of genes always have 10 columns
    for now..."""

    lines = mock_data['lines']
    data = clean_data(lines)

    assert len(data[0]) == 10

def test_create_lookup_returns_a_dictionary(mock_data):
    """Should return a dict with the same number of keys
    as the data had rows"""

    data = mock_data['data']
    lookup_table = create_lookup(data)

    assert len(lookup_table.keys()) == len(data)

def test_find_gene_returns_a_valid_nucleobase(mock_data):
    """Should only return A, C, T or G"""

    lookup_table = mock_data['lookup_table']
    find_gene('chr1', '10001', lookup_table) == \
        any(['A', 'C', 'T', 'G'])




