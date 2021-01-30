# Nomad-Coder-Python-Challenge

Nomad Coder Python 2 weeks Challenge.

## Tasks

- [x] Day 1 Quiz.
- [x] Day 2 Code Challenge.
- [x] Day 3 Code Challenge.
- [x] Day 4 Code Challenge.
- [x] Day 5 Code Challenge : Currency Conversion part One.
- [x] Day 6 Code Challenge : Currency Conversion part Two.

### Day 2 Challenge Goals

- This Blueprint code is broken. There are some functions missing, you need to create them. When you run the code, the output must look like this

<img src="https://nomad-coders-assets.s3.amazonaws.com/media/public/django-summernote/2020-04-13/b23ef8d3-eab8-412d-bd66-ea6062ce2b6f.png">

### Day 2 Challenge Conditions

- is_on_list
- get_x
- add_x
- remove_x
- DO NOT change anything inside of the "DO NOT TOUCH AREA"
- 해당 코드에서 빠진 함수가 있습니다. 위의 스크린과 같은 모습이 되도록 고쳐보세요.
- 반드시 위 표기된 함수들 (is_on_list. get_x. add_x. remove_x) 생성해야합니다.
- DO NOT TOUCH 영역은 건들지마세요!

### Day 3 Challenge Goals

- Today's Blueprint code is broken. The functions are incomplete. When you run the code, the output must look like this

<img src="https://nomad-coders-assets.s3.amazonaws.com/media/public/django-summernote/2020-04-14/3f3c2ef1-5eaa-4a94-b913-f10a9c862224.png">

### Day 3 Challenge Conditions

You need to complete the following functions:

- add_to_dict
- get_from_dict
- update_word
- delete_from_dict
- All this functions should check for errors, follow the comments to see all cases you need to cover. There should be NO ERRORS from - Python in the console. NOT change anything inside of the "DO NOT TOUCH AREA"
- 위의 스크린과 같은 모습이 되도록 코드를 고쳐보세요.
- 반드시 위 표기된 함수들 (add_to_dict. get_from_dict. update_word.delete_from_dict) 생성해야합니다.
- DO NOT TOUCH 영역은 건들지마세요!
- 힌트: Dict documentation

### Day 5 Challenge goals

- Using the boilerplate, make a program that gets a list of countries from a website with their currency codes, then let the user choose a country and display the currency code of that country.
- This is part one of a bigger "country scrapping" project we will complete in the following days.

### Day 5 Challenge Conditions

- This is how the program should work:[https://imgur.com/Nh7nkjF]
- The website you should get the countries and currencies from is:[https://www.iban.com/currency-codes]
- Save the name of the country and the "Alpha-3 code" in an array.
- Some countries don't have currency (No universal currency), don't add them to the list.
- Check the user input, only numbers from inside the country list are allowed.
- When a country is selected, show the name and currency code.
- 힌트1: Use try/except when converting strings to numbers. ( int(input()) )
- 힌트2: [https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops]

### Day 6 Challenge Goals:

- Using yesterday's work, extend the functionality to accomplish the following:

### Day 6 Challenge Conditions

- This is how the program should work: [https://i.imgur.com/J7jfXcJ.mp4]
- After getting the countries and their codes let the user choose two countries.
- Then let the user write an amount of currency they want to convert between country a and country b
- Then send the two currency codes and the amounts to a URL like: https://transferwise.com/gb/currency-converter/gbp-to-usd-rate?amount=50
- Use beautiful soup to scrape Transfer Wise to get the result of the conversion.

<img src="https://i.imgur.com/MbpdgXA.png">
