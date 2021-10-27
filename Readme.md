```sh
python3 -mvenv env
source env/bin/activate
pip install -r requirements.txt
cd src
python manage.py migrate
cd bulma_theme/nodejs_static && yarn && yarn build
cd ../.. && python manage.py runserver
```
