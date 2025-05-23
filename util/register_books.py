from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from time import sleep
import random


class ApiRegisterBook:

    URL = 'http://127.0.0.1:8000/books/'

    def __init__(self):
        self.driver = Chrome()
        self.wait = WebDriverWait(self.driver, 5)
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

    def open(self):
        self.driver.get(self.URL)
        self.driver.maximize_window()
        sleep(1)

    def send_register(self):
        self.wait.until(EC.presence_of_all_elements_located(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip"))
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip")
        if len(buttons) > 2:
            buttons[2].click()
            ActionChains(self.driver).move_to_element(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip").perform()
            self.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "button.btn.btn-primary.js-tooltip"))
            button_post.click()

    def register_books(self):
        for _ in range(5):
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
            self.send_register()

    def close(self):
        self.driver.quit()

if __name__ == '__main__':
    registar_livro = ApiRegisterBook()
    registar_livro.open()
    registar_livro.register_books()
    registar_livro.close()
