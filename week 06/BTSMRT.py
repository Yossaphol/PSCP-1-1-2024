"""BTSMRT"""
def main():
    """Main Function"""
    day = str(input())
    age = float(input())
    height = float(input())
    if day == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
    elif day == "Children Day":
        if age < 14 and height <= 140:
            print("FREE")
        else:
            print("PAY")
    elif day == "Senior Day":
        if age >= 60 or (age < 14 and height < 90):
            print("FREE")
        else:
            print("PAY")
main()
