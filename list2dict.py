def main():
    friends_lst = ['Noah', '1234567', 'Anooshree', '2347891', '9371924', 'Mel', '2398712']
    list_to_dict(friends_lst)

def list_to_dict(friends_lst):
    phone_nums = {}
    for elem in friends_lst:
        if elem.isnumeric():
            print(elem)
        # if elem.isalpha():
        #     print(elem)
            # if elem not in phone_nums.keys():
            #     phone_nums[elem]
    








if __name__ == '__main__':
    main()