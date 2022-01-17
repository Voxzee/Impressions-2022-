import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  
sender_email = "my@gmail.com"
password = input("Type your password and press enter: ")


context = ssl.create_default_context()


try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() 
    server.starttls(context=context) 
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 