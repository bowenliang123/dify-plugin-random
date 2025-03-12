import random
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomNumTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        lower_bound = tool_parameters.get("lower_bound", 0)
        upper_bound = tool_parameters.get("upper_bound", 1024)
        digits = int(tool_parameters.get("digits", 0))

        if digits < 0:
            raise ValueError("Invalid digits")
        elif digits == 0:
            random_num = random.randint(int(lower_bound), int(upper_bound))
        else:
            random_num = round(random.uniform(float(lower_bound), float(upper_bound)), digits)
        yield self.create_text_message(str(random_num))
