import random
import selenium
from faker import Faker
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def adicionar_livros():
    URL = "http://127.0.0.1:8000/books/"
    driver = Chrome()
    driver.get(URL)
    driver.maximize_window()
    faker = Faker('pt_BR')
    id_book = faker.first_name()
    title = ' '.join(faker.words(nb=4)).capitalize()
    author = faker.name()
    release_year = random.randint(1900, 2025)
    state = random.choice([
        "Acre", "Alagoas", "Amapá", "Amazonas",
        "Bahia", "Ceará", "Distrito Federal",
        "Espírito Santo", "Goiás", "Maranhão",
        "Mato Grosso", "Mato Grosso do Sul",
        "Minas Gerais", "Pará", "Paraíba", "Paraná",
        "Pernambuco", "Piauí", "Rio de Janeiro", "Rio Grande do Norte",
        "Rio Grande do Sul", "Rondônia",
        "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins"
    ])
    pages = random.randint(50, 1000)
    publishing_company = faker.company()
    create_at = faker.date()

    sleep(1)
    driver.find_element(By.NAME, "title").send_keys(title)
    sleep(1)
    driver.find_element(By.NAME, "author").send_keys(author)
    sleep(1)
    driver.find_element(By.NAME, "release_year").send_keys(release_year)
    sleep(1)
    driver.find_element(By.NAME, "state").send_keys(state)
    driver.find_element(By.NAME, "pages").send_keys(pages)
    driver.find_element(By.NAME, "publishing_company").send_keys(publishing_company)
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//button[text()="POST"]')
    ))
    button.click()


if __name__ == '__main__':
    adicionar_livros()