from typing import Dict, Any, List

from blueocean.node import Node
from blueocean.request import Request


class Run:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        super().__init__()
        self.request = request
        self._links = args["_links"]
        self.causes = args["causes"]
        self.state = args["state"]
        self.commitId = args["commitId"]
        self.durationInMillis = args["durationInMillis"]

    def get_link(self, key):
        return self._links[key]["href"]

    def nodes(self) -> List[Node]:
        return self.request.get(self.get_link("nodes"), cls=Node, array=True)

    def node(self, node_id) -> Node:
        return self.request.get(self.get_link("nodes"), node_id, cls=Node)
