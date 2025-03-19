import random
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomNumTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        lower_bound = tool_parameters.get("lower_bound", 0)
        upper_bound = tool_parameters.get("upper_bound", 100)
        digits = int(tool_parameters.get("digits", 0))
        num_count = int(tool_parameters.get("num_count", 1))
        separator = tool_parameters.get("separator", ", ")

        if num_count == 0:
            yield self.create_text_message("")
            return
        elif num_count < 0:
            raise ValueError(f"Invalid num_count {num_count}")

        if not lower_bound:
            raise ValueError("Invalid input lower_bound")
        if not upper_bound:
            raise ValueError("Invalid input upper_bound")

        lower_num = float(lower_bound)
        upper_num = float(upper_bound)
        if lower_num > upper_num:
            raise ValueError(f"Invalid range [{lower_bound}, {upper_bound}],"
                             f" the lower bound should be no greater than the upper bound")

        if digits < 0:
            raise ValueError(f"Invalid digits {digits}")

        # Generate random number(s)
        result_str = separator.join(
            self.generate_random_number(digits, lower_num, upper_num) for _ in range(num_count))

        yield self.create_text_message(result_str)

    @staticmethod
    def generate_random_number(digits: int, lower_num: float, upper_num: float) -> str:
        if digits == 0:
            random_num = random.randint(int(lower_num), int(upper_num))
        else:
            random_num = round(random.uniform(lower_num, upper_num), digits)

        return str(random_num)
