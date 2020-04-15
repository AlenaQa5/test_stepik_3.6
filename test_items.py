from selenium import webdriver
import time


def test_should_see_a_button(browser,language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(7)
    button = browser.find_element_by_css_selector("#add_to_basket_form > .btn")
    have_button = button.text
    print(have_button)
    if language == "fr":
        print(have_button)
        assert have_button == 'Ajouter au panier', 'не нашли кнопку'
        browser.quit()
    else:
        language == "es"
        print(have_button)
        assert have_button == 'Añadir al carrito', 'что-то пошло не так'

