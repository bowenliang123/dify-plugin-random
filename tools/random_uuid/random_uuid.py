from uuid import uuid4
from uuid_backport import uuid6, uuid7, uuid8
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomUUIDTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        uuid_type = tool_parameters.get("uuid_type", "uuid4")
        uuid_str = self.generate_uuid(uuid_type)
        yield self.create_text_message(uuid_str)

    def generate_uuid(self, uuid_type: str) -> str:
        """
        Generate a random UUID string
        :param uuid_type:
        :return:
        """
        uid = None
        match uuid_type:
            case "uuid4":
                uid = uuid4()
            case "uuid6":
                uid = uuid6()
            case "uuid7":
                uid = uuid7()
            case "uuid8":
                uid = uuid8()
            case _:
                raise ValueError(f"Invalid uuid_type {uuid_type}")

        return str(uid)
