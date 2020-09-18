import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

data = pd.DataFrame()

def data_cleanup(data):
    # Deletes NA rows
    data = data.dropna(how='all')

    # Find 'Or' and delete it
    data = data[data['Order Date'].str[0:2] != 'Or']

    # Add month column
    data['Month'] = data['Order Date'].str[0:2]
    data['Month'] = data['Month'].astype('int32')

    # Convert Price Each and Quantity Ordered to int
    data['Quantity Ordered'] = pd.to_numeric(data['Quantity Ordered'])
    data['Price Each'] = pd.to_numeric(data['Price Each'])

    # Add a sales column
    data['Sales'] = data['Quantity Ordered']*data['Price Each']

    # Add a city column
    data['City'] = data['Purchase Address'].apply(lambda x: x.split(',')[1])

    # Change the Order Date column to DateTime
    data['Order Date'] = pd.to_datetime(data['Order Date'])

    # Add a colum for Hour and Minute
    data['Hour'] = data['Order Date'].dt.hour
    data['Minute'] = data['Order Date'].dt.minute

    return data

def earned_in_month(data):
    sales = data.groupby('Month').sum()
    months = range(1,13)
    plt.figure(figsize=(16,9))
    plt.title('Sales per month', size=25)
    plt.bar(months, sales['Sales'],color='#6D75E9')
    plt.xticks(months,fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel('Sales in USD',size=20)
    plt.xlabel('Month',size=20)
    plt.show()
    # Did we spend more money on advertisment in May compared to April?

def sold_together(data):
    df = data[data['Order ID'].duplicated(keep=False)]
    df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
    df = df[['Order ID', 'Grouped']].drop_duplicates()
    count = Counter()
    for row in df['Grouped']:
        row_list = row.split(',')
        count.update(Counter(combinations(row_list,2)))
    most_common = count.most_common(5)
    ms = pd.DataFrame(most_common,columns=['Products sold together','# of times they were sold together'])
    return ms

def most_profit_city(data):
    sales = data.groupby('City').sum()
    cities = [city for city, df in data.groupby('City')]
    plt.figure(figsize=(16,9))
    plt.title('Sales per city', size=25)
    plt.bar(cities, sales['Sales'],color='#6D75E9')
    plt.xticks(cities,rotation='vertical',fontsize=14)
    plt.yticks(fontsize=14)
    plt.ylabel('Sales in USD',size=20)
    plt.xlabel('City name',size=20)
    plt.show()

def best_time_ad(data):
    hours = [hour for hour, df in data.groupby('Hour')]
    plt.figure(figsize=(16,9))
    plt.title('Orders for each hour', size=25)
    plt.xticks(hours)
    plt.grid()
    plt.plot(hours,data.groupby('Hour').count(),color='#6D75E9')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel('Hours',size=20)
    plt.ylabel('Number of orders',size=20)
    plt.show()

# Define function for 'What products are most often sold together?'


def most_sold(data):
    product_group = data.groupby('Product')
    quantity = product_group.sum()['Quantity Ordered']
    products = [product for product, df in product_group]
    prices = data.groupby('Product').mean()['Price Each']
    
    fig,ax1 = plt.subplots(figsize=(16,9))
    plt.title('Most sold products and their prices', size=25)
    ax2 = ax1.twinx()
    ax1.bar(products,quantity,color='#6D75E9')
    ax2.plot(products,prices,color='#EE5C5C')
    ax1.set_xlabel('Product Name')
    ax1.set_ylabel('Quantity Ordered', color='#6D75E9',size=20)
    ax2.set_ylabel('Price in USD', color='#EE5C5C',size=20)
    ax1.set_xticklabels(products,rotation=45,size=20)
    ax2.tick_params(labelsize=12)
    ax1.tick_params(labelsize=12)
    plt.show()




if __name__ == '__main__':

    path = r'/sales_bakery/'
    files = [file_ for file_ in os.listdir(path)]

    all_data = pd.DataFrame()

    for file_ in files:
        df = pd.read_csv(path+file_)
        all_data = pd.concat([all_data,df])

    data = data_cleanup(data=all_data)
    earned_in_month(data=data)
    most_profit_city(data=data)
    best_time_ad(data=data)
    most_sold(data=data)


