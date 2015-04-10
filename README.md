# txmandrill-api

[![Build Status](https://travis-ci.org/lextoumbourou/txmandrill-api.svg?branch=master)](https://travis-ci.org/lextoumbourou/txmandrill-api)
[![Coverage Status](https://coveralls.io/repos/lextoumbourou/txmandrill-api/badge.svg)](https://coveralls.io/r/lextoumbourou/txmandrill-api)
[![Downloads](https://pypip.in/download/txmandrill/badge.svg)](https://pypi.python.org/pypi/txmandrill/)
[![Latest Version](https://pypip.in/version/txmandrill/badge.svg)](https://pypi.python.org/pypi/txmandrill/)

The Mandrill Python client but for Twisted.

## Installation

```bash
> pip install txmandrill
```

## Usage

Exactly the same as the [mandrill-api-python](https://bitbucket.org/mailchimp/mandrill-api-python) library, 'cept every method returns a [deferred](http://twistedmatrix.com/documents/current/core/howto/defer-intro.html). Simple as.

## Example

```python
import pprint

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from txmandrill import TXMandrill


@inlineCallbacks
def example():
    m = TXMandrill('YOUR_API_KEY')

    # Ping
    result = yield m.users.ping()
    pprint(result)

    # Return the information about the API-connected user
    result = yield m.users.info()
    pprint(result)


if __name__ == "__main__":
    df = example()
    df.addErrback(lambda err: err.printTraceback())
    df.addCallback(lambda _: reactor.stop())
    reactor.run()
```

## License

Apache (as per original project).
