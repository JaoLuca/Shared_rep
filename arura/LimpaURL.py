import re

class ExtractURLValues:
    def __init__(self, url) -> None:
        self.url = url

    def urlRegExValidation(self):
        expressao = re.compile('[0-9]{3}')
        busca = expressao.search(self.url)
        print(busca.group())  

        pass

    def __len__(self):
        return len(self.url)
    
    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url


site = ExtractURLValues('https://cursos.alura.com.br/course/string-python-extraindo-informacoes-url/task/91889')
site.urlRegExValidation()
print(len(site))
print(site)
