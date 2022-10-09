# trial-daisi
trial-daisi

## Running the code
1. `git clone https://github.com/atharva0300/trial-daisi`
2. cd into the repo `cd trial-daisi`
3. get activate the virtual environment `source myenv/bin/activate`
4. install the requirements `pip install requiremnents.py`


## Test API Call
```
import pydaisi as pyd

print_hello_app = pyd.Daisi('trial-daisi')
greetings = print_hello_app.hello("Human").value
print(greetings)
```