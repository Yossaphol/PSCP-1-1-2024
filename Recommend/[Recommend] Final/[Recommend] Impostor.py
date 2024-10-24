"""imposter"""
import json
def main():
    """main"""
    among = {}
    dead = {}
    alive = {}
    impos = 0
    while True:
        name = input()
        if name == 'End':
            break
        if name == 'Start':
            continue
        if name[0] == '{':
            among.update(json.loads(name))
        else:
            dead.update({name: among[name]})
    for i in among:
        if i in dead:
            continue
        else:
            alive.update({i : among[i]})
    for i in alive:
        if alive[i] == 'Impostor':
            impos += 1
    print(f"{impos} Impostor Remains")
    print('***Alive***')
    for i in sorted(alive.items(), key=lambda item: item[0]):
        print(f"{i[0]} : {i[1]}")
    print('***Dead***')
    for i in sorted(dead.items(), key=lambda item: item[0]):
        print(f"{i[0]} : {i[1]}")
main()
