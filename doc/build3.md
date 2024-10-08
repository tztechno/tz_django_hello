エラーメッセージを見ると、まだPythonが正しくインストールされていないか、パスが適切に設定されていないようです。また、Homebrewの権限に関する問題も発生しているようです。これらの問題を順番に解決していきましょう。

1. まず、Homebrewの権限問題を解決します：

```
sudo chown -R $(whoami) /usr/local/lib/docker
```

2. 次に、Pythonが正しくインストールされているか確認します。Macには通常、Python 3がプリインストールされています。以下のコマンドで確認してみてください：

```
python3 --version
```

3. もし上記のコマンドでバージョンが表示された場合、`python`の代わりに`python3`を使用することができます。その場合、以下のようにパスを設定します：

```
echo 'alias python=python3' >> ~/.zshrc
source ~/.zshrc
```

4. もし`python3`も見つからない場合は、Homebrewを使って再度Pythonをインストールしてみましょう：

```
brew install python
```

5. インストールが完了したら、パスを確認します：

```
which python3
```

6. 表示されたパスを使って、`.zshrc`ファイルを更新します：

```
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

7. これで`python`コマンドが使えるはずです。確認してみましょう：

```
python --version
```

8. Pythonが正しく動作することを確認できたら、仮想環境を作成します：

```
python -m venv venv
```

9. 仮想環境を有効化します：

```
source venv/bin/activate
```

これらの手順で問題が解決するはずです。もし引き続き問題がある場合は、各ステップで発生したエラーメッセージを教えてください。それに基づいて、さらに詳しいアドバイスができます。