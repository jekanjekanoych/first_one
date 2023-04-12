from urllib.parse import urlsplit, parse_qs
from http.cookies import SimpleCookie


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


def parse_cookie(query: str) -> dict:
    try:
        a = query
        cookie = SimpleCookie()
        cookie.load(a)
        cookies = {k: v.value for k, v in cookie.items()}
        print(cookies)
        return cookies

    except AttributeError:
        return "must be a string"


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('/') == {}
    assert parse_cookie('devicePixelRatio=1;') == {'devicePixelRatio': '1'}
    assert parse_cookie('__utmc=13103656942;') == {'__utmc': '13103656942'}
    assert parse_cookie('__utmz=13105942.1.1.1.utmcsr=google|utmccn=(organic);') == \
           {'__utmz': '13105942.1.1.1.utmcsr=google|utmccn=(organic)'}
    assert parse({'b': -2}) == 'must be a string'
    assert parse((3, 2, 1)) == 'must be a string'
