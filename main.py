# This is a sample Python script.

import csv
# Press ⌥⇧X to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from decimal import Decimal

import matplotlib.pyplot as plt


class Question5:
    def __init__(self):
        self.data_dict = {}
        with open('Assessment_PIBs - modelo 1.csv') as csv_file:
            for line in csv.DictReader(csv_file):
                self.data_dict.update(
                    {
                        line.pop('País'): dict({key: value for key, value in line.items()})
                    }
                )

    def resolve_question_a(self, country: str, year: int):
        country_selected = self.data_dict.get(country)
        if country_selected:
            value = country_selected.get(year)
            if value:
                print(f'PIB {country} em {year}: US${value} trilhões.')
            else:
                print('Ano não encontrado.')
        else:
            print('País não encontrado.')

    def resolve_question_b(self, country: str, year: int):
        ...


class Question4:
    def __init__(self, initial_amount, percent, support_amount, periods):
        self.initial_amount = initial_amount
        self.percent = percent
        self.support_amount = support_amount
        self.periods = periods

    def resolve(self):
        total_amount = self.initial_amount
        x_axis = []
        y_axis = []
        for period in range(self.periods):
            total_amount += (total_amount * self.percent / 100) + self.support_amount
            x_axis.append(period + 1)
            y_axis.append(total_amount)
            print(f'After {period + 1} period(s), the total amount will be: {total_amount:.2f}')

        self.plot_graph(x_axis, y_axis)

    def plot_graph(self, x_axis, y_axis):
        plt.plot(x_axis, y_axis)
        plt.xlabel('X - Total Amount')
        plt.ylabel('X - Periods')
        plt.title('Amount graph')
        plt.show()


def call_question_4():
    initial_amount = Decimal(input('Enter the initial amount: '))
    percent = Decimal(input('Enter the percent: '))
    support_amount = Decimal(input('Enter the support_amount: '))
    periods = int(input('Enter the number of periods: '))
    question4 = Question4(initial_amount, percent, support_amount, periods)
    question4.resolve()


def call_question_5a():
    country_name = input('Enter the country name: ')
    year = input('Enter the year: ')
    Question5().resolve_question_a(country_name, year)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_question_5a()
