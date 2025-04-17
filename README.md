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
│   │   └── App.tsx                  # アプリエントリポイント
│   │
│   ├── public/                      # 静的ファイル（HTML, favicon, ogp画像など）
│   │   └── index.html               # ReactのHTMLエントリー
│   │
│   └── config/                      # 環境別設定やビルド設定
│       ├── webpack.config.js
│       └── env.development          # 環境変数（開発用）
│       └── env.production           # 環境変数（本番用）
│
├── backend/                         # バックエンド（Node.js / Express）
│   ├── src/
│   │   ├── controllers/             # ルーティングごとの処理まとめ
│   │   │   └── designController.ts  # 設計データ用コントローラー
│   │   ├── services/                # ビジネスロジック層
│   │   │   └── designService.ts     # データ取得・保存処理
│   │   ├── models/                  # DBスキーマ（ORMを使う場合）
│   │   │   └── Design.ts            # 設計データモデル
│   │   ├── routes/                  # APIルーティング定義
│   │   │   └── designRoutes.ts      # /api/designエンドポイント
│   │   ├── utils/                   # 汎用ヘルパー関数
│   │   ├── config/                  # 設定ファイル（DB接続・環境変数）
│   │   │   └── db.ts                # データベース接続設定
│   │   └── server.ts                # アプリケーションのエントリポイント
│   │
│   └── tests/                       # バックエンド用テストコード
│       └── design.test.ts
│
├── docker-compose.yml               # コンテナ環境構築用ファイル
├── .env                             # 環境変数（共通）
├── README.md                        # プロジェクト概要
└── package.json                     # プロジェクト依存関係

```

## ブランチ戦略
ブランチ名は以下のように命名する

| ブランチ名 | 用途 | 命名規則例 |
|------------------|----------------------------------------------------------------------|---------------------|
| main | 安定したバージョンを保持。完成した機能や修正をマージ。 | main |
| feature/xxx | 新しい機能の開発に使用。xxxは機能の名前を示す。 | feature/add-feature |
| bugfix/xxx | バグ修正に使用。xxxは修正内容を示す。 | bugfix/fix-issue |

## コミットメッセージのルール
以下のタグを使用する

| タグ | 用途 | 例 |
|--------|----------------------------------|------------------------------------|
| feature | 新しい機能の追加 | [feature]画像認識モデルを追加 |
| bugfix | バグ修正 | [bugfix]データ読み込みエラーを修正 |
| docs | ドキュメントの変更 | [docs]READMEに使用方法を追加 |
| refactor | コードのリファクタリング（動作に影響しない） | [refactor]モデルの構造を整理 |
| chore | その他の変更（パッケージ更新、ビルドプロセスの変更など） | [chore]依存パッケージを更新 |
