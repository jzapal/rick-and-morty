import pytest as pytest

from main import schema


def test_fetching_characters_no_params():
    query = """
            query {
                characters {
                    info {
                      count
                      next
                      prev
                      pages
                    }
                    results {
                      name
                    }
                }
            }
        """
    result = schema.execute_sync(query)
    assert result.errors is None
    assert result.data


def test_characters_pagination():
    query = """
            query {
                characters {
                    info {
                      count
                      next
                      prev
                      pages
                    }
                }
            }
        """
    result = schema.execute_sync(query)
    assert result.errors is None
    assert result.data
    info = result.data['characters']['info']
    assert info == {
        'count': 40,
        'next': 2,
        'prev': None,
        'pages': 4
    }


def test_fetching_nested_records():
    query = """
            query {
                characters {
                    info {
                      count
                    }
                    results {
                      name
                      episode {
                        id
                      }
                    }
                }
            }
        """
    result = schema.execute_sync(query)
    assert result.errors is None
    assert result.data


@pytest.mark.parametrize('characters_filter,results_count', [
    ('{name: "Rick"}', 5),
    ('{name: "rick"}', 5),
    ('{name: "Ri"}', 7),
    ('{name: ""}', 10),
    ('{name: "xxx"}', 0)
])
def test_filtering_characters(characters_filter, results_count):
    query = """
            query {
                characters(filter: %s){
                    info {
                      count
                    }
                    results {
                      name
                      episode {
                        id
                      }
                    }
                }
            }
        """ % characters_filter
    result = schema.execute_sync(query)
    assert result.errors is None
    assert result.data
    assert len(result.data['characters']['results']) == results_count
