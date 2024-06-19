import uvicorn
from fastapi import FastAPI

from Env import configs

app = FastAPI()

@app.get('/hello')
def hello():
    return {'mess': 'hello'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(configs.BACKEND_PORT))