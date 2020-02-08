"""
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.
"""

def word_counter(x):
    counter=[]
    for item in x:
        item=item.split()
        for i in item:
            if len(i)<2:
                item.remove(i)
        counter.append(len(item))
    return counter


with open('data/task2.data','r') as f:
    user_list=f.readlines()
    print(f'Количество строк: {len(user_list)}')

for sentence, num in zip(user_list,word_counter(user_list)):
    print(f'{sentence[:-2]} ::: содержится {num} слов в предложении.')