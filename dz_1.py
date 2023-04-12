from http.cookies import SimpleCookie


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
