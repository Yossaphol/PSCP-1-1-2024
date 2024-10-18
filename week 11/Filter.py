"""Filter"""
import json
def main(txt, num):
    """main"""
    my_dict = json.loads(txt)
    ans = []
    for i in my_dict:
        if my_dict[i] >= num:
            ans.append(i)
    if ans:
        for i in sorted(ans):
            print(f"{i}\t{my_dict[i]:.2f}")
    else:
        print('Nope')
main(input(), float(input()))
