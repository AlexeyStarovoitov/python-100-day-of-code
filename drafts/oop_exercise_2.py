class BaseException(Exception):
    pass

class InputError(BaseException):
    def __init__(self, name, *args, **kwargs):
        print(f'{name} is not unique')
        super(BaseException, self).__init__(args, kwargs)

class AgeError(BaseException):
    def __init__(self, age, *args, **kwargs):
        print(f'{age} is not positive')
        super(BaseException, self).__init__(args, kwargs)

class UnderAgeError(BaseException):
    def __init__(self, name, *args, **kwargs):
        print(f'{name} is an underaged person')
        super(BaseException, self).__init__(args, kwargs)

class EmailError(BaseException):
    def __init__(self, email, *args, **kwargs):
        print(f'{email} is incorrect')
        super(BaseException, self).__init__(args, kwargs)
        

def parse_email(email):
    parse_result = email.count('@') == 1 and len(email.split(sep='@')) == 2
    return parse_result

if __name__ == '__main__':
    data_set = [{'name':'Mark', 'age':35, 'email': 'mark@zuckerberg.com'}, \
                {'name':'Joe', 'age':15, 'email': 'joe@little.com'}, \
                {'name':'alex', 'age':26, 'email':'alex@@olvoight.ru'}, \
                {'name':'mark', 'age':23, 'email':'mark@ordirnary.com'}]
                
    directory = []
    for data in data_set:
        try:
            for dir_data in directory:
                if dir_data['name'].upper() == data['name'].upper():
                    raise InputError(dir_data['name'])
            
            if data['age'] <= 0:
                raise AgeError(data['name'])
            
            if data['age'] < 16:
                raise UnderAgeError(data['name'])
                
            if parse_email(data['email']) == 0:
                raise EmailError(data['email'])
            
        except (InputError, AgeError, UnderAgeError, EmailError):
            continue
            
        directory.append(data)
    
    print('\n')
    print(f'Directory content:\n{directory}')
            
        
