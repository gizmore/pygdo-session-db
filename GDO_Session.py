from gdo.base.GDO import GDO
from gdo.base.GDT import GDT
from gdo.core.GDT_AutoInc import GDT_AutoInc
from gdo.core.GDT_Serialize import GDT_Serialize
from gdo.core.GDT_Token import GDT_Token
from gdo.core.GDT_User import GDT_User


class GDO_Session(GDO):

    _cookies: list

    @classmethod
    def start(cls, cookies):
        instance = cls().cookies(cookies)
        return instance

    def gdo_columns(self) -> list[GDT]:
        return [
            GDT_AutoInc('sess_id'),
            GDT_Token('sess_token'),
            GDT_User('sess_user'),
            GDT_Serialize('sess_data'),
        ]

    def cookies(self, cookies):
        self._cookies = cookies
        return self

