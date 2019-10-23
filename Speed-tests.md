# Characters to be used to create a password and how to get them (speed tests)

**Characters to be used to create a password:**
 - 0123456789
 - ABCDEFGHIJKLMNOPQRSTUVWXYZ
 - abcdefghijklmnopqrstuvwxyz

**How to get them:**

Python3 uses Unicode encoding for strings. Remember that in Python, unlike many other programming languages, there is no such data type as a single character. In Python, any character is a string whose length is one.
The chr() function returns the character from the Unicode table corresponding to the passed number code.

```python3
print(
    ''.join([str(i) for i in range(10)])  # 0123456789
)

print(
    ''.join([chr(i) for i in range(65, 91)])  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
)

print(
    ''.join([chr(i) for i in range(97, 123)])  # abcdefghijklmnopqrstuvwxyz
)
```

At first you might think that generating lists takes longer and this is not the best choice. At first it seems that it’s better to just write ready-made lists and paste them into the code like this:
```python3
        random.choice(
            list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        ) for _ in range(arg())
```
instead of using:
```python3
        random.choice(
            [str(i) for i in range(10)] +
            [chr(i) for i in range(65, 91)] +
            [chr(i) for i in range(97, 123)]
        ) for _ in range(arg())
```
However, if you run speed tests, you can see that no matter how strange it may be, generating lists is still faster than using a ready-made list.

**Speed tests:**
```
Speed test when list generation:                    Speed test when using a ready-made list:
--------------------------------                    ----------------------------------------
0.006052614015061408                                0.006369479990098625
0.0062050020205788314                               0.00638000201433897
0.006213217013282701                                0.006395709002390504
0.006225417018868029                                0.006434156006434932
0.006230436003534123                                0.006450809014495462
0.006257681001443416                                0.006462963996455073
0.006305918999714777                                0.006477282993728295
0.006325159018160775                                0.006486636004410684
0.006394861004082486                                0.006487586011644453
0.006408912013284862                                0.0065103889792226255
0.006430254987208173                                0.006511708983452991
0.006437242991523817                                0.0065261260024271905
0.006453774985857308                                0.006528272002469748
0.006474898982560262                                0.006530279002618045
0.0064962680044118315                               0.006540709000546485
0.006502891978016123                                0.006564592011272907
0.0065493670117575675                               0.006577224005013704
0.006553015991812572                                0.006607293005799875
0.006558501976542175                                0.006660646991804242
0.006698187004076317                                0.006685447006020695
0.006729554006597027                                0.006690582988085225
0.006777674017939717                                0.0067324970150366426
0.0068738860136363655                               0.006748925021383911
0.006891846976941451                                0.006891222990816459
0.00697691401001066                                 0.007094986009178683
```
**Conclusion:**
Code runs faster when we generate lists "on the fly". 
