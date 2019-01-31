from clip import clip
from inspect import signature
sig = signature(clip)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
