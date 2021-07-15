# AWS構成
![AWS構成](https://user-images.githubusercontent.com/24289696/125838431-f3515a5f-9eff-41ca-a936-de576820969f.jpg)


# デプロイ
`sls deploy -v`

# S3
- jsonファイルを置く. e.g hello.json
```
{
    "greeting": "Hello, World!"
}
```

# 環境変数の設定 .env
  - DB
  - Lambda

# Vpc Labmda と S3 の疎通
### IAM Role 
- Lambda 実行ロールに Amazon S3 バケットへのアクセスを許可する
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/lambda-execution-role-s3-bucket/

### Vpc Endpoint
- VPC Lambda から S3 へ接続するためには VPC Endpoint を設定する.
  - https://aws.amazon.com/blogs/aws/new-vpc-endpoint-for-amazon-s3/

# Cognito (SSO)
- Amazon Cognito ユーザープールを使用して、SAML ID プロバイダーを設定する. e.g Auth0 
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/auth0-saml-cognito-user-pool/?nc1=h_ls

- SAML ユーザープール IdP 認証フロー
  - https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/cognito-user-pools-saml-idp-authentication.html

- Amazon EC2 インスタンスを踏み台ホストとして使用して、ローカルマシンからプライベート Amazon RDS DB インスタンスに接続する
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/rds-connect-ec2-bastion-host/?nc1=h_ls

# Bastion(踏み台)サーバー
- https://aws.amazon.com/jp/premiumsupport/knowledge-center/rds-connect-ec2-bastion-host/?nc1=h_ls
  - Public Subnet, Internet Gateway, Elastic IP(Public IP), Security Group
  - mysql


# 静的ウェブサイトのホスティング
### bucket 作成
- `aws --profile $profile s3api create-bucket --bucket $bucket_name`
### 静的ウェブサイトの設定
- `aws --profile $profile s3 website --index-document index.html --error-document error.html s3://elearning-sub-ui`
### デプロイ
- `aws --profile $profile s3 sync public/ s3://$bucket_name --acl public-read`

# CORS設定
- APIGateway, Lambda, S3
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/api-gateway-cors-errors/ 
