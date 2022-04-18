#!/bin/bash
docker-compose run wasm wasm-pack build --target web
sudo chown -R shelleywong:shelleywong hello-wasm
# cp ./hello-wasm/pkg/hello_wasm* ./mysite/static/js/
# docker-compose run web python manage.py collectstatic --noinput
