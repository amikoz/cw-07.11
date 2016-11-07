import json

def func():
    d = {'Собака': '- это домашнее животное', 'Пенал': ' - это ящичек для ручек, карандашей, перьев и т. п.', 'Dog': ' is a domesticated canine which has been selectively bred over millennia for various behaviours, sensory capabilities, and physical attributes'}
    f = open('data.json', 'w', encoding = 'utf-8')
    json.dump(d, f, ensure_ascii = False)
    f.close()

def func1():
    f = open('data.json','r', encoding = 'utf-8')
    d = json.load(f)
    f.close
    return d
def main():
    g = func()
    func1()
if __name__ == '__main__':
    main()


