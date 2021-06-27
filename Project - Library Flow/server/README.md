# Library Flow Server

Backend server for both data collecting and client servering.

## Development

```shell
uvicorn library_flow.main:app --reload
```

## Production

* Setup environment variable `DATABASE_URL` for database, PostgreSQL is suggested
* Start server

```shell
uvicorn library_flow.main:app
```

