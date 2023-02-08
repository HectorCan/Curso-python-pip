from read_csv import read_csv
from utils import population_by_country, get_population
from charts import generate_pie_chart, generate_bar_chart


def run():
  data = read_csv('./data.csv')

  # Se puede filtrar por continente
  '''  
  labels = [c['Country/Territory'] for c in data]
  values = [c['World Population Percentage'] for c in data]
  
  generate_pie_chart(labels, values)
  '''
  
  country = input('Type Country => ')

  result = population_by_country(data, country)
  
  if len(result) > 0:
    countryData = result[0]
    labels, values = get_population(countryData)

    generate_bar_chart(country, labels, values)


if __name__ == "__main__":
  run()
