# Talebi API service

## Development

### Prerequisites

- Pycharm (IDE)
- Docker
- Docker compose

### Getting started

- Copy and update environment variables from `.env.sample`
  ```shell
  cp .env.sample .env
   ```
- Run services
  ```shell
  docker compose up
  ```
- Apply migrations
  ```shell
  docker compose run --rm backend python3 manage.py migrate
  ```
- Modify the files, the web server will reload on your file changes.
- Happy coding!!