# postgres tutorial - part 1

aqui va lo que hice siguiendo el tutorial de postgres (https://www.postgresql.org/docs/current/tutorial.html), solo la parte 1, capitulo por capitulo.

en vez de instalar postgres lo levante con docker (v18), con `docker compose up -d` y ya, la primera vez corre solo los scripts de la carpeta sql.

los scripts:
- 01 es el capitulo 1, lo basico (version, fecha, etc)
- 02 es el capitulo 2, crear tablas, insert, select, joins, group by, update y delete
- 03 es el capitulo 3, vistas, llaves foraneas, transacciones, ventanas y herencia
- 04 es el ejercicio mio, una biblioteca chiquita con autores, libros, socios y prestamos

en evidencias deje lo que salio al correr cada script, las consultas con su resultado.

para entrar a la base:

```
docker exec -it pg-tutorial-part1 psql -U postgres -d mydb
```

usuario y clave: postgres / postgres, puerto 5432

si quieres empezar de cero borras la carpeta data y lo levantas de nuevo:

```
docker compose down
Remove-Item -Recurse -Force .\data
docker compose up -d
```

nota: hay un par de ejemplos del tutorial que dan error a proposito, esos los deje comentados para que no se caiga la carga .-.
