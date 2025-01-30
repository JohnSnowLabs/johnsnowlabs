from pydantic import BaseConfig, BaseModel

from johnsnowlabs import settings
from johnsnowlabs.abstract_base.base_enum import BaseEnum
from johnsnowlabs.py_models.lib_version import LibVersion
from johnsnowlabs.utils.enums import ProductName

BaseConfig.json_encoders = {
    LibVersion: lambda v: v.as_str(),
    ProductName: lambda x: x.value,
    BaseEnum: lambda x: x.value,
}


class WritableBaseModel(BaseModel):
    def write(self, path, *args, **kwargs):
        with open(path, "w", encoding="utf8") as json_file:
            if "indent" not in kwargs:
                kwargs["indent"] = settings.json_indent
            json_file.write(self.model_dump_json(*args, **kwargs))

    class Config:
        arbitrary_types_allowed = True
