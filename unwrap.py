# Print Your code here
import json
t = """{ "nested" : { "array": [ {"string":"a value"}, 
{"string":"the other stuff"} ] }, "subvalue" : { "string" : "i contain stuff"} }"""
dt = json.loads(t)
print(len({"abe":2, "ksks": 5}))
def unwrap(kv):
    if type(kv) is dict:
        return unwrap(kv.values()[0])            
    elif type(kv) is list:
        return [unwrap(items) for items in kv]
    else:
        return kv
    
print(unwrap(dt['subvalue']))
