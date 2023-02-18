import os
import time

from Loging import Login
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Item(Login):
    # Used to assert the final message after all steps are done
    item_list_names = []
    item_list_prices = []
    final_price = 0
    final_country = ""
    final_city = ""
    final_street = ""

    def __init__(self, driver=r"/home/balor/Documents/Pyp/EVERYTHING_ELSE/Chrome_Drive"):
        try:
            self.driver = driver
            os.environ['PATH'] += self.driver
            super(Item, self).__init__(driver)
            f = open("Test", "a")
            f.write("Setup-Item - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Setup-Item - FAIL\n")
            f.close()

    # Gets all the items and their prices and stores them in the class variables( item_list_names, item_list_prices)
    def get_all_items(self, item_class_name="//span[@class='shop-item-title']",
                      item_class_price="//span[@class='shop-item-price']"):
        """
        Gets the items and prices from 1 page of a website

        :param item_class_name: <str> XPATH to all item names, default set for the used site
        :param item_class_price: <str> XPATH to all item prices, default set for the used site
        :return: self
        """
        if not isinstance(item_class_name, str) or not (item_class_price, str):
            f = open("Test", "a")
            f.write("Get_all_Items - Fail\n")
            f.close()
            raise AttributeError("both params must be type<str>")
        else:
            for i in range(1):
                item_name = self.find_elements(By.XPATH, item_class_name)
                item_price = self.find_elements(By.XPATH, item_class_price)
                for p in item_name:
                    self.item_list_names.append(p.text)
                for o in item_price:
                    self.item_list_prices.append(o.text)
            # removes the $ sign from the prices
            for i in range(len(self.item_list_prices)):
                self.item_list_prices[i] = float(self.item_list_prices[i].replace("$", ''))
            # dict used to print items and price combinations, mostly for info purposes
            # item_dict = {self.item_list_names[i]: self.item_list_prices[i] for i in range(len(self.item_list_prices))}
            f = open("Test", "a")
            f.write("Get-items - PASS\n")
            f.close()
        time.sleep(5)
        return self

    # Adds specified items to cart
    def add_item_to_cart(self, *args):
        """
        Adds specific items in the cart, the args must be strings matching the title of the item
        The webpage does not accept multiple add to cart for the same item

        :param args: <str> Specific Items from the item_list_name class variable, must be strings
        :return: self
        """
        WebDriverWait(self, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary shop-item-button']")))
        lista = list(self.find_elements(By.XPATH, "//button[@class='btn btn-primary shop-item-button']"))[:]
        for i in args:
            for elem in self.item_list_names:
                if i == elem:
                    lista[self.item_list_names.index(elem)].click()
        f = open("Test", "a")
        f.write("ADD_to_CART - PASS\n")
        f.close()
        time.sleep(5)
        return self

    # changes the quantity of the items already in the cart
    def change_item_quantity(self, *args: int):
        """
        Changes the quantity of any item already in the list
        It will start with the first item in the list and set the quantity
        It needs to have fewer or equal number of args as the add to cart function

        :param args: <int> The quantity of each function
        :return: self
        """
        for arg in args:
            if not isinstance(arg, int):
                f = open("Test", "a")
                f.write("Change_Quantity - FAIL\n")
                f.close()
                raise AttributeError("all params must be type<int>")

        WebDriverWait(self, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='cart-quantity-input']")))
        lista = list(self.find_elements(By.XPATH, "//input[@class='cart-quantity-input']"))[:]
        for elem in args:
            lista[args.index(elem)].click()
            lista[args.index(elem)].send_keys(Keys.BACKSPACE)
            lista[args.index(elem)].send_keys(elem)
            lista[args.index(elem)].send_keys(Keys.ENTER)
        f = open("Test", "a")
        f.write("Change_Quantity - PASS\n")
        f.close()
        time.sleep(5)
        return self

    # removes specified items from the cart
    def remove_item_from_cart(self, *args: int):
        """
        Removes specified items from the shopping cart
        Each argument specifies the position of the item to be removed
        Must not have more args than number of items currently in the cart
        No arg can be larger than the number of items currently in the cart

        :param args: <int> Position of the item to be removed
        :return: self
        """
        for elem in args:
            if not isinstance(elem, int):
                f = open("Test", "a")
                f.write("Change_Quantity - FAIL\n")
                f.close()
                raise AttributeError("all params must be type<int>")
        WebDriverWait(self, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-danger']")))
        for elem in reversed(args):
            self.find_element(By.XPATH,
                              f"/html/body/div/div/div[2]/section[1]/div[2]/div[{elem}]/div[2]/button").click()
        f = open("Test", "a")
        f.write("Remove_Item - PASS\n")
        f.close()
        time.sleep(5)
        return self

    # Calculates the total price in the cart and passes it to the final_price class variable
    def get_total_price(self):
        try:
            total_price = self.find_element(By.XPATH, "//span[@class='cart-total-price']")
            total_price = float(total_price.text.replace("$", ''))
            self.final_price = total_price
            f = open("Test", "a")
            f.write("Get_total_Price - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Get_total_Price - FAIL\n")
            f.close()

        return self

    # presses the checkout button
    def check_out_click(self):
        try:
            self.find_element(By.XPATH, "//button[@class='btn btn-primary btn-purchase']").click()
            f = open("Test", "a")
            f.write("Check_out_btn - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Check_out_btn - FAIL\n")
            f.close()
        time.sleep(5)
        return self

    # fills the checkout form
    def check_out_form_filler(self, phone_num: int, city: str, street: str):
        """
        Fills the checkout form

        :param phone_num: (int)
        :param city: (str)
        :param street: (str)
        :return: self
        """
        try:
            WebDriverWait(self, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[1]/h2")))
            self.final_street = street
            self.final_city = city
            insert_phone_num = self.find_element(By.ID, "phone")
            insert_street = self.find_element(By.NAME, "street")
            insert_city = self.find_element(By.NAME, "city")

            insert_phone_num.clear()
            insert_street.clear()
            insert_city.clear()

            insert_phone_num.send_keys(phone_num)
            insert_street.send_keys(street)
            insert_city.send_keys(city)
            f = open("Test", "a")
            f.write("Fill Checkout - PASS\n")
            f.close()
        except TimeoutError:
            f = open("Test", "a")
            f.write("Fill Checkout - FAIL\n")
            f.close()
        time.sleep(5)
        return self

    # select the country from the dropdown
    def country_drop_down(self, country: str):
        """
        Selects the country in the dropdown, country must exist in the dropdown

        :param country: (str) Country
        :return: self
        """
        try:
            self.final_country = country
            select_country = self.find_element(By.ID, "countries_dropdown_menu")
            choice = Select(select_country)
            choice.select_by_visible_text(country.capitalize())
            f = open("Test", "a")
            f.write("Drop_Down - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Drop_Down - FAIL\n")
            f.close()
        time.sleep(5)
        return self

    # clicks submit
    def submit_btn_clk(self):
        try:
            self.find_element(By.ID, "submitOrderBtn").click()
            f = open("Test", "a")
            f.write("Submit_btn - PASS\n")
            f.close()
        except:
            f = open("Test", "a")
            f.write("Submit_btn - FAIL\n")
            f.close()
        time.sleep(5)
        return self

    # checks if the correct message is displayed after submitting the order
    def final_message(self):
        try:
            final_text = WebDriverWait(self, 15).until(EC.presence_of_element_located((By.ID, "message")))
            if final_text.text == f"Congrats! Your order of ${self.final_price} has been registered and will be " \
                                  f"shipped to {self.final_street}, {self.final_city} - {self.final_country}.":
                f = open("Test", "a")
                f.write("final_message - PASS\n")
                f.close()
            else:
                f = open("Test", "a")
                f.write("final_message - FAIL\n")
                f.close()
        except:
            f = open("Test", "a")
            f.write("final_message - Fail\n")
            f.close()