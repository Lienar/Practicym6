import data_download as dd
import data_plotting as dplt
import dates_check as dcheck
import data_calculate as dc
import data_save as ds


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    #print("Заданы процент колебаний: от 0 до 100")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = period_choice()
    stile = plotting_stile()
    #threshold = input("Введите заданный процент колебаний (например, '5.23' для 5.23 процентов): ")
    #filename = input("Введите имя файла для сохранения данных: ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, period, stile)

    # Сalculate the average
    #dc.calculate_and_display_average_price(stock_data)

    # Checking for exceeding the threshold
    #dc.notify_if_strong_fluctuations(stock_data, threshold)

    # Export data to file
    #ds.export_data_to_csv(stock_data, filename)

    # Creat data with RSI
    #rsi_data = dd.data_for_RSI_calculate(stock_data)

    # Return company name by ticker
    #name = dd.name_return(ticker)

    # Plot RSI
    #dplt.RSI_plot(rsi_data, period, ticker, name)


def period_choice():
    ''' Функция определения периода для данных '''
    index = input("выберите способ определения временного периода. PP для предустановленых периодов или DP для вабора периода по датам: ")
    ''' Выбор способа определения периода '''
    if index == 'PP':
        print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
        period_temp = input("Введите период для данных (например, '1mo' для одного месяца): ")
        ''' Ввод предустановленного периода  '''
        period = [index, period_temp]
        ''' Формирование данных по предустановленноу периоду '''
    elif index == 'DP':
        print("Укажите первую и вторую даты в формате гггг-мм-дд (например 2005-04-22)")
        period1_temp = input("Введите дату начала периода: ")
        period1_temp = dcheck.dates_rechandge(period1_temp)
        ''' Ввод первой даты '''
        period2_temp = input("Введите дату окончания периода: ")
        period2_temp = dcheck.dates_rechandge(period2_temp)
        period_temp = dcheck.dates_order(period1_temp, period2_temp)
        ''' Ввод второй даты '''
        period = ['DP', (f'{period_temp[0][0]}-{period_temp[0][1]}-{period_temp[0][2]}'),
                        (f'{period_temp[1][0]}-{period_temp[1][1]}-{period_temp[1][2]}')]
        ''' Формирование данных по датам '''
    else:
        period = ['DD', '1mo']
        ''' Формирование данных по умолчанию '''
    return period

def plotting_stile():
    ''' Функция меню настройки стиля графика '''
    print('Для входа в меню настройки стиля графика введите Yes для пропуск No')
    is_enter = input('Хотите войти в меню: ')
    enter = 'in'
    stile = [True, None, 'red', 10, 14, 'black', 'solid', 'black', 'solid', 'red']
    palitra = ['blue', 'green', 'red', 'purple', 'grey', 'yellow', 'black']
    if is_enter.lower() == 'yes':
        while enter.lower() != 'exit':
            print(' ')
            print('Выберите параметр для настройки')
            print(f'1. Размер текста текущие значение {stile[4]}')
            print(f'2. Цвет текста текущие значение {stile[5]}')
            print(f'3. Отображение маркера значений текущие значение {stile[1]}')
            print(f'4. Цвет маркера значений текущие значение {stile[2]}')
            print(f'5. Размер маркера значений текущие значение {stile[3]}')
            print(f'6. Отображение сетки текущие значение {stile[0]}')
            print('7. Подменю настройки графиков')
            enter = input('Введите номер пункта для установки значения или exit для выхода: ')
            if enter == '1':
                print(' ')
                font_size = int(input('Введите значение размера шрифта от 8 до 24: '))
                if font_size < 8:
                    font_size = 8
                    print('Размер шрифта слишком мал установлен минимальный размер')
                if font_size > 24:
                    font_size = 24
                    print('Размер шрифта слишком велик установлен максимальный размер')
                stile[4] = font_size
            if enter == '2':
                print(' ')
                print('Выберите параметр для настройки')
                print('1. blue(синий)')
                print('2. green(зеленый)')
                print('3. red(красный)')
                print('4. purple(голубой)')
                print('5. grey(серый)')
                print('6. yellow(желтый)')
                print('7. black(черный стоит по умолчанию)')
                index = input('Введите номер цвета: ')
                stile[5] = palitra[int(index)-1]
            if enter == '3':
                print(' ')
                is_mark = input('Введите Yes для отображения маркеров значений и No чтобы их скрыть (по умолчанию маркеры скрыты): ')
                if is_mark.lower() == 'yes':
                    stile[1] = 'o'
                else:
                    stile[1] = is_mark
            if enter == '4':
                print(' ')
                print('Выберите параметр для настройки')
                print('1. blue(синий)')
                print('2. green(зеленый)')
                print('3. red(красный стоит по умолчанию)')
                print('4. purple(голубой)')
                print('5. grey(серый)')
                print('6. yellow(желтый)')
                print('7. black(черный)')
                index = input('Введите номер цвета: ')
                stile[2] = palitra[int(index) - 1]
            if enter == '5':
                print(' ')
                mark_size = int(input('Введите значение размера шрифта от 1 до 12: '))
                if mark_size < 1:
                    mark_size = 1
                    print('Размер маркера слишком мал установлен минимальный размер')
                if mark_size > 12:
                    mark_size = 12
                    print('Размер маркера слишком велик установлен максимальный размер')
                stile[3] = mark_size
            if enter == '6':
                print(' ')
                is_mark = input(
                    'Введите Yes для отображения сетки и No чтобы их скрыть (по умолчанию сетка отображается): ')
                if is_mark.lower() == 'yes':
                    stile[0] = True
                else:
                    stile[0] = False
            if enter == '7':
                stily_graf_temp = graf_plot_menu(stile)
                for i in range(0, len(stily_graf_temp)):
                    stile[i+6] = stily_graf_temp[i]
    return stile

def graf_plot_menu(stile):
    enter = 'in'
    graf_stile = ['solid', 'black', 'solid', 'red']
    for i in range(len(stile)-len(graf_stile), len(stile)):
        graf_stile[i-(len(stile)-len(graf_stile))] = stile[i]
    line_stile = ['solid', 'dotted', 'dashed', 'dashdot']
    line_color = ['blue', 'green', 'red', 'purple', 'grey', 'yellow', 'black']
    while enter.lower() != 'exit':
        print(' ')
        print('Выберите параметр для настройки')
        print(f'1. Стиль графика значение цены на момент закрытия текущие значение {graf_stile[0]}')
        print(f'2. Цвет графика значение цены на момент закрытия текущие значение {graf_stile[1]}')
        print(f'3. Стиль графика средних значений текущие значение {graf_stile[2]}')
        print(f'4. Цвет графика средних значений текущие значение {graf_stile[3]}')
        print(' ')
        enter = input('Введите параметр меню или exit для выхода: ')
        if enter == '1':
            print(' ')
            print('Выберите параметр для настройки')
            print('1. сплошная линия')
            print('2. линия из точек')
            print('3. пунктирная линия')
            print('4. пунктирная с точками в промежутках')
            index = input('Введите номер цвета: ')
            graf_stile[0] = line_stile[int(index) - 1]
        if enter == '2':
            print(' ')
            print('Выберите параметр для настройки')
            print('1. blue(синий)')
            print('2. green(зеленый)')
            print('3. red(красный)')
            print('4. purple(голубой)')
            print('5. grey(серый)')
            print('6. yellow(желтый)')
            print('7. black(черный стоит по умолчанию)')
            index = input('Введите номер цвета: ')
            graf_stile[1] = line_color[int(index) - 1]
        if enter == '3':
            print(' ')
            print('Выберите параметр для настройки')
            print('1. сплошная линия')
            print('2. линия из точек')
            print('3. пунктирная линия')
            print('4. пунктирная с точками в промежутках')
            index = input('Введите номер цвета: ')
            graf_stile[2] = line_stile[int(index) - 1]
        if enter == '4':
            print(' ')
            print('Выберите параметр для настройки')
            print('1. blue(синий)')
            print('2. green(зеленый)')
            print('3. red(красный стоит по умолчанию)')
            print('4. purple(голубой)')
            print('5. grey(серый)')
            print('6. yellow(желтый)')
            print('7. black(черный)')
            index = input('Введите номер цвета: ')
            graf_stile[3] = line_color[int(index) - 1]
    return graf_stile

if __name__ == "__main__":
    main()



