"""Big Frame"""
def main():
    """Main Function"""
    line1 = str(input()).strip()
    line2 = str(input()).strip()
    line3 = str(input()).strip()
    line4 = str(input()).strip()
    line5 = str(input()).strip()
    space = len(line1)
    if space < len(line2):
        space = len(line2)
    if space < len(line3):
        space = len(line3)
    if space < len(line4):
        space = len(line4)
    if space < len(line5):
        space = len(line5)
    print("*" * (space + 4))
    print(f"* {line1:<{space}} *")
    print(f"* {line2:<{space}} *")
    print(f"* {line3:<{space}} *")
    print(f"* {line4:<{space}} *")
    print(f"* {line5:<{space}} *")
    print("*" * (space + 4))
main()
