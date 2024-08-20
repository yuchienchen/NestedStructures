def main():
    get_animal_counts('poll.txt')

def get_animal_counts(filename):
    poll = {}
    with open('poll.txt') as file:
        for line in file:
            line = line.strip()
            # print(line)
            parts = line.split(': ')
            name = parts[0]
            vote = parts[-1]
            # print(name)
            # print(vote)
            
            poll[name] = vote

    print(poll)







if __name__ == '__main__':
    main()