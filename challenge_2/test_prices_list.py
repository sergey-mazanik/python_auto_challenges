from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


base_url = 'https://magento.softwaretestingboard.com'
page_url = '/gear/bags.html'
ITEM_PRICE: tuple[str, str] = (By.XPATH, '//*[@data-price-type="finalPrice"]/*[@class="price"]')


def test_get_all_prices(driver: WebDriver):
    wait = WebDriverWait(driver, 10, poll_frequency=1)
    driver.get(f'{base_url}{page_url}')
    wait.until(ec.presence_of_element_located(ITEM_PRICE))
    price_list = driver.find_elements(*ITEM_PRICE)
    final_list = [i.text[1:] for i in price_list]
    print(final_list)
