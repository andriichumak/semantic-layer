from dataclasses import dataclass, field
from typing import Optional, NewType, Union, Any

TagList = NewType('TagList', list[str])

@dataclass
class Dimension:
    id: str
    title: Optional[str]
    tags: Optional[TagList]
    source_column: Optional[str]

@dataclass
class Grain(Dimension):
    pass

@dataclass
class Fact:
    id: str

@dataclass
class Join:
    dataset: Union['Dataset', str]
    using: Union[list[str], str]

@dataclass
class MultiJoin(Join):
    pass

@dataclass
class Dataset:
    id: str
    data_source: str
    title: Optional[str]
    tags: Optional[TagList]
    fields: list[Union[Dimension, Fact]]
    joins: list[Union[Join, MultiJoin]]
