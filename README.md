# Trigger team D backend

## Requirement

- python 
- fastAPI
- postgreSQL

## Run

### database

```
mkdir -p ./database/postgres/data
docker compose up -d
```

postgresサーバーは5433ポートで立ち上がります．

### app

- Run app
`uvicorn main:app`

- Watch directory

`uvicorn main:app --reload`
