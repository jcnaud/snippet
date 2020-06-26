# OpenID Connect


## Principe


link : https://openid.net/connect/

- core: (minimal)
- Discovery: (Dynamic part) Defines how Clients dynamically discover information about OpenID Providers
- Dynamique Clinet registration: (Dynamic part) Defines how clients dynamically register with OpenID Providers
- Session management:
- Form Post response Mode:



Provider exemple:
 - your own server provider
 - google
 - microsoft
 - facebook
 7OP iframe on RP pages


## Ways of using OIDC
- Basic RP
- Implicit RP
- Hybrid RP
- Config RP
- Dynamic RP


RP = relying party
OP = 


## RP exemple

Python librarie iodcrp: OIDC OPs or RPs

  layer 4:
    - pypi: https://pypi.org/project/oidcrp/
    - github: https://github.com/IdentityPython/JWTConnect-Python-OidcRP
    - doc: https://oidcrp.readthedocs.io/en/latest/

## pyoidc

  - https://pyoidc.readthedocs.io/en/latest/

```python
from oidcrp import RPHandler
rph = RPHandler()
issuer_id = "https://example.org/"
info = rph.begin(issuer_id)
print(info['url'])
```

result
```
https://example.org/op/authorization?state=Oh3w3gKlvoM2ehFqlxI3HIK5&nonce=UvudLKz287YByZdsY3AJoPAlEXQkJ0dK&redirect_uri=https%3A%2F%2Fexample.com%2Frp%2Fauthz_cb&response_type=code&scope=openid&client_id=zls2qhN1jO6A
```