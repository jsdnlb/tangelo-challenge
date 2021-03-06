from app.modules.api_requests import get_all_contries
from app.modules.connect_and_insert_in_table import connect_and_insert_log
from app.modules.structure_dataframe import filter_data
from app.modules.calculate_run_times import calculate_execution_times

# Start execution

def run():
    print('Initiating execution... 🚀')
    info_countries = get_all_contries("https://restcountries.com/v3.1/all")
    data = filter_data(info_countries)
    # I use the tuple returned by calculate_execution_times() to send them to the database.
    all_times = calculate_execution_times(data)
    connect_and_insert_log(all_times)
    print('\nEverything was executed correctly, thank you for testing it 🥳!\n')


if __name__ == '__main__':
    run()
