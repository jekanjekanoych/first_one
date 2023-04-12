from urllib.parse import urlsplit, parse_qs


def parse(query: str) -> dict:

    try:
        query = urlsplit(query).query
        params = parse_qs(query)
        print(params)
        return {k: v[0] for k, v in params.items()}

    except AttributeError:
        return "must be a string"


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Дима') == {'name': 'Дима'}
    assert parse('http://example.com/?status=студент') == {'status': 'студент'}
    assert parse('https://example.com/path/to/page?group=101&course=1') == {'group': '101', 'course': '1'}
    assert parse({'a': 1}) == 'must be a string'
    assert parse((1, 2, 3)) == 'must be a string'



