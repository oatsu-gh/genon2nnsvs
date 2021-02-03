# genon2nnsvs
 UTAU音源の原音をNNSVSで学習できるようにする。

## 使い方

1. UTAU音源の各音階を moresampler で原音設定しなおす。設定は 日本語VCV、連番なし、エイリアスへのprefix追加なし。
2. [oto_estimation_checker](https://github.com/oatsu-gh/oto_estimation_checker) で原音設定ミスを検出する。手動チェックでもよい。
3. 原音設定ミスを直す。オーバーラップが子音開始位置、先行発声が母音開始位置となるようにする。
4. 原音設定ファイルの右ブランクを正にする。setParamで一括変換するか、[force_otoini_cutoff_negative](https://github.com/oatsu-gh/oto2lab/tree/master/tool/force_otoini_cutoff_negative) を使う。
5. **genon2db.py** を実行して、tableファイルとかを指定してなんかこう…する。
6. dataフォルダ内にlabファイルとwavが保存される。ついでにustも生成される。
7. 未実装：学習の評価に使うファイルのリストを作る。（dev, eval, utt_list とか）
8. 未実装：acoustic、duration、timelag に各種学習データを配置する。