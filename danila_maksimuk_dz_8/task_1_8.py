import  re


def email_parse(email: str):
    e_mail = re.compile(r'(?P<name>[a-zA-Z0-9-_.]+)@(?P<our_domain>[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')
    result = e_mail.match(email)
    if not result:
        raise ValueError(f'please check e-mail format for {email}')
    our_dict = result.groupdict()
    return our_dict



if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
    email_parse('someone@geekbrainsru')
