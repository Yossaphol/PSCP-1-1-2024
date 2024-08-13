"""ValidVar"""
def main():
    '''main'''
    n = int(input())
    for _ in range(n):
        txt = input().strip()
        if not txt.isidentifier() or txt in ['if','else','elif','while','for','True','False',\
                                             'continue','break','return','is', 'in','and','or',\
                                                'from','as','pass','not','def','None']:
            print('Invalid')
        else:
            print('Valid')
main()
