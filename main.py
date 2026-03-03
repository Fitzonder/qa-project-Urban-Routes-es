import data
import CodeRetrieve
from PageLocators import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        edge_options = webdriver.EdgeOptions()
        edge_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        edge_options.set_capability("ms:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Edge(options=edge_options)
        cls.driver.execute_cdp_cmd("Network.enable", {})

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.from_field, address_from))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_selection(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.comfort_button_title))
        routes_page.select_comfort_tariff()
        assert self.driver.find_element(*UrbanRoutesPage.comfort_button_title).text == 'Comfort'

    def test_fill_phone_field(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        phone_number = data.phone_number
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.number_field_module))
        routes_page.fill_phone_number(phone_number)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.phone_code_field))
        def _phone_code_ready(driver):
            try:
                code = CodeRetrieve.retrieve_phone_code(driver)
                return code if code else False
            except Exception:
                return False

        phone_code = WebDriverWait(self.driver, 20, 1).until(_phone_code_ready)
        self.driver.find_element(*UrbanRoutesPage.phone_code_field).send_keys(phone_code)
        routes_page.confirm_phone_code()
        assert phone_code.isdigit()

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        card_number = data.card_number
        card_code = data.card_code
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.payment_field))
        routes_page.add_credit_card(card_number, card_code)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.payment_choice))
        assert 'Tarjeta' in self.driver.find_element(*UrbanRoutesPage.payment_choice).text

    def test_set_driver_comment(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        driver_comment = data.message_for_driver
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.driver_message_field))
        routes_page.write_message_for_driver(driver_comment)
        assert self.driver.find_element(*UrbanRoutesPage.driver_message_field).get_property("value") == driver_comment

    def test_request_blanket(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.comfort_button_title))
        routes_page.select_comfort_tariff()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesPage.mantas_slider))
        routes_page.request_blanket()
        assert routes_page.is_manta_selected(), "No esta seleccionada la casilla de Manta y panuelos"

    def test_request_ice_creams(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.comfort_button_title))
        routes_page.select_comfort_tariff()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.ice_cream_counter))
        routes_page.request_ice_creams()
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(UrbanRoutesPage.ice_cream_chosen, "2"))
        assert routes_page.get_ice_cream_count() == '2'

    def test_taxi_request(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.from_field))
        routes_page.set_route(address_from, address_to)
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element_value(UrbanRoutesPage.to_field, address_to))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.ask_taxi_button))
        routes_page.ask_taxi_option()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.comfort_button_title))
        routes_page.select_comfort_tariff()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(UrbanRoutesPage.send_taxi_request))
        routes_page.request_taxi()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.diver_information))
        assert routes_page.is_send_request_button_displayed(), "No esta habilitado aun el boton para pedir taxi"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

