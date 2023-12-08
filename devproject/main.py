from ElectricPython import sendJSRequest as js
from ElectricPython import FRONTEND, BACKEND, Window

print(js('console.log("Python is running...")', env=BACKEND))

w = Window(html="<head><title>Test</title></head><body><h1>Test</h1></body>")

print(js('console.log("Python complete!")', env=BACKEND))
