import random
import string
from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class RandomStringTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        length = int(tool_parameters.get("length", 0))
        if not length or length <= 0:
            yield self.create_text_message("")
            return

        include_alphabets = tool_parameters.get("include_alphabets", "upper_and_lower")
        include_numbers = tool_parameters.get("include_numbers", "true").lower()
        include_punctuation = tool_parameters.get("include_punctuation", "false").lower()

        characters = (self.append_alphabets(include_alphabets)
                      + self.append_numbers(include_numbers)
                      + self.append_punctuation(include_punctuation))

        random_string = ''.join(random.choice(characters) for _ in range(length))
        yield self.create_text_message(random_string)

    @staticmethod
    def append_alphabets(include_alphabets: str) -> str:
        match include_alphabets:
            case "upper_and_lower":
                return string.ascii_letters
            case "uppercase_only":
                return string.ascii_uppercase
            case "lowercase_only":
                return string.ascii_lowercase
            case "not_included":
                return ""
            case _:
                return ""

    @staticmethod
    def append_numbers(include_numbers: str) -> str:
        match include_numbers:
            case "true":
                return string.digits
            case _:
                return ""

    @staticmethod
    def append_punctuation(include_punctuation: str) -> str:
        match include_punctuation:
            case "true":
                return string.punctuation
            case _:
                return ""
