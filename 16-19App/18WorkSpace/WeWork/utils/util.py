from faker import Faker


class Fake:
    fake = Faker('zh_CN')

    @classmethod
    def name(self):
        return self.fake.name()

    @classmethod
    def tel(self):
        return self.fake.phone_number()
