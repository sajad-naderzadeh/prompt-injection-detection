import json


def load_logs(path):

    with open(path) as f:
        return json.load(f)


if __name__ == "__main__":

    logs = load_logs(
        "data/logs/security_logs.json"
    )

    print(logs)
