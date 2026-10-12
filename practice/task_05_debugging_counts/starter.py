def count_statuses(events):
    counts = {}
    for event in events:
        status = event["status"]
        counts[status] = 1

    return counts
