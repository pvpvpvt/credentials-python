from alibabacloud_credentials.utils import auth_constant as ac
from alibabacloud_credentials.models import CredentialModel


class Credential:

    def get_credential(self):
        return

    async def get_credential_async(self):
        return


class BearerTokenCredential(Credential):
    """BearerTokenCredential"""

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        self.credential_type = ac.BEARER

    def get_credential(self):
        return CredentialModel(
            bearer_token=self.bearer_token,
            type=ac.BEARER
        )

    async def get_credential_async(self):
        return CredentialModel(
            bearer_token=self.bearer_token,
            type=ac.BEARER
        )
