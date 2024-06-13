from dataclasses import dataclass, replace
from functools import cache
from typing import Self

from beet import Context, Generator

from bolt import Runtime


@dataclass
class ResourceGenerator:
    """Helpful sugar for generating resource locations and paths

    Adds some python data model functions to provide easier access to
      :class:`~beet.Generator` functions.

    - `__truediv__` lets you define paths similar to :class:`~pathlib.Path`
    - `__getattr__` lets you define namespaced paths easily
    - `__neg__` makes it cleaner to convert a :class:`ResourceGenerator` into a string

    ```py
    pack = ctx.inject(ResourceGenerator)
    function (pack / "load"):
        say "Loaded"

    pack.entity == "namespace.entity"

    tick = pack / "tick"

    function_tag minecraft:tick {
        "values": [-(tick)]  # unfortuntely need parens here
    }

    function tick:
        as @r say hi
    ```
    """

    _generator: Generator

    def __init__(self, _generator: Generator | Context):
        match _generator:
            case Generator():
                self._generator = _generator
            case Context():
                self._generator = _generator.generate

    def __truediv__(self, path: str):
        """Allows you to define subpaths based on the root generator"""
        return replace(self, _generator=self._generator[path])

    @cache
    def __getattr__(self, key: str):
        """Produce a namespaced id"""
        return self.__getitem__(key)

    @cache
    def __getitem__(self, key: str):
        """Produce a namespaced id"""
        return self._generator.id(key)

    def __neg__(self):
        """Simplfied sugar for `__str__`"""
        return str(self)

    def __str__(self):
        return self._generator.format("{namespace}:{path}")[:-1]

    def __eq__(self, other: Self):
        return str(self) == str(other)

    def __repr__(self):
        return f"{self.__class__.__name__}({self})"

    def __hash__(self):
        return hash(str(self))


def beet_default(ctx: Context):
    """Adds `ctx.inject(ResourceGenerator)` as `pack` to runtime globals"""
    runtime = ctx.inject(Runtime)
    runtime.globals["pack"] = ctx.inject(ResourceGenerator)
