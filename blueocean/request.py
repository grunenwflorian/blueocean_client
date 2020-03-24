import requests

BLUE_OCEAN_PREFIX_PATH = "blue/rest/organizations/jenkins"
PIPELINES_PATH = "pipelines"
BRANCHES_PATH = "branches"
RUNS_PATH = "runs"


class Request:

    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url

    def get(self, *args, cls, array=False):
        response = requests.get(join_path(self.base_url, *args), params={"limit": 10_000})
        response.raise_for_status()
        obj = response.json()
        if not array:
            return cls(self, obj)

        return list(map(lambda o: cls(self, o), obj))


def join_path(*args):
    return "/".join(args)
