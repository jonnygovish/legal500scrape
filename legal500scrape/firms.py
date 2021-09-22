import requests
from bs4 import BeautifulSoup
from csv import writer


def websrapper():
    try:
        source = requests.get('https://www.legal500.com/c/france/directory/').text

        soup = BeautifulSoup(source, 'html.parser')

        firms = soup.find("ul", {"id": "directoryUL"}).find_all('li')


        base_url = 'https://www.legal500.com'

        filename = 'firms.csv'

        company_urls = []
        
        with open(filename, 'w') as csv_file:
            csv_writer = writer(csv_file)
            headers = ['Company_name', "Company_url", "City"]
            csv_writer.writerow(headers)

            for firm in firms:
                # Check whether class of the selector is either multiple-offices or single-office
                if firm.get('class') == ['multiple-offices']:
                    # Extracting the company name
                    companyName = ' '.join(firm.find_all(text=True, recursive = False)).strip().split(",")[0]

                    # Getting the Company Urls
                    url =' '.join([base_url + url['href'] for url in firm.find_all('a')]).replace(" ", ", ")
                    
                    # Add urls to the company urls list 
                    [company_urls.append(base_url + url['href']) for url in firm.find_all('a')]
                    
                    # Getting the cities the company is located in 
                    cities = ' '.join([city.text for city in firm.find_all('a')]).replace(" ", ", ")
                    
                    # Write the extracted company information to the csv
                    csv_writer.writerow([ companyName, url, cities])
                                

                else:
                    # Extracting the company name
                    company_name = firm.find('strong').text
                    
                    # Getting the Company Url
                    url = base_url + firm.find('a')['href']

                    # Add url extracted to the company urls list
                    company_urls.append(url)

                    # Getting the cities the company is located in 
                    city = ''.join(firm.find_all(text= True)).strip().split('\t')[-1]
                
                    # Write the extracted company information to the csv
                    csv_writer.writerow([ company_name, url, city])

        return company_urls
                
                
    except Exception as e:
        print(e)




