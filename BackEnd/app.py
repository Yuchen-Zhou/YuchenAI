import uvicorn
from fastapi import FastAPI
from BackEnd.Env.handle import configs

app = FastAPI()

print(configs.get_params())

if __name__ == '__main__':
    uvicorn.run(app)