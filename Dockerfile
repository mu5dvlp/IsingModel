# ベースイメージとしてPython 3.9を使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    graphviz \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# スクリプトをコピー
COPY normal.ipynb \
    transverseField.ipynb \
    manualCalculation.ipynb \
    commonLogin.py \
    /app/

# //ーーーーーーーーーーーーーーーーーーーーー
# pipをアップグレード
RUN pip install --upgrade pip

# 〜〜〜
# qiskitのインストール
RUN pip install qiskit

# 回路図などの画像生成用
RUN pip install matplotlib
RUN pip install pylatexenc

# plot_state_qshpere用
RUN pip install seaborn

# 〜〜〜
# jupyter notebookのインストール
RUN pip install notebook

# //ーーーーーーーーーーーーーーーーーーーーー
# Jupyter Notebookを起動するコマンドを指定
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]


