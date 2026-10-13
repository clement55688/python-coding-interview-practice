from collections import defaultdict

def max_students_on_bench(records: list[tuple[str, str]]) -> int:
    if not isinstance(records, list):
        raise ValueError("Recorrds is not tuple.")

    students_by_bench = defaultdict(set)

    for record in records:
        if not isinstance(record, tuple) or len(record) != 2:
            raise ValueError("Invalid record error")

        if not isinstance(record[0], str) or not isinstance(record[1], str) or record[0] == '' or record[1] == '':
            raise ValueError("Invalid input value")
        students_by_bench[record[0]].add(record[1])

    return max((len(students) for students in students_by_bench.values()), default = 0)