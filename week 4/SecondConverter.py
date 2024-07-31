"""secondconverter"""
def main():
    """Main"""
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    hours = (k // (s * m)) % h
    remaining_seconds = k % (s * m)
    minutes = remaining_seconds // s
    seconds = remaining_seconds % s
    print(f"{hours}:{minutes}:{seconds}")
main()
