# enricorotundo.github.io
Dropping a few commands here since I tend to forget them.

### Create env

```
virtualenv venv
source venv/bin/activate
pip install "pelican[markdown]==4.5.4"
pip install ghp-import==1.0.1

cd ~/git
git clone git@github.com:alexandrevicenzi/Flex.git
pelican-themes --install ~/git/Flex --verbose
```

### Develop
```
source venv/bin/activate
pelican --listen --autoreload
```



### Publish

From `source` branch:

```
git commit -am "up" && pelican content -o output -s pelicanconf.py && ghp-import --branch=master output && git push -f origin master && git push
```

Give it 1 minuto to update + use Incogito!
Check if custom domain and HTTPS are set uo --> https://github.com/enricorotundo/enricorotundo.github.io/settings