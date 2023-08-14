
import daz._core as daz_core

class DAZ:
    def __init__(self, daz: bool = True, ftz: bool = True) -> None:
        self.daz: bool = daz
        self.ftz: bool = ftz
        self._prev_daz: bool = False
        self._prev_ftz: bool = False

    @staticmethod
    def set_daz(daz: bool | None = True) -> bool:
        """sets 'Denormals-Are-Zero'-flag and return previous value"""
        prev = daz_core.get_daz()
        if daz is not None:
            if daz is True:
                daz_core.set_daz()
            else:
                daz_core.unset_daz()
        return prev

    @staticmethod
    def set_ftz(ftz: bool | None = True) -> bool:
        """sets 'Flush-To-Zero'-flag and return previous value"""
        prev = daz_core.get_ftz()
        if ftz is not None:
            if ftz is True:
                daz_core.set_ftz()
            else:
                daz_core.unset_ftz()
        return prev

    def __enter__(self) -> tuple[bool, bool]:
        self._prev_daz = DAZ.set_daz(self.daz)
        self._prev_ftz = DAZ.set_ftz(self.ftz)
        return self.daz, self.ftz

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        DAZ.set_daz(self._prev_daz)
        DAZ.set_ftz(self._prev_ftz)
