# 「Python実践入門」サンプルコード

技術評論社刊「Python実践入門」のサンプルコードです。

このサンプルコードはPython 3.8.1、JupyterLab 1.2.4で動作確認をしています。
各ディレクトリは書籍の各章と対応しており、サンプルコードはそれぞれ1つのノートブックファイル（.ipynb）にまとめています。
ノートブックファイルを実行する際は、ノートブックファイルのある場所で`jupyter lab`コマンドを実行してください。

# 実行方法

はじめに仮想環境の作成とJupyterLabのインストールを行います。

```shell
# 仮想環境の作成とJupyterLabのインストール
$ python3 -m venv venv
$ . venv/bin/activate
(venv)$ pip install jupyterlab==1.2.4
```

各章のディレクトリでJupyter Labを起動すると、ブラウザが立ち上がります。
左ペインから.ipynbファイルを開くとサンプルコードが表示されます。
ソースコードの書かれたセルの選択中にShift + Enterを押すと、そのセルのコードを実行できます。

```shell
# 各章のノートブックファイルがある場所でJupyterLabを起動
(venv)$ cd 01-introduction
(venv)$ jupyter lab
```

実行例は、「screenshot_01.png」を参照してください。

