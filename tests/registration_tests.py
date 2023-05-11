from functions_for_test.elements_test import RegistrationPage


def test_complete_registration_demoqa():
    # открытие регистрации
    registration_page = RegistrationPage()
    registration_page.open()
    # заполнение формы
    registration_page.fill_first_name("Albert")
    registration_page.fill_last_name("Ivanov")
    registration_page.fill_email("ALLIIVAN@mail.ru")
    registration_page.fill_number("8954567689")
    registration_page.choice_gender('Male')
    registration_page.fill_date_of_birth('1993', 'December', '28')
    registration_page.choice_subject('Physics')
    registration_page.choice_hobbies('Sports')
    registration_page.choice_hobbies_more('Reading')
    registration_page.choice_hobbies_more_more('Music')
    registration_page.file_pictures('pictures.jpg')
    registration_page.fill_adress('Pharabi street 18')
    registration_page.fill_state('Rajasthan')
    registration_page.fill_city('Jaipur')

    # THEN
    # проверка формы
    registration_page.assert_register_user_info(
        'Albert Ivanov',
        'ALLIIVAN@mail.ru',
        'Male',
        '8954567689',
        '28 November,1993',
        'Physics',
        'Sports, Reading, Music',
        'pictures.jpg',
        'Pharabi street 18',
        'Rajasthan Jaipur')
