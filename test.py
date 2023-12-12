from collections import OrderedDict

def flatten_dict(d):
    def items():
        for key, value in d.items():
            # nested subtree
            if isinstance(value, dict):
                for subkey, subvalue in flatten_dict(value).items():
                    yield '{}.{}'.format(key, subkey), subvalue
            # nested list
            elif isinstance(value, list):
                for num, elem in enumerate(value):
                    for subkey, subvalue in flatten_dict(elem).items():
                        yield '{}.[{}].{}'.format(key, num, subkey), subvalue
            # everything else (only leafs should remain)
            else:
                yield key, value

    return OrderedDict(items())

import xmltodict

# Convert to dict
with open('policy_sample.xml', 'rb') as f:
    xml_content = xmltodict.parse(f)

# Flatten dict
flattened_xml = flatten_dict(xml_content)

# Print in desired format
for k,v in flattened_xml.items():
    print('{} = {}'.format(k,v))
