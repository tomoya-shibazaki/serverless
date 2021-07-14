# AWS構成
![AWS構成](https://user-images.githubusercontent.com/24289696/125596492-e35f4cbc-18a0-4ed5-886a-66e0c5f90359.jpg)

# デプロイ
`sls deploy -v`

# S3
- jsonファイルを置く

# 環境変数の設定 .env
  - DB
  - Lambda

# Vpc Endpoint
- VPC Lambda から S3 へ接続するためには VPC Endpoint を設定する.
  - https://aws.amazon.com/blogs/aws/new-vpc-endpoint-for-amazon-s3/

# Cognito (SSO)
- Amazon Cognito ユーザープールを使用して、SAML ID プロバイダーを設定する. e.g Auth0 
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/auth0-saml-cognito-user-pool/?nc1=h_ls

- SAML ユーザープール IdP 認証フロー
  - https://docs.aws.amazon.com/ja_jp/cognito/latest/developerguide/cognito-user-pools-saml-idp-authentication.html

- Amazon EC2 インスタンスを踏み台ホストとして使用して、ローカルマシンからプライベート Amazon RDS DB インスタンスに接続する
  - https://aws.amazon.com/jp/premiumsupport/knowledge-center/rds-connect-ec2-bastion-host/?nc1=h_ls
