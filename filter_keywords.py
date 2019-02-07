import os


def clean(data):
    results = []
    for i in set(data):
        temp = i

        temp = ''.join([i for i in temp if i not in ['(', ')', ',', '.']])
        temp = ''.join([i for i in temp if not i.isdigit()])

        results.append(temp)
    return results


if __name__ == "__main__":
    os.chdir('webpages')
    for dir in os.listdir(os.getcwd()):
        os.chdir(os.path.join(os.getcwd(), dir))
        print('Cleaning ', os.path.join(os.getcwd(), 'keywords.txt'))

        file = open(os.path.join(os.getcwd(), 'keywords.txt'), 'r')
        data = file.readlines()
        file.close()

        file = open(os.path.join(os.getcwd(), 'keywords.txt'), 'w')
        for i in clean(data):
            file.write(i)
        os.chdir('..')
        file.close()
