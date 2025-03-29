virtualenv venv
source venv/bin/activate
cd examen_bentoml/
pip3 install -r requirements.txt
cd ../
docker load --input bento_image.tar
docker run --rm -d -p 3000:3000 quiroga_examen_bentoml_service:gqln4xqmowjq766n
python -m pytest -o log_cli=1 -o log_cli_level=INFO test.py