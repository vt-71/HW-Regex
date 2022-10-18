import re

def name_correct(contacts_list):
# Функция приводит ФИО к формату имя, фамилия, отчество
    result_list = []
    for contact in contacts_list[1:]:
        name_list = []
        person = ' '.join(contact[0:3])
        person = person.rstrip().split()
        if len(person) < 3:
            person.extend(' ')
        for i in range(len(person)):
            name_list.insert(i,person[i])
        name_list= name_list + contact[3:]
        result_list.append(name_list)
    return(result_list)


def unit_same(result_list):
# Функция объединяет строки с одинаковыми именем и фамилией. Что-то мне подсказывает, что можно было сделать проще))
    for person in result_list:
        for next_person in result_list[(result_list.index(person) + 1):(len(result_list)-1)]:
            if person [0:1] == next_person[0:1]:
                for index in range(7):
                    unit_data= []
                    for data_1,data_2 in zip(person,next_person):
                        if data_1 == '' or data_2 == '':
                            unit = data_1 + data_2
                            unit_data.insert(index,unit)
                        elif data_1 == '':
                            unit_data.insert(index,data_2)
                        else:
                            unit_data.insert(index,data_1)
                result_list.pop(result_list.index(person))    
                result_list.remove(next_person)    
                result_list.append(unit_data)
    return(result_list)           



def phone_correct (result_list):
# Функция приводит номера телефонов к единому формату.
    for person in result_list:    
        pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
        substitution = r"+7(\2)\3-\4-\5 \6\7"
        result = re.sub(pattern, substitution, person[5])
        person.pop(5)
        person.insert(5,result.strip())
    headers = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    result_list.insert(0,headers)
    return(result_list)