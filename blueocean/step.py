from typing import Dict, Any

from blueocean.request import Request


class Step:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        super().__init__()
        self.request = request
        self._links = args["_links"]
        self.id = args["id"]
        self.display_name = args["displayName"]
        self.actions = args["actions"]
        self.result = args["result"]
        self.duration_millis = args["durationInMillis"]
