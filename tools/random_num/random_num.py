import decimal
import random
from collections.abc import Generator
from decimal import Decimal
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomNumTool(Tool):
    @staticmethod
    def gen_random_decimal(rand: random.SystemRandom, lower: float, upper: float, digits: int) -> Decimal:
        """
        Generate a random decimal number between lower and upper bounds with specified precision.
        """

        # Setting decimal precision
        decimal.getcontext().prec = digits + 10  # Preserve extra precision for calculations

        # Generate random integer within the scaled range, avoiding floating-point precision issues
        scaled_lower = decimal.Decimal(str(lower)) * (10 ** digits)
        scaled_upper = decimal.Decimal(str(upper)) * (10 ** digits)
        random_int = rand.randint(int(scaled_lower), int(scaled_upper))

        # Convert the random integer to a decimal
        result = decimal.Decimal(random_int) / (10 ** digits)

        # Make sure the decimal has exactly digits decimal places
        return result.quantize(decimal.Decimal(f"1.{'0' * digits}"))

    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        lower_bound = tool_parameters.get("lower_bound")
        upper_bound = tool_parameters.get("upper_bound")
        if lower_bound is None:
            lower_bound = 1
        if upper_bound is None:
            upper_bound = 100
        digits = int(tool_parameters.get("digits") or 0)
        num_count = tool_parameters.get("num_count")
        if num_count is None:
            num_count = 1
        num_count = int(num_count)
        separator = tool_parameters.get("separator") or ","

        if num_count == 0:
            yield self.create_text_message("")
            return
        elif num_count < 0:
            raise ValueError(f"Invalid num_count {num_count}")

        lower_num = float(lower_bound)
        upper_num = float(upper_bound)
        if lower_num > upper_num:
            raise ValueError(f"Invalid range [{lower_bound}, {upper_bound}],"
                             f" the lower bound should be no greater than the upper bound")

        if digits < 0:
            raise ValueError(f"Invalid digits {digits}")

        # Generate random number(s)
        system_random = random.SystemRandom()
        gen_random_int = lambda rand, lower, upper, _: rand.randint(int(lower), int(upper))
        gen_func = gen_random_int if digits == 0 else self.gen_random_decimal
        random_numbers = [gen_func(system_random, lower_num, upper_num, digits) for _ in range(num_count)]

        result_str = separator.join([str(num) for num in random_numbers])
        yield self.create_text_message(result_str)
