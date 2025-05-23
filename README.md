# design_detailer
設計の概要から、詳細と図を作成するツール


## ディレクトリ構成
以下の構成になるように進める

### 概要
```
app_name/
├── frontend/           # フロントエンド（ReactやVue）
│   ├── src/            # アプリのコード（UI、設計の入力画面、mermaid図プレビューなど）
│   ├── public/         # 静的ファイル（HTML, CSS, 画像など）
│   └── config/         # フロントエンド用設定（環境設定、ビルド設定）
│
├── backend/            # バックエンド（APIサーバーなど）
│   ├── models/         # モデルファイル（.gguf等）
│   ├── lib/            # llama.cppなど外部バイナリ
│   ├── src/            # サーバーコード（データの処理、APIロジック）
│   └── config/         # バックエンド設定（DB接続設定、APIキーなど）
│
└── README.md           # プロジェクト全体の概要
```

### 詳細版
```
app_name/
├── frontend/                        # フロントエンド（React）
│   ├── src/
│   │   ├── assets/                  # 画像・フォント・アイコンなど静的アセット
│   │   ├── components/              # 再利用可能なUIコンポーネント
│   │   │   ├── DesignForm.tsx       # 設計概要フォームコンポーネント
│   │   │   ├── MermaidPreview.tsx   # mermaid図を表示するコンポーネント
│   │   │   └── ...
│   │   ├── pages/                   # ルーティング単位のページコンポーネント
│   │   │   ├── Home.tsx             # トップページ
│   │   │   ├── Detail.tsx           # 詳細ページ
│   │   │   └── ...
│   │   ├── hooks/                   # Reactカスタムフック
│   │   │   └── useDesignData.ts     # 設計データ取得・保存用hook
│   │   ├── services/                # API通信や外部連携ロジック
│   │   │   └── designService.ts     # 設計データのAPI呼び出し処理
│   │   ├── utils/                   # 汎用ユーティリティ関数
│   │   │   └── formatDate.ts        # 日付フォーマット関数など
│   │   ├── App.tsx                  # アプリエントリポイント
│   │   ├── index.tsx                # Appのエクスポート用
│   │   └── styles.ts                # Appのスタイル定義
│   │
│   ├── public/                      # 静的ファイル（HTML, favicon, ogp画像など）
│   │   └── index.html               # ReactのHTMLエントリー
│   │
│   └── config/                      # 環境別設定やビルド設定
│       ├── webpack.config.js
│       └── env.development          # 環境変数（開発用）
│       └── env.production           # 環境変数（本番用）
│
├── backend/                         # バックエンド（Python / FastAPI）
│   ├── models/                      # LLMなどのモデルファイル（.gguf等）
│   ├── lib/                         # llama.cpp等の外部バイナリ・C/C++ライブラリ
│   ├── src/                         # Pythonアプリ本体
│   │   ├── api/                     # APIルーティング定義（APIRouterでエンドポイントをまとめる）
│   │   │   └── design.py            # /api/designエンドポイント
│   │   ├── controllers/             # コントローラー層（リクエストごとの処理）
│   │   │   └── design_controller.py
│   │   ├── services/                # ビジネスロジック層
│   │   │   └── design_service.py
│   │   ├── models/                  # PydanticモデルやDBモデル
│   │   │   └── design.py
│   │   ├── utils/                   # 汎用ヘルパー関数
│   │   │   └── helpers.py
│   │   ├── config/                  # 設定ファイル（DB接続、環境変数など）
│   │   │   └── db.py
│   │   ├── lib/                     # Python自作モジュール（必要な場合のみ）
│   │   └── main.py                  # アプリケーションのエントリポイント
│   │
│   └── tests/                       # バックエンド用テストコード（pytest推奨）
│       └── test_design.py
│
├── docker-compose.yml               # コンテナ環境構築用ファイル
├── .env                             # 環境変数（共通）
├── README.md                        # プロジェクト概要
└── requirements.txt                 # Python依存パッケージ

```

### コンポーネント設計
default exportは基本使用しない（import側で自由に名前をつけることができるため）

`Button`というコンポーネントの場合以下のような構成で設計する
```
Button/
├── index.tsx  # Buttonをexportするためだけのファイル
├── types.ts  # Buttonコンポーネントに関連する型定義を含むファイル
├── styles.ts  # Buttonコンポーネントのスタイルを定義するファイル
├── Button.tsx  # 見た目に関する部分
├── Button.stories.tsx  # Storybookで表示するためのファイル
├── hooks.ts  # ロジックに関する部分
|── components/
│   ├── SubComponentA/
│   ├── SubComponentB/
```

---

## ブランチ戦略
ブランチ名は以下のように命名する

| ブランチ名 | 用途 | 命名規則例 |
|------------------|----------------------------------------------------------------------|---------------------|
| main | 安定したバージョンを保持。完成した機能や修正をマージ。 | main |
| feature/xxx | 新しい機能の開発に使用。xxxは機能の名前を示す。 | feature/add-feature |
| bugfix/xxx | バグ修正に使用。xxxは修正内容を示す。 | bugfix/fix-issue |
| refactor/xxx | コードのリファクタリングに使用。xxxはリファクタリングの内容を示す。 | refactor/improve-component-structure |

---

## コミットメッセージのルール
以下のタグを使用する

| タグ | 用途 | 例 |
|--------|----------------------------------|------------------------------------|
| feature | 新しい機能の追加 | [feature]画像認識モデルを追加 |
| update | 既存機能の仕様変更や改善 | [update]ボタンのデザインを変更 |
| bugfix | バグ修正 | [bugfix]データ読み込みエラーを修正 |
| docs | ドキュメントの変更 | [docs]READMEに使用方法を追加 |
| refactor | コードのリファクタリング（動作に影響しない） | [refactor]モデルの構造を整理 |
| chore | その他の変更（パッケージ更新、ビルドプロセスの変更など） | [chore]依存パッケージを更新 |

---

## 環境構築
`conda`内に`nodeenv`で`node`環境を入れる。

```
nodenv install 20.18.0
```