# amazon-connect-last-agent-rooting
amazon connectでラストエージェントルーティングを実装する  

# ラストエージェントルーティングとは
ラストエージェントルーティングは、コンタクトセンターの着信アルゴリズムの1つ。  
最後に対応したエージェントに接続可能な場合、再度ルーティングすること。  
追加の質問や手続きを円滑に行い、顧客満足度を向上させることが可能。

# デプロイコマンド
```
# ビルド
sam build

# デプロイ
sam deploy

# connectにLambda関数を紐付け(Function分2回実行)
aws connect associate-lambda-function \
    --instance-id [connectのインスタンスID] \
    --function-arn [デプロイしたlamdbaのARN] \
    --region "ap-northeast-1"
```

