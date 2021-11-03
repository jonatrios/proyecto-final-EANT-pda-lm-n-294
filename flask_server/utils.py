import csv
import requests
from contextlib import closing
from bs4 import BeautifulSoup


def get_info(group,organization, tags, page):
    url = f'https://data.buenosaires.gob.ar/dataset/?_tags_limit=0&_organization_limit=0&groups={group}&organization={organization}&tags={tags}&page={page}'
    print(url)
    session = requests.Session()
    req = session.get(url).content
    if req:
        soup = BeautifulSoup(req, features='html.parser')

        filter_container = soup.find('div', class_='filters-container col-md-4')

        g = filter_container.find_all('div', class_='search-filter')

        g = g[1:]

        info = {f"{j.h2.text} ({str(len(j.find_all('a')))})" if j.h2.text not in ['Organizaciones', 'Etiquetas'] else f"{j.h2.text} ({str(len(j.find_all('a'))-1)})": [{f.text.strip() : 'https://data.buenosaires.gob.ar' + f['href']} for f in g[i].find_all('a') if f.text.strip() != 'Mostrar menos' ] for i, j in enumerate(g)}
        datasets = soup.find('div', class_='dataset-list')
        dataset_list = [a for a in datasets.find_all('a')]      
        pages = [int(a.text.replace('\n','')) for a in soup.find('div', class_='pagination-wrapper').find_all('li') if a.text.replace('\n','').isdigit()] if soup.find('div', class_='pagination-wrapper') != None else [1]

        d = {}

        dict_list = []
        for i, j in enumerate(dataset_list):
            d['dataset-id'] = i+1
            d['dataser-prefix'] = dataset_list[i]['href'].split('/')[-1]
            d['dataset-author'] = dataset_list[i].find('div', class_='dataset-author').text
            d['dataset-title'] = dataset_list[i].h3.text
            d['dataset-description'] = dataset_list[i].find('div', class_='dataset-notes').text
            d['dataset-formats'] = [x.text for x in dataset_list[i].find_all('span')[1:]]
            d['dataset-relation'] = [im['title'] for im in dataset_list[i].find_all('img')]
            d['dataset-link'] = 'https://data.buenosaires.gob.ar' + dataset_list[i]['href']
            dict_list.append(d.copy())
        info.update({f'datasets ({str(len(dict_list))})': dict_list, 'pages': max(pages)})
        return info
    else:
        return {'message': 'page not found'}


def get_resources(prefix):

    session = requests.Session()
    url_dataset = f'https://data.buenosaires.gob.ar/dataset/{prefix}'

    req_data = session.get(url_dataset).content

    soup_data = BeautifulSoup(req_data, features='html.parser')

    resources = soup_data.find('div', id='pkg-resources')

    dataset_container = resources.find_all('div', class_='pkg-container')
    d = {}

    dict_list = []
    for i, j in enumerate(dataset_container):
        d['dataset-title'] = dataset_container[i].h3.text
        d['datset-description'] = dataset_container[i].p.text
        d['dataset-link'] = dataset_container[i].a['href']
        d['dataset-data-format'] = dataset_container[i].a['href'].split('.')[-1]
        dict_list.append({f'resource ({str(i+1)})': d.copy()})
    final_dict = {'resources-prefix': prefix, 'resources-list': dict_list}
    return final_dict


def cache_data(resource:str) -> list:
    url = f'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/{resource}'
    print(url)
    '''
    This function creates a redis client to cache the data,
    if data is already there retrieve from redis, otherwise go to fetch the file,
    the expire cache time can be set depends on the needs.
    Also do a simple ETL to standarize the data.
    '''
    file_data = []
    with closing(requests.get(url, stream=True)) as r:
        f = [ line.decode('utf-8') for line in r.iter_lines()]
        print(f[0])
        headers = ['id'] + f[0].split(',')
        reader = csv.DictReader(f, delimiter=';' if ';' in f[0] else ',', quotechar='"')
        
        for row in reader:
            file_data.append(row)
        
    return file_data