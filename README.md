## Instrucciones para Docker

### 1. Desarrollo

`a)` **Reconstruir la imagen de Docker y ejecutar en segundo plano**:

```bash
docker-compose up --build
```

`b)` **Reconstruir la imagen de Docker y ejecutar en segundo plano**:

```bash
docker-compose up --build -d
```

`c)` **Ver los contenedores en ejecución**:

```bash
docker-compose ps
```

`d)` **Detener el contenedor**:

```bash
docker-compose down
```

`e)` **Eliminar contenedores, redes y volúmenes (limpiar todo)**:

```bash
docker-compose down --volumes ai-chat
```

`f)` **Ver logs del contenedor**:

```bash
docker-compose logs -f ai-chat
```

`g)` **Acceder a la terminal del contenedor**:

```bash
docker-compose exec -it ai-chat /bin/sh
```

### 2. Producción

- Cambiar el comando final del `Dockerfile` a:

```bash
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5500"]
```
