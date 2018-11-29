import json
import re
import itertools

with open('part-00000', 'r') as nerFile:
    # locations = myfile.read().replace('\n', '')
    nerRaw = nerFile.read()

    reentities = re.findall(r'{(.*?)}', nerRaw)

    reentities = ['{' + e + '}' for e in reentities]

    entities = [json.loads(e) for e in reentities]

    locations = [e['LOCATION'] for e in entities]

    locations = list(itertools.chain.from_iterable(locations))

    locations = list(set(locations))
    print locations

# entities = [m.group(1) for l in lines for m in reentities if m]
