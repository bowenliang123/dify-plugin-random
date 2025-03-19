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

        lower_num: float | int = float(lower_bound) if digits == 0 else int(lower_bound)
        upper_num: float | int = float(upper_bound) if digits == 0 else int(upper_bound)
        if lower_num > upper_num:
            raise ValueError(f"Invalid range [{lower_bound}, {upper_bound}],"
                             f" the lower bound should be no greater than the upper bound")

        if digits < 0:
            raise ValueError(f"Invalid digits {digits}")

        # Generate random number(s)
        gen_random_int = lambda lower, upper: random.randint(lower, upper)
        gen_random_float = lambda lower, upper: round(random.uniform(lower, upper), digits)
        gen_func = gen_random_int if digits == 0 else gen_random_float
        result_str = separator.join(str(gen_func(lower_num, upper_num)) for _ in range(num_count))

        yield self.create_text_message(result_str)
