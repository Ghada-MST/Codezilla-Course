import re


def mail_validate():
  try:
    with open("emails.txt") as f:
      all_mails = f.read()
    with open("Validated_mails", "w") as f:
      validated_mails = re.findall(r"[\w\.\-]+@[A-Za-z0-9\-\.]+\.com",
                                   all_mails)
      mails = "\n".join(validated_mails)
      f.write(f'Validated_mails:\n___________________ \n{mails}')
    with open("Non_Validated_mails", "w") as f:
      all_mails_lst = all_mails.split("\n")
      f.write('Non Validated mails:\n__________________\n')
      for mail in all_mails_lst:
        if not mail in validated_mails:
          f.write(f'{mail}\n')
  #errors
  #No Such File Or Directory
  # Not Readable
  # Not Writable
  except OSError as error:
    print(error)


mail_validate()
