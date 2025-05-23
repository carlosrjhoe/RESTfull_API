from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep
import random


class ApiRegisterBook:

    URL = 'http://127.0.0.1:8000/books/'

    def __init__(self):
        self.driver = Chrome()
        self.faker = Faker('pt_BR')
        self.title = (By.NAME, 'title')
        self.author = (By.NAME, 'author')
        self.release_year = (By.NAME, 'release_year')
        self.state = (By.NAME, 'state')
        self.pages = (By.NAME, 'pages')
        self.publishing_company = (By.NAME, 'publishing_company')
        self.estados_brasil = [
            "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
            "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão",
            "Mato Grosso", "Mato Grosso do Sul", "Minas Gerais", "Pará",
            "Paraíba", "Paraná", "Pernambuco", "Piauí", "Rio de Janeiro",
            "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima",
            "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
        ]
        self.button_post = (By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip")

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        sleep(1)

    def register_books(self):
        title = self.faker.sentence(nb_words=4)
        author = self.faker.name()
        release_year = random.randint(1900, 2025)
        state = random.choice(self.estados_brasil)
        pages = random.randint(50, 1000)
        publishing_company = self.faker.company()
        self.driver.find_element(*self.title).send_keys(title)
        self.driver.find_element(*self.author).send_keys(author)
        self.driver.find_element(*self.release_year).send_keys(release_year)
        self.driver.find_element(*self.state).send_keys(state)
        self.driver.find_element(*self.pages).send_keys(pages)
        self.driver.find_element(*self.publishing_company).send_keys(publishing_company)

    def send_register(self):
        buttons = self.driver.find_elements(*self.button_post)
        button_post = buttons[0]
        button_post.click()


if __name__ == '__main__':
    registar_livro = ApiRegisterBook()
    registar_livro.open()
    registar_livro.register_books()
    registar_livro.send_register()
