import random
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        upper_bound = int(tool_parameters.get("upper_bound", 0))
        lower_bound = int(tool_parameters.get("lower_bound", 1024))
        random_num = random.randint(upper_bound, lower_bound)
        yield self.create_text_message(str(random_num))
