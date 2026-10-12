import unittest
from practice.task_10_json_validator.starter import validate

SCHEMA={"type":"object","required":["name","samples"],"additionalProperties":False,"properties":{
"name":{"type":"string","minLength":2},"samples":{"type":"array","minItems":1,"items":{"type":"object","required":["id"],"properties":{"id":{"type":"integer"}}}}}}
class Tests(unittest.TestCase):
    def test_valid(self): self.assertEqual(validate({"name":"Run","samples":[{"id":1}]},SCHEMA),[])
    def test_nested_errors_deterministic(self):
        self.assertEqual(validate({"extra":1,"name":"R","samples":[{"id":True},{}]},SCHEMA),[
            "$.extra: unexpected","$.name: too short","$.samples[0].id: expected integer","$.samples[1].id: required"])
    def test_type_short_circuit(self):
        self.assertEqual(validate([],SCHEMA),["$: expected object"])
    def test_bad_schema(self):
        with self.assertRaises(ValueError): validate(1,{"type":"mystery"})
if __name__ == "__main__": unittest.main()

