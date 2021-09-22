# enricorotundo.github.io
Dropping a few commands here since I tend to forget them.

### 1. Clone

```
git clone git@github.com:enricorotundo/enricorotundo.github.io.git
git checkout source
```

### 2. Create env

```
virtualenv venv
source venv/bin/activate
pip install "pelican[markdown]==4.5.4"
pip install ghp-import==1.0.1

cd ~/git
git clone git@github.com:alexandrevicenzi/Flex.git
pelican-themes --install ~/git/Flex --verbose
```

### 3. Develop
```
# cd back into this repo
source venv/bin/activate
pelican --listen --autoreload
```

Head to http://127.0.0.1:8000/

### 4. Publish

1. From `source` branch: `git commit -am "up" && pelican content -o output -s pelicanconf.py && ghp-import --branch=master output && git push -f origin master && git push`

2. Add custom domain (`enricorotundo.com`) and enable HTTPS --> https://github.com/enricorotundo/enricorotundo.github.io/settings

Give it 1 minute to update + use Incogito!