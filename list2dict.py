def main():
    friends_lst = ['Noah', '1234567', 'Anooshree', '2347891', '9371924', 'Mel', '2398712']
    list_to_dict(friends_lst)

def list_to_dict(friends_lst):
    num_lst = []
    phone_nums = {}
    for elem in friends_lst:
        if elem.isnumeric():
            print(elem)
            if elem.isalpha():
                break
            num_lst.append(elem)
            print(num_lst)
        
        if elem.isalpha():
            # print(elem)
            name = elem
            if name not in phone_nums.keys():
                phone_nums[name] = num_lst

    print(phone_nums)
    






if __name__ == '__main__':
    main()