import sys
from datetime import date, datetime
from typing import Any, Optional, SupportsFloat, Union

if sys.version_info < (3, 9):
    from typing import List, MutableMapping, Sequence, Tuple
else:
    from builtins import list as List, tuple as Tuple
    from collections.abc import MutableMapping, Sequence

if sys.version_info < (3, 10):
    from typing_extensions import TypeAlias
else:
    from typing import TypeAlias

if sys.version_info < (3, 11):
    from typing_extensions import Self
else:
    from typing import Self

CMR_OPS: str
CMR_UAT: str
CMR_SIT: str

FloatLike: TypeAlias = Union[str, SupportsFloat]
PointLike: TypeAlias = Tuple[FloatLike, FloatLike]

class Query:
    params: MutableMapping[str, Any]
    options: MutableMapping[str, Any]
    concept_id_chars: Sequence[str]
    headers: MutableMapping[str, str]

    def __init__(self, route: str, mode: str = ...) -> None: ...
    def _build_url(self) -> str: ...
    def get(self, limit: int = ...) -> List[Any]: ...
    def hits(self) -> int: ...
    def get_all(self) -> List[Any]: ...
    def parameters(self, **kwargs: Any) -> Self: ...
    def format(self, output_format: str = "json") -> Self: ...
    def concept_id(self, ids: Sequence[str]) -> Self: ...
    def provider(self, provider: str) -> Self: ...
    def mode(self, mode: str = ...) -> None: ...
    def token(self, token: str) -> Self: ...
    def bearer_token(self, bearer_token: str) -> Self: ...

class GranuleCollectionBaseQuery(Query):
    def online_only(self, online_only: bool = True) -> Self: ...
    def temporal(
        self,
        date_from: Optional[Union[str, date, datetime]],
        date_to: Optional[Union[str, date, datetime]],
        exclude_boundary: bool = False,
    ) -> Self: ...
    def short_name(self, short_name: str) -> Self: ...
    def version(self, version: str) -> Self: ...
    def point(self, lon: FloatLike, lat: FloatLike) -> Self: ...
    def circle(self, lon: FloatLike, lat: FloatLike, dist: FloatLike) -> Self: ...
    def polygon(self, coordinates: Sequence[PointLike]) -> Self: ...
    def bounding_box(
        self,
        lower_left_lon: FloatLike,
        lower_left_lat: FloatLike,
        upper_right_lon: FloatLike,
        upper_right_lat: FloatLike,
    ) -> Self: ...
    def line(self, coordinates: Sequence[PointLike]) -> Self: ...
    def downloadable(self, downloadable: bool = True) -> Self: ...
    def entry_title(self, entry_title: str) -> Self: ...

class GranuleQuery(GranuleCollectionBaseQuery):
    def __init__(self, mode: str = ...) -> None: ...
    def orbit_number(
        self,
        orbit1: FloatLike,
        orbit2: Optional[FloatLike] = ...,
    ) -> Self: ...
    def day_night_flag(self, day_night_flag: str) -> Self: ...
    def cloud_cover(
        self,
        min_cover: Optional[FloatLike] = ...,
        max_cover: Optional[FloatLike] = ...,
    ) -> Self: ...
    def instrument(self, instrument: str) -> Self: ...
    def platform(self, platform: str) -> Self: ...
    def sort_key(self, sort_key: str) -> Self: ...
    def granule_ur(self, granule_ur: str) -> Self: ...

class CollectionQuery(GranuleCollectionBaseQuery):
    def __init__(self, mode: str = ...) -> None: ...
    def archive_center(self, center: str) -> Self: ...
    def keyword(self, text: str) -> Self: ...
    def native_id(self, native_ids: Sequence[str]) -> Self: ...
    def tool_concept_id(self, ids: Sequence[str]) -> Self: ...
    def service_concept_id(self, ids: Sequence[str]) -> Self: ...

class ToolServiceVariableBaseQuery(Query):
    def native_id(self, native_ids: Sequence[str]) -> Self: ...
    def name(self, name: str) -> Self: ...

class ToolQuery(ToolServiceVariableBaseQuery):
    def __init__(self, mode: str = ...) -> None: ...

class ServiceQuery(ToolServiceVariableBaseQuery):
    def __init__(self, mode: str = ...) -> None: ...

class VariableQuery(ToolServiceVariableBaseQuery):
    def __init__(self, mode: str = ...) -> None: ...
