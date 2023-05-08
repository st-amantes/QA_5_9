import os
from selene import browser, have, command


class RegistrationPage:
    def __init__(self):
        self.state = browser.all('[id^=react-select][id*=option]')
        self.adress = browser.element('#currentAddress')

    def open(self):
        browser.driver.set_window_size(1920, 1080)
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.fullscreen_window()

    def file_pictures(self, file_name):
        browser.element('#uploadPicture').send_keys(os.path.abspath(f'../resources/{file_name}'))

    def fill_first_name(self, value):
        browser.element('#firstName').send_keys(value)

    def fill_last_name(self, value):
        browser.element('#lastName').send_keys(value)

    def fill_email(self, value):
        browser.element('#userEmail').send_keys(value)

    def fill_number(self, value):
        browser.element('#userNumber').send_keys(value)

    def choice_gender(self, value):
        browser.element('[name = gender][value = Male]+label').click()

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').send_keys(month)
        browser.element('.react-datepicker__year-select').send_keys(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def choice_subject(self, value):
        browser.element('#subjectsInput').send_keys(value).press_enter()

    def resource_path(file_name):
        return os.path.abspath(f'../QA_5_9/resources/{file_name}')

    def choice_hobbies(self, value):
        browser.all('[for = hobbies-checkbox-1]').element_by(have.exact_text(value)).click()

    def choice_hobbies_more(self, value):
        browser.all('[for = hobbies-checkbox-2]').element_by(have.exact_text(value)).click()

    def choice_hobbies_more_more(self, value):
        browser.all('[for = hobbies-checkbox-3]').element_by(have.exact_text(value)).click()

    def assert_register_user_info(self, full_name,
                                  email, gender,
                                  number, day_brith,
                                  subject, hobbies,
                                  picture, adress, city):
        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {email}',
            f'Gender {gender}',
            f'Mobile {number}',
            f'Date of Birth {day_brith}',
            f'Subjects {subject}',
            f'Hobbies {hobbies}',
            f'Picture {picture}',
            f'Address {adress}',
            f'State and City {city}',
        ))

    def fill_adress(self, adress):
        self.adress.perform(command.js.scroll_into_view)
        self.adress.send_keys(adress)
        browser.element('#state').click()

    def fill_state(self, state):
        self.state.element_by(have.exact_text(state)).click()
        browser.element('#city').click()

    def fill_city(self, city):
        self.state.element_by(have.exact_text(city)).click()
        browser.element('#submit').perform(command.js.click)
