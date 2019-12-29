## npmにpython2.7がいる

https://sutaba-mac.site/gyp-not-accept-python3/



・pyenvを入れる



・Python環境を指定

npm config set python /Users/mn/.pyenv/versions/2.7.9/bin/pythonnode-pre-gyp


## permission error

・node modlesフォルダを消してみる（再度npm install

・パーミッションを無視

sudo npm install --unsafe-perm
