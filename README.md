# txmandrill-api

[![Build Status](https://travis-ci.org/lextoumbourou/txmandrill-api.svg?branch=master)](https://travis-ci.org/lextoumbourou/txmandrill-api)
[![Coverage Status](https://coveralls.io/repos/lextoumbourou/txmandrill-api/badge.svg)](https://coveralls.io/r/lextoumbourou/txmandrill-api)
[![Latest Version](https://img.shields.io/pypi/v/txmandrill.svg)](https://pypi.python.org/pypi/txmandrill/)

*The Mandrill Python client but for [Twisted](https://twistedmatrix.com/trac/).*

<img src="https://farm6.staticflickr.com/5260/5495737139_e2bddaf1d5_m_d.jpg">
<br>
*[Mandrill - Oregon Zoo (Kathy & Sam)](https://www.flickr.com/photos/39871249@N07/5495737139/in/photostream/)*

## Installation

```bash
> pip install txmandrill
```

## Usage

Exactly the same as the [mandrill-api-python](https://mandrillapp.com/api/docs/index.python.html) library, 'cept every method returns a [Deferred](http://twistedmatrix.com/documents/current/core/howto/defer-intro.html). Simple as.

## Example

```python
from pprint import pprint

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from txmandrill import TXMandrill


@inlineCallbacks
def ping_and_get_users():
    mandrill_client = TXMandrill('YOUR_API_KEY')

    # Ping
    result = yield mandrill_client.users.ping()
    pprint(result)

    # Return the information about the API-connected user
    result = yield mandrill_client.users.info()
    pprint(result)


if __name__ == "__main__":
    df = ping_and_get_users()
    df.addErrback(lambda err: err.printTraceback())
    df.addCallback(lambda _: reactor.stop())
    reactor.run()
```

## License

Apache (as per original project).
