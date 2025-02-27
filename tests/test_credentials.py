import unittest
from alibabacloud_credentials import credentials


class TestCredentials(unittest.TestCase):

    def test_BearerTokenCredential(self):
        bearer_token = 'bearer_token'
        cred = credentials.BearerTokenCredential(bearer_token=bearer_token)
        model = cred.get_credential()
        self.assertEqual('bearer_token', model.bearer_token)
        self.assertEqual('bearer', model.type)

        self.assertEqual('bearer_token', cred.bearer_token)
        self.assertEqual('bearer', cred.credential_type)
