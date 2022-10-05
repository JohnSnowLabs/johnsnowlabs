from enum import Enum, EnumMeta


class MetaEnum(EnumMeta):

    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True

    def from_name(cls, name):
        return cls._member_map_[name]


class BaseEnum(Enum, metaclass=MetaEnum):
    # Enums extending this will support `in` keyword for values of enums
    pass
