import json



# Function for flattening
# json


ufj2 = {"fruit": 
          {
              "grapes": {
                  "nandi_hills": { "capacity" : 33 },
                  "nasik": { "capacity" : 67 },
              },
       
              "orange":{   
                  "california":  { "capacity" : 44 },
                  "nagpur": { "capacity" : 56 },
              }
          }
}

def flatten_json(y):
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:
            if not "capacity" in list(x.keys()) :
                x['queues'] = ",".join(list(x.keys()))
            for a in x:
                flatten(x[a], name + a + '.')

        # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# Driver code
print(json.dumps(flatten_json(ufj2)))


