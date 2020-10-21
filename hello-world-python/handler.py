import time

def hello(event, context):
    print("second update !")
    time.spleep(4)
    return "hello-world"