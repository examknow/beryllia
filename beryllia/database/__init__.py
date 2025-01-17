import asyncpg

from .db_cliconns import *
from .db_klines   import *
from .db_statsp   import *

from ..normalise  import SearchType, SearchNormaliser

class Database(object):
    def __init__(self,
            pool:       asyncpg.Pool,
            normaliser: SearchNormaliser
            ):

        self.kline        = KLineTable(pool, normaliser)
        self.kline_remove = KLineRemoveTable(pool, normaliser)
        self.kline_kill   = KLineKillTable(pool, normaliser)
        self.cliconn      = CliconnTable(pool, normaliser)
        self.statsp       = StatsPTable(pool, normaliser)

    @classmethod
    async def connect(self,
            username:   str,
            password:   str,
            hostname:   str,
            db_name:    str,
            normaliser: SearchNormaliser):

        pool = await asyncpg.create_pool(
            user    =username,
            password=password,
            host    =hostname,
            database=db_name
        )
        return Database(pool, normaliser)
