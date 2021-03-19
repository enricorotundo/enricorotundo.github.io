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
```
# from `source` branch
git commit -am "up"
pelican content -o output -s pelicanconf.py
ghp-import --branch=master output
git push origin master
```