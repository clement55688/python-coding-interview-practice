def latest_status(events):
    res = {} # {sample_id: (timestamp, status)}

    for event in events:
        sample_id = event["sample_id"]
        timestamp = event["timestamp"]
        status = event["status"]

        if sample_id not in res or timestamp >= res[sample_id][0]:
            res[sample_id] = (timestamp, status)

    return res