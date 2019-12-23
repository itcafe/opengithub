{

"coediting": false,
"tags": [{"name": "チートシート"}],
"private": true,
"tweet": false

]

}++++++

## パスを通す

#### Viで環境変数を編集

```bash
vi ~/.bash_profile
```

※Viコマンド

http://www.gi.ce.t.kyoto-u.ac.jp/user/susaki/command/vi.html


#### 設定を保存

```bash
source ~/.bash_profile
```



#### 一回だけパスを通したい場合

下記はflutterの例

```bash
export PATH="$PATH:`pwd`/flutter/bin"
```



## Flutter

macOS

https://flutter.dev/docs/get-started/install/macos

### Get the Flutter SDK









###  iOS setup

pod setupがややこしい

### Android setup

1. pluginsで Flutter iFluter18n をインストール
2.



## node

#### python2系が必要なモジュール
npm config set python /anaconda3/envs/py27/bin/python

####  buildでメモリ不足

NODE_OPTIONS=--max_old_space_size=4096 npm run build



#### S3にUP

aws s3 sync /Users/mn/github/vue-dashboard-local/dist s3://5slabo.com



## anaconda

### アンインストール

1.アンインストール

```
conda install anaconda-clean
```

```
anaconda-clean
```

2.Homeフォルダ直下のAnacondaフォルダを完全削除する

3.パスを削除

```
open ~/.bash_profile       // 標準のテキストエディタで .bash_profile を開く
```

または

```
atom ~/.bash_profile
```

`open ~/.bash_profile -a Atom` のように `-a + [Application]` でテキストエディタを指定できます

内容は↓

```
export PATH=(パス):$PATH
```

4.反映（ターミナルの再起動不要）

```
$ source ~/.bash_profile
```

5.確認

```
printenv PATH
```



### インストール

1.パッケージダウンロード

https://www.anaconda.com/distribution/

2.パッケージたちを最新にしておく

```
conda update --all
```



### トラブルシュート

■アナコンダがおかしい
conda install anaconda



## aws

```
conda install -c conda-forge awscli
```
