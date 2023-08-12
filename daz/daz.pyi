def set_ftz() -> None: ...
def set_daz() -> None: ...
def unset_ftz() -> None: ...
def unset_daz() -> None: ...
def get_ftz() -> bool: ...
def get_daz() -> bool: ...

class DAZ:
    def __init__(self, daz: bool = True, ftz: bool = True) -> None: ...
    @staticmethod
    def set_daz(daz: bool | None = True) -> bool: ...
    @staticmethod
    def set_ftz(ftz: bool | None = True) -> bool: ...
    def __enter__(self) -> tuple[bool, bool]: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...