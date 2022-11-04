tar -cvzf test2.tar.gz model.pt

aws s3 cp test2.tar.gz s3://npx-translation-models/