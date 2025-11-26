from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.random_num.random_num import RandomNumTool
from tools.random_prime.random_prime import RandomPrimeTool
from tools.random_string.random_string import RandomStringTool
from tools.random_uuid.random_uuid import RandomUUIDTool


class RandomProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            for t in [
                RandomNumTool,
                RandomStringTool,
                RandomUUIDTool,
                RandomPrimeTool,
            ]:
                t.from_credentials({})
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
