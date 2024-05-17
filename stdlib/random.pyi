import _random
import sys
from _typeshed import SupportsLenAndGetItem
from collections.abc import Callable, Iterable, MutableSequence, Sequence, Set as AbstractSet
from fractions import Fraction
from typing import Any, ClassVar, NoReturn, TypeVar

__all__ = [
    "Random",
    "seed",
    "random",
    "uniform",
    "randint",
    "choice",
    "sample",
    "randrange",
    "shuffle",
    "normalvariate",
    "lognormvariate",
    "expovariate",
    "vonmisesvariate",
    "gammavariate",
    "triangular",
    "gauss",
    "betavariate",
    "paretovariate",
    "weibullvariate",
    "getstate",
    "setstate",
    "getrandbits",
    "choices",
    "SystemRandom",
]

if sys.version_info >= (3, 9):
    __all__ += ["randbytes"]
if sys.version_info >= (3, 12):
    __all__ += ["binomialvariate"]

_T = TypeVar("_T")

class Random(_random.Random):
    VERSION: ClassVar[int]
    if sys.version_info >= (3, 9):
        def __init__(self, x: int | float | str | bytes | bytearray | None = None) -> None: ...
    else:
        def __init__(self, x: Any = None) -> None: ...
    # Using other `seed` types is deprecated since 3.9 and removed in 3.11
    # Ignore Y041, since random.seed doesn't treat int like a float subtype. Having an explicit
    # int better documents conventional usage of random.seed.
    if sys.version_info >= (3, 9):
        def seed(self, a: int | float | str | bytes | bytearray | None = None, version: int = 2) -> None: ...  # type: ignore[override]  # noqa: Y041
    else:
        def seed(self, a: Any = None, version: int = 2) -> None: ...

    def getstate(self) -> tuple[Any, ...]: ...
    def setstate(self, state: tuple[Any, ...]) -> None: ...
    def randrange(self, start: int, stop: int | None = None, step: int = 1) -> int: ...
    def randint(self, a: int, b: int) -> int: ...
    if sys.version_info >= (3, 9):
        def randbytes(self, n: int) -> bytes: ...

    def choice(self, seq: SupportsLenAndGetItem[_T]) -> _T: ...
    def choices(
        self,
        population: SupportsLenAndGetItem[_T],
        weights: Sequence[float | Fraction] | None = None,
        *,
        cum_weights: Sequence[float | Fraction] | None = None,
        k: int = 1,
    ) -> list[_T]: ...
    if sys.version_info >= (3, 11):
        def shuffle(self, x: MutableSequence[Any]) -> None: ...
    else:
        def shuffle(self, x: MutableSequence[Any], random: Callable[[], float] | None = None) -> None: ...
    if sys.version_info >= (3, 11):
        def sample(self, population: Sequence[_T], k: int, *, counts: Iterable[int] | None = None) -> list[_T]: ...
    elif sys.version_info >= (3, 9):
        def sample(
            self, population: Sequence[_T] | AbstractSet[_T], k: int, *, counts: Iterable[int] | None = None
        ) -> list[_T]: ...
    else:
        def sample(self, population: Sequence[_T] | AbstractSet[_T], k: int) -> list[_T]: ...

    def uniform(self, a: float, b: float) -> float: ...
    def triangular(self, low: float = 0.0, high: float = 1.0, mode: float | None = None) -> float: ...
    if sys.version_info >= (3, 12):
        def binomialvariate(self, n: int = 1, p: float = 0.5) -> int: ...

    def betavariate(self, alpha: float, beta: float) -> float: ...
    if sys.version_info >= (3, 12):
        def expovariate(self, lambd: float = 1.0) -> float: ...
    else:
        def expovariate(self, lambd: float) -> float: ...

    def gammavariate(self, alpha: float, beta: float) -> float: ...
    if sys.version_info >= (3, 11):
        def gauss(self, mu: float = 0.0, sigma: float = 1.0) -> float: ...
        def normalvariate(self, mu: float = 0.0, sigma: float = 1.0) -> float: ...
    else:
        def gauss(self, mu: float, sigma: float) -> float: ...
        def normalvariate(self, mu: float, sigma: float) -> float: ...

    def lognormvariate(self, mu: float, sigma: float) -> float: ...
    def vonmisesvariate(self, mu: float, kappa: float) -> float: ...
    def paretovariate(self, alpha: float) -> float: ...
    def weibullvariate(self, alpha: float, beta: float) -> float: ...

# SystemRandom is not implemented for all OS's; good on Windows & Linux
class SystemRandom(Random):
    def getrandbits(self, k: int) -> int: ...  # k can be passed by keyword
    def getstate(self, *args: Any, **kwds: Any) -> NoReturn: ...
    def setstate(self, *args: Any, **kwds: Any) -> NoReturn: ...

_inst: Random
seed = _inst.seed
random = _inst.random
uniform = _inst.uniform
triangular = _inst.triangular
randint = _inst.randint
choice = _inst.choice
randrange = _inst.randrange
sample = _inst.sample
shuffle = _inst.shuffle
choices = _inst.choices
normalvariate = _inst.normalvariate
lognormvariate = _inst.lognormvariate
expovariate = _inst.expovariate
vonmisesvariate = _inst.vonmisesvariate
gammavariate = _inst.gammavariate
gauss = _inst.gauss
if sys.version_info >= (3, 12):
    binomialvariate = _inst.binomialvariate
betavariate = _inst.betavariate
paretovariate = _inst.paretovariate
weibullvariate = _inst.weibullvariate
getstate = _inst.getstate
setstate = _inst.setstate
getrandbits = _inst.getrandbits
if sys.version_info >= (3, 9):
    randbytes = _inst.randbytes
