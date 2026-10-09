class LibVersionIdentifier(str):
    """Representation of a specific library version"""

    # pydantic 2 demands an exact instance otherwise and rejects plain strings read from json
    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        from pydantic_core import core_schema

        return core_schema.no_info_after_validator_function(
            cls, core_schema.str_schema()
        )


class Secret(str):
    pass
