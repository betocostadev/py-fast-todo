# To-Done Backend
Simple Python Backend using FastAPI to run a To-Do Application

## Run the Container

Run the commands in the application folder
Build the Docker Image

```docker build --pull -t py-fast-todo .```


With the image create you can just use Dockercompose

```docker compose up```

Then, open another terminal window and run Postgres

```docker compose exec db psql -U postgres```
