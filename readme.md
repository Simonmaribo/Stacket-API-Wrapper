![version](https://img.shields.io/github/v/release/simonmaribo/Stacket-API-Wrapper?label=Version&style=plastic) 
# Stacket API Wrapper : Python
Build powerful systems integrating your services together like never before.

#### Installing Requests and Supported Versions

Stacket is available on PyPI:

```console
$ python -m pip install stacket
```

# Example usage
```python
from stacket.StacketClient import StacketClient

client = StacketClient("auth-token")

if not client.verify():
    print("Token not authenticated with Stacket")
else:
    print("Authenticated with Stacket")


client.createService({
    "type": "minecraft",
    "node": "aad10",
    "package": "pkg1",
    "platform": "spigot",
    "version": "1.8.8"
})

for service in client.getServices():
    print(f"{service.getId()} : {service.getStatus()}")
```
