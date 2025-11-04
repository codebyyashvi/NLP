import re

# chat1 = 'codebasics: you ask lot of questions 1235678912, abc@xyz.com, 9998881234'
# chat2 = 'codebasics: here it is: (123)-567-8912, abc_82@xyz.com'
# chat3 = 'codebasics: yes, phone: 1235678912 email:abc@xyz.com'

# # pattern = r'\d{10}'
# # pattern = r'\d{10}|\(\d{3}\)-\d{3}-\d{4}' # for phone number
# pattern = r'[a-z0-9A-Z_]*@[a-z0-9A-Z]*\.[a-zA-Z]*' # for email
# matches = re.findall(pattern, chat2)
# email = matches[0]
# # print(matches) 
# print(email)

# chat1 = 'codebasics: Hello, I am having an issue with my order # 412889912'
# chat2 = 'codebasics: I have a problem with my order number 412889912'
# chat3 = 'codebasics: My order 412889912 is having an issue, I was charged 300$ when online it says 280$.'

# pattern = r'order[^\d]*(\d*)'
# matches = re.findall(pattern, chat1)
# order_id = matches[0]
# print(order_id)

text = '''Born	Elon Reeve Musk
June 28, 1971 (age 54)
Pretoria, South Africa
Citizenship	
South Africa
Canada
U.S.
Political party	Independent
Spouses	
Justine Wilson

(​m. 2000; div. 2008)
Talulah Riley

​(m. 2010; div. 2016)
Children	at least 14 (including Vivian Wilson)
Parents	
Errol Musk (father)
Maye Musk (mother)
Relatives	Musk family
Education	University of Pennsylvania (BA, BS)'''

# pattern = r'age (\d+)'
# pattern = r'Born(.*)'
# pattern = r'Born.*\n(.*)\(age'
pattern = r'\(age.*\n(.*)'
matches = re.findall(pattern, text)
born = matches[0].strip()
# print(born)

def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
age = get_pattern_match(r'\(age.*\n(.*)', text)
# print(age)

def get_personal_information(text):
    age = get_pattern_match(r'age (\d+)', text)
    full_name = get_pattern_match(r'Born(.*)\n', text)
    birth_date = get_pattern_match(r'Born.*\n(.*)\(age', text)
    birth_place = get_pattern_match(r'\(age.*\n(.*)', text)
    return {
        'age': age,
        'name': full_name.strip(),
        'birth_date': birth_date.strip(),
        'birth_place': birth_place.strip()
    }

print(get_personal_information(text))