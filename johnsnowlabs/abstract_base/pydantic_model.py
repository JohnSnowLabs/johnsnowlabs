from johnsnowlabs import settings

from johnsnowlabs.abstract_base.base_enum import BaseEnum
from johnsnowlabs.utils.enums import ProductName

from johnsnowlabs.py_models.lib_version import LibVersion
from pydantic import BaseConfig, BaseModel

BaseConfig.json_encoders = {
    LibVersion: lambda v: v.as_str(),
    ProductName: lambda x: x.value,
    BaseEnum: lambda x: x.value,
}


class WritableBaseModel(BaseModel):

    def write(self, path, *args, **kwargs):
        with open(path, 'w') as json_file:
            if 'indent' not in kwargs:
                kwargs['indent'] = settings.json_indent
            json_file.write(self.json(*args, **kwargs))

    class Config:
        arbitrary_types_allowed = True
