import matplotlib.pyplot as plt
import pandas as pd
import data_save as ds

def create_and_save_plot(data, ticker, period, stile, filename=None):
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    graf_names = stile['graf_names']

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label=stile[f'{graf_names[0]}'],
                     linestyle=stile[f'{graf_names[0]}_stile'], color=stile[f'{graf_names[0]}_color'],
                     marker=stile[f'{graf_names[0]}_mark'], markerfacecolor=stile[f'{graf_names[0]}_mark_color'],
                     markersize=stile[f'{graf_names[0]}_mark_size'])
            plt.plot(dates, data['Moving_Average'].values, label=stile[f'{graf_names[1]}'],
                     linestyle=stile[f'{graf_names[1]}_stile'], color=stile[f'{graf_names[1]}_color'],
                     marker=stile[f'{graf_names[1]}_mark'], markerfacecolor=stile[f'{graf_names[1]}_mark_color'],
                     markersize=stile[f'{graf_names[1]}_mark_size'])
            plt.grid(stile['grid'], which='both')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label=stile[f'{graf_names[0]}'],
                 linestyle=stile[f'{graf_names[0]}_stile'], color=stile[f'{graf_names[0]}_color'],
                 marker=stile[f'{graf_names[0]}_mark'], markerfacecolor=stile[f'{graf_names[0]}_mark_color'],
                 markersize=stile[f'{graf_names[0]}_mark_size'])
        plt.plot(data['Date'], data['Moving_Average'], label=stile[f'{graf_names[1]}'],
                 linestyle=stile[f'{graf_names[1]}_stile'], color=stile[f'{graf_names[1]}_color'],
                 marker=stile[f'{graf_names[1]}_mark'], markerfacecolor=stile[f'{graf_names[1]}_mark_color'],
                 markersize=stile[f'{graf_names[1]}_mark_size'])
        plt.grid(stile['grid'], which='both')

    plt.title(f"{ticker} Цена акций с течением времени", color=stile['font_color'])
    plt.xlabel("Дата", color=stile['font_color'])
    plt.ylabel("Цена", color=stile['font_color'])
    plt.legend()

    file_data = ds.file_name_creator(filename, period, ticker, 'Default')

    plt.savefig(file_data[0])
    print(f"График сохранен как {file_data[0]}")

def RSI_plot(data, period, ticker, name, stile, filename=None):
    ''' Функция создания файла с графиком RSI по заданным значениям '''
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    graf_names = stile['graf_names']
    ''' Настройка окна графика и шрифа в нем '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['rsi'].values, label=stile[f'{graf_names[2]}'],
                     linestyle=stile[f'{graf_names[2]}_stile'], color=stile[f'{graf_names[2]}_color'],
                     marker=stile[f'{graf_names[2]}_mark'], markerfacecolor=stile[f'{graf_names[2]}_mark_color'],
                     markersize=stile[f'{graf_names[2]}_mark_size'])
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['rsi'], label=stile[f'{graf_names[2]}'],
                 linestyle=stile[f'{graf_names[2]}_stile'], color=stile[f'{graf_names[2]}_color'],
                 marker=stile[f'{graf_names[2]}_mark'], markerfacecolor=stile[f'{graf_names[2]}_mark_color'],
                 markersize=stile[f'{graf_names[2]}_mark_size'])
    ''' Отрисовка графика по дате и значениям RSI '''
    plt.title(f"RSI {name} ({ticker}) с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI индекс")
    plt.grid()
    plt.legend()
    ''' Отрисовка информации по графику '''
    file_data = ds.file_name_creator(filename, period, ticker, 'RSI')
    ''' Определение имени сохраняемого файла '''
    plt.savefig(file_data[0])
    ''' Сохранение графика '''
    print(f"График сохранен в {file_data[1]} имя файла {file_data[2]}")
    ''' Сообщение о создание файла с его данными '''