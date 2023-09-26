#九九乘法表  有個問題，是數字從0開始到小於9，沒關係，先寫
for i in range(9):
  for j in range(9):
    print(i, 'x', j,sep='',end=' ')
  print()