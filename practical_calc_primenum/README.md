## 素数計算を複数パターンで実施

### 2パターンで実装
- calc_prime_num_0_1.py：数字を順番に見ていって、素数で割れるか判定
- calc_prime_num_e1_1.py：エラトステネスのふるいを実装

### trial：上記2パターンになるまでの記録

- trial/calc_prime_num_0_0.py：何も調べず、まず考えたコードを実装
- calc_prime_num_e0_0.py：エラトステネスのふるいの原理だけを調べて、自分で考えて実装
  - 一般的なフラグ管理ではなく、リストで実数を格納
- calc_prime_num_e0_1.py：calc_prime_num_e0_0.pyのコンセプトはそのままに最適化
- calc_prime_num_e1_0.py：一般的なエラトステネスのふるいの方法での実装
  - ブールを使った効率的な方法
