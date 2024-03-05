# Generated by Selenium IDE
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from helpers.base_test import BaseTest


@allure.title("Тестовое задание от компании Тензор")
@allure.description("Сравнение размеров картинок в блоке 'Работаем'")
class TestDefaultSuite(BaseTest):

    sbis_window = {}
    tenzor_window={}

    def test_first_scenario(self, driver):
        self.sbis_home_page.open()
        print("self.sbis_home_page.click_to_contacts_link()")
        self.sbis_home_page.click_to_contacts_link()
        print("self.sbis_contacts_page.is_opened()")
        self.sbis_contacts_page.is_opened()
        print("self.sbis_contacts_page.click_to_tensor_banner()")
        self.sbis_window = driver.current_window_handle
        print("self.sbis_window = driver.current_window_handle")
        self.sbis_contacts_page.click_to_tensor_banner()
        print("self.sbis_contacts_page.click_to_tensor_banner()")
        self.tensor_home_page.switch_to_self(self.sbis_window)
        print("self.tensor_home_page.switch_to_self(self.sbis_window)")
        self.tensor_window = driver.current_window_handle
        print("self.tensor_window = driver.current_window_handle")
        self.tensor_home_page.is_opened()
        print(" self.tensor_home_page.is_opened()")
        self.tensor_home_page.is_working_block_present()
        print("self.tensor_home_page.is_working_block_present()")
        self.tensor_home_page.is_details_present()
        print("self.tensor_home_page.is_details_present")
        self.tensor_home_page.click_to_details_link()
        print("self.tensor_home_page.click_to_details_link()")
        self.tensor_about_page.is_opened()
        print("self.tensor.about_bage.is_opened()")
        self.tensor_about_page.is_working_block_present()
        print("self.tensor_about_page.is_working_block_present()")
        self.tensor_about_page.check_images_same_size()
        print("self.tensor_about_page.check_images_same_size()")
