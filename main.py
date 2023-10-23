def create_script_file(filename, website):

    template = '''DELAY 1000
GUI r
DELAY 200
STRING powershell Start-Process "{}"
DELAY 500
ENTER
'''

    code = template.format(website)

    if not filename.endswith('.txt'):
        filename += '.txt'

    with open(filename, 'w') as file:
        file.write(code)

filename = input("Enter the file name: ")

website = input("Enter the website link: ")

create_script_file(filename, website)

print(f"Script file '{filename}' has been created.")
