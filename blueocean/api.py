from __future__ import annotations

from typing import Any, Dict, List

from blueocean.request import Request


DOWNSTREAM_JOB_CLASS = "io.jenkins.blueocean.listeners.NodeDownstreamBuildAction"


class Artifact:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        self.request = request
        self._links = args["_links"]
        self.downloadable = args["downloadable"]
        self.name = args["name"]
        self._url = args["url"]

    @property
    def url(self):
        return self.request.base_url + self._url


class Step:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        self.request = request
        self._links = args["_links"]
        self.id = args["id"]
        self.display_name = args["displayName"]
        self.actions = args["actions"]
        self.result = args["result"]
        self.duration_millis = args["durationInMillis"]


class Node:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        self.request = request
        self._links = args["_links"]
        self._actions = args["actions"]
        self.id = args["id"]
        self.display_name = args["displayName"]
        self.state = args["state"]
        self.result = args["result"]
        self.type = args["type"]
        self.duration_millis = args["durationInMillis"]

    @property
    def log_url(self):
        return self.request.base_url + self.get_link("log") + "?start=0"

    def get_link(self, key):
        return get_link(self._links, key)

    def steps(self) -> List[Step]:
        return self.request.get(self.get_link("steps"), cls=Step, array=True)

    def step(self, step_id) -> Step:
        return self.request.get(self.get_link("steps"), step_id, cls=Step)

    def get_downstream_runs(self) -> List[Run]:
        runs = []
        for action in self._actions:
            if action["_class"] == DOWNSTREAM_JOB_CLASS:
                runs.append(self.request.get(get_link(action["_links"], "self"), cls=Run))

        return runs


class Run:
    def __init__(self, request: Request, args: Dict[str, Any]) -> None:
        self.request = request
        self._links = args["_links"]
        self.causes = args["causes"]
        self.state = args["state"]
        self.commitId = args["commitId"]
        self.durationInMillis = args["durationInMillis"]

    @property
    def log_url(self):
        return self.request.base_url + self.get_link("log") + "?start=0"

    def get_link(self, key):
        return get_link(self._links, key)

    def nodes(self) -> List[Node]:
        return self.request.get(self.get_link("nodes"), cls=Node, array=True)

    def node(self, node_id) -> Node:
        return self.request.get(self.get_link("nodes"), node_id, cls=Node)

    def artifacts(self) -> List[Artifact]:
        return self.request.get(self.get_link("artifacts"), cls=Artifact, array=True)


def get_link(links, key):
    return links[key]["href"]
