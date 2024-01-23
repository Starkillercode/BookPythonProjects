#this is an example of book store using boolean operators
print('Please provide next data to help with your search')
name = input('Please provide the name of the book: ')
id = int(input('Please provide the serial number: '))
price = float(input('Please provide the price of the book: '))
delivery = input('Please specify if it includes free delivery with True/False: ')
if delivery == True:
    print('True')
elif delivery == False:
    print('False')
else:
    delivery = 'The answer is incorrect, please whrite True/False'
print(f'''
Book Title: {name} 
ID Number: {id}
Price: {price}
Free Delivery: {delivery}''')