from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api import design_detail, mermaid


app = FastAPI()
# CORSを許可
# 以下のコードを書くことでフロントエンド（http://localhost:3000 や http://127.0.0.1:3000）からのAPIリクエストがブロックされずに通るようにできる。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # フロントエンドのURL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(design_detail.router, prefix="/api")
app.include_router(mermaid.router, prefix="/api")
