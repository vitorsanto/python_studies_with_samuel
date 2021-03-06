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
                print('Year not found.')
        else:
            print('Country not found.')

    def resolve_question_b(self):
        for key, values in self.data_dict.items():
            current = float(values.get('2020'))
            previous = float(values.get('2013'))

            if current == previous:
                print(f'{key}    No variation between 2013 and 2020')
            try:
                variation = (current - previous) / previous * 100.0
                print(f'{key}    Variation of {variation:.4g}% between 2013 and 2020')
            except ZeroDivisionError:
                print(float('inf'))

    def resolve_question_c(self, country: str):
        country_selected = self.data_dict.get(country)
        x_axis = []
        y_axis = []
        if country_selected:
            for year, value in country_selected.items():
                x_axis.append(year)
                y_axis.append(value)
        else:
            return print('Country not found.')

        plot_graph(x_axis, y_axis)


def plot_graph(x_axis, y_axis):
    plt.plot(x_axis, y_axis)
    plt.xlabel('X - Total Amount')
    plt.ylabel('X - Periods')
    plt.title('Amount graph')
    plt.show()


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

        plot_graph(x_axis, y_axis)


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


def call_question_5b():
    Question5().resolve_question_b()


def call_question_5c():
    country_name = input('Enter the country name: ')
    Question5().resolve_question_c(country_name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_question_5c()
