def detect_anomaly(logs):

    alerts = []


    failed_logins = {}

    for log in logs:

        if log["event"] == "login_failed":

            ip = log["ip"]

            failed_logins[ip] = failed_logins.get(ip, 0) + 1


    for ip, count in failed_logins.items():

        if count >= 3:

            alerts.append(
                {
                    "type": "Brute Force Attack",
                    "severity": "HIGH",
                    "source_ip": ip
                }
            )


    for log in logs:

        if log["event"] == "file_download":

            if log.get("files", 0) > 1000:

                alerts.append(
                    {
                        "type": "Data Exfiltration",
                        "severity": "CRITICAL",
                        "user": log["user"]
                    }
                )


    return alerts


if __name__ == "__main__":

    from src.parser.log_parser import load_logs

    logs = load_logs(
        "data/logs/security_logs.json"
    )

    print(
        detect_anomaly(logs)
    )
