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

        lower_num = float(lower_bound)
        upper_num = float(upper_bound)
        if lower_num > upper_num:
            raise ValueError("Invalid range, the the lower bound should be less than or equal to the upper bound")

        if digits < 0:
            raise ValueError(f"Invalid digits {digits}")
        elif digits == 0:
            random_num = random.randint(int(lower_num), int(upper_num))
        else:
            random_num = round(random.uniform(lower_num, upper_num), digits)

        yield self.create_text_message(str(random_num))
