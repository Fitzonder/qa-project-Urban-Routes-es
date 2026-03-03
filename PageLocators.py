from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Localizadores
    ask_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_button_title = (By.XPATH, "//*[contains(@class,'tcard-title') and normalize-space()='Comfort']")
    number_field_module = (By.CLASS_NAME, 'np-text')
    add_phone = (By.ID, 'phone')
    phone_next_button = (By.CSS_SELECTOR, '.button.full')
    phone_text = (By.CSS_SELECTOR, '.np-text')
    phone_code_field = (By.ID, 'code')
    code_confirm_button = (By.XPATH, "//button[@class='button full']")
    payment_field = (By.CSS_SELECTOR, '.pp-button.filled')
    add_card_button = (By.CSS_SELECTOR, '.pp-row.disabled')
    card_number = (By.ID, 'number')
    code_card = (By.ID, 'code')
    enable_add_button = (By.CLASS_NAME, 'pp-separator')
    added_card_button = (By.CSS_SELECTOR, '.button.full')
    close_window_button = (By.CSS_SELECTOR, '.close-button.section-close')
    payment_choice = (By.CSS_SELECTOR, '.pp-value-text')
    driver_message_field = (By.ID, 'comment')
    mantas_slider = (By.XPATH, "//span[@class='slider round']")
    ice_cream_counter = (By.CLASS_NAME, 'counter-plus')
    ice_cream_chosen = (By.CSS_SELECTOR, '.counter-value')
    send_taxi_request = (By.CLASS_NAME, 'smart-button-main')

    # Validaciones de modales
    search_taxi_modal = (By.CSS_SELECTOR, '.order-header')
    driver_info_modal = (By.CSS_SELECTOR, '.order-body')
    diver_information = (By.CLASS_NAME, 'order-header-title')

    def __init__(self, driver, timeout=10):
        self.driver = driver


    #Esta función lo que hace es diligenciar los dos campos a la vez.
    def set_route(self, address_from, address_to):
        self.driver.find_element(*self.from_field).send_keys(address_from)
        self.driver.find_element(*self.to_field).send_keys(address_to)

    #Función que solo rellena el campo "from"
    def set_from(self, address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    #Función que solo rellena el campo "to"
    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    #Función que permite recuperar la información suministrada.
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    # Función que permite recuperar la información suministrada.
    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    #Pedir el taxí
    def ask_taxi_option(self):
        return self.driver.find_element(*self.ask_taxi_button).click()

    #Seleccionar tarifa comfort
    def select_comfort_tariff(self):
        self.driver.find_element(*self.comfort_button_title).click()

    #Agregar número de teléfono
    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.number_field_module).click()
        self.driver.find_element(*self.add_phone).send_keys(phone_number)
        self.driver.find_element(*self.phone_next_button).click()

    #Confirmar número de teléfono
    def confirm_phone_code(self):
        for button in self.driver.find_elements(*self.code_confirm_button):
            if button.is_displayed() and button.is_enabled():
                button.click()
                return
        raise Exception("No se encontró un botón de confirmación de teléfono interactuable.")

    #Agregar tarjeta
    def add_credit_card(self, card_number, card_code):
        payment_button = self.driver.find_element(*self.payment_field)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", payment_button)
        payment_button.click()
        self.driver.find_element(*self.add_card_button).click()

        card_number_input = next(
            (el for el in self.driver.find_elements(*self.card_number) if el.is_displayed() and el.is_enabled()),
            None
        )
        card_code_input = next(
            (el for el in self.driver.find_elements(*self.code_card) if el.is_displayed() and el.is_enabled()),
            None
        )
        if not card_number_input or not card_code_input:
            raise Exception("No se encontraron campos interactuables para número/código de tarjeta.")

        card_number_input.send_keys(card_number)
        card_code_input.send_keys(card_code)
        # Saca foco del input para disparar validaciones del formulario.
        card_code_input.send_keys(Keys.TAB)

        add_button = next(
            (el for el in self.driver.find_elements(*self.added_card_button) if el.is_displayed() and el.is_enabled()),
            None
        )
        if not add_button:
            raise Exception("No se encontró el botón para agregar tarjeta habilitado.")
        add_button.click()

    #Enviar mensaje a conductor
    def write_message_for_driver(self, driver_comment):
        message_input = self.driver.find_element(*self.driver_message_field)
        message_input.clear()
        message_input.send_keys(driver_comment)

    #Seleccionar manta
    def request_blanket(self):
        slider = self.driver.find_element(*self.mantas_slider)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", slider)
        try:
            slider.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", slider)

    #Sleccionar dos helados
    def request_ice_creams(self):
        self.driver.find_element(*self.ice_cream_counter).click()
        self.driver.find_element(*self.ice_cream_counter).click()

    def get_ice_cream_count(self):
        return self.driver.find_element(*self.ice_cream_chosen).text

    #Regresará "true" si la manta está seleccionada
    def is_manta_selected(self):
        slider = self.driver.find_element(*self.mantas_slider)
        checkbox = slider.find_element(By.XPATH, "./preceding-sibling::input[@type='checkbox'][1]")
        return checkbox.is_selected()

   #Regresará "true" si el botón de pedido de taxí está disponible
    def is_send_request_button_displayed(self):
        return self.driver.find_element(*self.send_taxi_request).is_displayed()

    #Termina la tarea pidiendo finalmente el taxi
    def request_taxi(self):
        self.driver.find_element(*self.send_taxi_request).click()
