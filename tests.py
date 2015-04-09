"""Tests for txmandrill-api class."""

from mock import patch, Mock

from twisted.trial import unittest
from twisted.internet.defer import inlineCallbacks, succeed
from mandrill import ValidationError

from txmandrill import TXMandrill


class TXMandrillTest(unittest.TestCase):

    """Test the txmandrill base class returns a deferred when called."""

    @patch('txmandrill.treq')
    @inlineCallbacks
    def test_call(self, treq_mock):
        """A call to a Mandrill API endpoint will return a deferred."""
        response_mock = Mock()
        response_mock.json.return_value = {'some': 'response'}
        response_mock.code = 200
        treq_mock.post.return_value = succeed(response_mock)
        m = TXMandrill('nah')
        result = yield m.users.info()
        self.assertEquals(result, {'some': 'response'})

    @patch('txmandrill.treq')
    @inlineCallbacks
    def test_failure(self, treq_mock):
        """An error HTTP response will raise an exception."""
        response_mock = Mock()
        response_mock.json.return_value = {
            'name': 'ValidationError',
            'status': 'error', 'message': 'Validation failed.'}
        response_mock.code = 404
        treq_mock.post.return_value = succeed(response_mock)
        m = TXMandrill('nah')
        yield self.assertFailure(m.users.info(), ValidationError)
