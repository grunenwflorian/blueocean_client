from typing import Dict, Any, List

from blueocean.request import Request
from blueocean.step import Step


class Node:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        super().__init__()
        self.request = request
        self._links = args["_links"]
        self.id = args["id"]
        self.display_name = args["displayName"]
        self.state = args["state"]
        self.result = args["result"]
        self.type = args["type"]
        self.duration_millis = args["durationInMillis"]

    def get_link(self, key):
        return self._links[key]["href"]

    def steps(self) -> List[Step]:
        return self.request.get(self.get_link("steps"), cls=Step, array=True)

    def step(self, step_id) -> Step:
        return self.request.get(self.get_link("steps"), step_id, cls=Step)
