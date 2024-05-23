# Base para BDD con Python y Flask

## Correr la App

### Modo desarrollo

```sh
flask --app app run --debug
```

### Modo producción

```sh
gunicorn app:app
```

### Ejecutar un script en psql

```sh
psql -f script.sql
```
