import pydaisi as pyd

print_hello_app = pyd.Daisi('trial-daisi')
greetings = print_hello_app.hello("Human").value
print(greetings)