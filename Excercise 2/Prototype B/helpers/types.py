from dataclasses import dataclass, field
from typing import Optional, NewType, Union, Any

TagList = NewType('TagList', list[str])

@dataclass
class Grain:
    '''
    A dataclass describing a primary key in the dataset


    Attributes
    ----------
    id : str
        A unique identifier of the grain.
    source_column : str
        A column name in the physical database. Optional, equals to id by default.
    title : str
        A human readable title of the grain. Optional, derived from id if not provided explicitly.
    description : str
        An optional description of the grain.
    tags : TagList
        A list of strings - metadata tags for this grain.
    '''
    id: str
    source_column: Optional[str]
    title: Optional[str]
    description: Optional[str]
    tags: Optional[TagList]

@dataclass
class Fact:
    '''
    A dataclass describing a single fact in the dataset


    Attributes
    ----------
    id : str
        A unique identifier of the fact.
    source_column : str
        A column name in the physical database. Optional, equals to id by default.
    title : str
        A human readable title of the fact. Optional, derived from id if not provided explicitly.
    description : str
        An optional description of the fact.
    tags : TagList
        A list of strings - metadata tags for this fact.
    '''
    id: str
    title: Optional[str]
    description: Optional[str]
    tags: Optional[TagList]
    source_column: Optional[str]

@dataclass
class Dimension:
    '''
    A dataclass describing a single dimension in the dataset


    Attributes
    ----------
    id : str
        A unique identifier of the dimension.
    source_column : str
        A column name in the physical database. Optional, equals to id by default.
    title : str
        A human readable title of the dimension. Optional, derived from id if not provided explicitly.
    description : str
        An optional description of the dimension.
    tags : TagList
        A list of strings - metadata tags for this dimension.
    '''
    id: str
    source_column: Optional[str]
    title: Optional[str]
    description: Optional[str]
    tags: Optional[TagList]

@dataclass
class Join:
    '''
    A dataclass describing a 1-N join between dimensions.

    Foreign dataset is defined in "dataset" attribute and will always be joined by it's grain.
    Current dataset will be join by the column name defined in "using" attribute.

    Attributes
    ----------
    dataset : Dataset | str
        Either a reference to the Dataset object or a dataset id to join to.
    using : str
        A name of the source column in the physical database for the current dataset.
    '''
    dataset: Union['Dataset', str]
    using: Union[list[str], str]

@dataclass
class JoinMtoN:
    '''
    A dataclass describing a M-N join between dimensions.

    Foreign dataset is defined in "dataset" attribute and will always be joined by it's grain.
    Current dataset will be join by the column name defined in "using" attribute.

    Attributes
    ----------
    dataset : Dataset | str
        Either a reference to the Dataset object or a dataset id to join to.
    using : str
        A name of the source column in the physical database for the current dataset.
    '''
    dataset: Union['Dataset', str]
    using: Union[list[str], str]

@dataclass
class Dataset:
    '''
    Declarative definition for the dataset


    Attributes
    ----------
    id : str
        A unique identifier of the dataset.
    data_source : str
        A data source of the dataset in format "<data_source_id>.<table_name>", for example "my_datasource.my_table".
    grain : str
        A primary key for the given dataset.
    title : str
        An optional human readable title for the dataset. Will be derived from id if not provided explicitly.
    description : str
        An optional description of the dataset.
    tags : TagList
        A list of strings - metadata tags of this dataset.
    fields : list
        A list of Facts and Dimensions in the dataset.
    joins : list
        A list of Join or JoinMtoN, specifies the relations between datasets.
    '''
    id: str
    data_source: str
    grain: Grain
    title: Optional[str]
    description: Optional[str]
    tags: Optional[TagList]
    fields: list[Union[Dimension, Fact]]
    joins: Optional[list[Union[Join, MultiJoin]]]
