# _*_coding:utf-8_*_
import poplib
email = input('email: ')
password = input('password: ')
pop3_server = input('POP3 server: ')

server = poplib.POP3(pop3_server)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('message: %s. Size: %s' % servre.stat())
resp,mails,octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parserstr(msg_content)
server.quit()