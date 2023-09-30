import logging
from typing import Any, List, Optional, Mapping

import redis

REDIS_ERRORS = (redis.ConnectionError, redis.ConnectionError, redis.TimeoutError)

from cfg import services

class Connection:
    def __init__(self) -> None:
        self._conn = redis.Redis(
            host=services.REDIS["host"],
            port=int(services.REDIS["port"]),
            password=services.REDIS["password"],
            socket_timeout=2,
            socket_connect_timeout=2,
            socket_keepalive=True,
            encoding="utf-8",
            decode_responses=True,  # To remove "b'" prefix as part of byte string
        )

    def close(self) -> None:
        self._conn.close()

    #
    # Low level APIs
    #
    def set(self, key: str, value: str) -> bool:
        try:
            self._conn.set(key, value)
            return True
        except REDIS_ERRORS as r:
            logging.error(r)
            return False

    def get(self, key: str) -> Optional[Any]:
        try:
            ret = self._conn.get(key)
            return ret
        except REDIS_ERRORS as r:
            logging.error(r)
            return None
