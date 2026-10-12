def usage_totals(records):
    res = {}
    seen_id = set()

    for record in records:
        record_id = record["record_id"]
        reagent = record["reagent"]
        quantity = record["quantity"]

        if record_id not in seen_id:
            res[reagent] = res.get(reagent, 0) + quantity
        seen_id.add(record_id)

    return res