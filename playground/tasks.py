from app import app

@app.task
def testtask():
    print('SayHello')

@app.task
def testtask2():
    print('KEKW')