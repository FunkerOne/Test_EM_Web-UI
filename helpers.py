from faker import Faker


class PersonalInformationData:

    @staticmethod
    def first_name_gen():
        fake = Faker()
        first_name = fake.first_name()
        return first_name

    @staticmethod
    def last_name_gen():
        fake = Faker()
        last_name = fake.last_name()
        return last_name

    @staticmethod
    def zip_code_gen():
        fake = Faker()
        zip_code = fake.zipcode()
        return zip_code
