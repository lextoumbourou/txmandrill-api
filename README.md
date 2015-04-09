# txmandrill-api

[![Build Status](https://travis-ci.org/lextoumbourou/txmandrill-api.svg?branch=master)](https://travis-ci.org/lextoumbourou/txmandrill-api)

The Mandrill Python client but for Twisted.

## Installation

```
> pip install txmandrill
```

## Usage

Exactly the same as the [mandrill-api-python](https://bitbucket.org/mailchimp/mandrill-api-python) library, 'cept every method returns a [deferred](http://twistedmatrix.com/documents/current/core/howto/defer-intro.html). Simple as.

## Example

```
import pprint

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks

from txmandrill import TXMandrill


@inlineCallbacks
def example():
    m = TXMandrill('YOUR_API_KEY')

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
