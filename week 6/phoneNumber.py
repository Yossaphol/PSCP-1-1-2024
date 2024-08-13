"""phone number"""
def main():
    """Main Function"""
    phone = input()
    type_ = input()
    check = len(phone)
    if type_ == 'Domestic':
        if check == 9:
            print(phone[0], phone[1:5], phone[5:])
        elif check == 10:
            print(phone[0:2], phone[2:6], phone[6:])
    else:
        if check == 10:
            print(f"+66{phone[1]} {phone[2:6]} {phone[6:]}")
        else:
            print(f"+66 {phone[1:5]} {phone[5:]}")
main()
