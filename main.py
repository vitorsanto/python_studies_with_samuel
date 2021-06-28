# This is a sample Python script.

# Press ⌥⇧X to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from decimal import Decimal

import matplotlib.pyplot as plt


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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    call_question_4()
