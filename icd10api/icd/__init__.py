

from collections import OrderedDict
import json
class ReasonableOrderedDict(OrderedDict):
    def __str__(self):
        return json.dumps(self, indent=2)

    def __repr__(self):
        return str(self)

__ALL__=('ReasonableOrderedDict',)
