# trial-daisi
trial-daisi

## Running the code
1. Clone the repo `git clone https://github.com/atharva0300/trial-daisi`
2. cd into the repo `cd trial-daisi`
3. Create a vitual environment. I have called it `myenv`. create it using `python3 -m venv /path/to/the venv/myenv` or if you are already in the directory, use `python3 -m venv myenv`.
4. Activate the virtual environment `source myenv/bin/activate`
5. Install the requirements `pip install requiremnents.py`


## Test API Call
```
import pydaisi as pyd

print_hello_app = pyd.Daisi('trial-daisi')
greetings = print_hello_app.hello("Human").value
print(greetings)
```