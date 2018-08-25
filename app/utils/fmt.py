import json
from collections import OrderedDict

def formatOutput(isFailed, output):
    if isFailed > 0:
        output['state'] = 'failed'
    return json.dumps(OrderedDict([('state', output['state']), 
                                    ('confStatus', output['confStatus']), 
                                    ('htpStatus', output['htpStatus']), 
                                    ('ngingxStatus', output['nginxStatus'])]))
