from blueocean.run import Run
from blueocean.request import *


def create_client(base_url: str):
    return BlueOceanClient(
        Request(base_url)
    )


class BlueOceanClient:

    def __init__(self, request: Request) -> None:
        self.request = request

    def multi_branch_pipeline(self):
        pass

    def run(self, pipeline, branch, run_id) -> Run:
        return self.request.get(
            BLUE_OCEAN_PREFIX_PATH, PIPELINES_PATH, pipeline, BRANCHES_PATH, branch, RUNS_PATH, str(run_id),
            cls=Run
        )


if __name__ == "__main__":
    client = create_client("http://macpro.fr.murex.com/ci")

    run = client.run("polycd", "master", 25999)
    nodes = run.nodes()

    undeploy_job = next(n for n in nodes if n.display_name == "undeploy e2eTest")
    e2E_jobs = [n for n in nodes if "run e2e" in n.display_name]

    print("done")
