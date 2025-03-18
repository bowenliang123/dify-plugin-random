from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage
from sympy import randprime


class RandomPrimeTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        lower_bound = tool_parameters.get("lower_bound", 0)
        upper_bound = tool_parameters.get("upper_bound", 1024)

        lower_num = int(lower_bound)
        upper_num = int(upper_bound)
        if lower_num > upper_num:
            raise ValueError(f"Invalid range [{lower_bound}, {upper_bound}],"
                             f" the lower bound should be less than or equal to the upper bound")

        try:
            random_prime = randprime(lower_num, upper_num)
        except ValueError:
            random_prime = None

        # NaN represents no prime number found according to IEEE_754 standard
        random_prime_str = str(random_prime) if random_prime else 'NaN'
        yield self.create_text_message(random_prime_str)
