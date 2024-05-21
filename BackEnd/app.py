import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Env.handle import configs

app = FastAPI()

origins = [
    "http://192.168.124.4:3000",
    # 你可以添加其他允许的源
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/hello')
def hello():
    return {'mess': 'hello'}


print(configs.get_params())
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(configs.BACKEND_PORT))