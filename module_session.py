from gdo.base.GDO_Module import GDO_Module
from gdo.session.GDO_Session import GDO_Session


class module_session(GDO_Module):

    def __init__(self):
        super().__init__()

    def gdo_classes(self):
        return [
            GDO_Session,
        ]
