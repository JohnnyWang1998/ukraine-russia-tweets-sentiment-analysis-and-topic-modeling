from bs4 import BeautifulSoup
import urllib
import pandas as pd


def get_media_dict(url: str) -> dict:
    """
    Get a dictionary of media accounts from website url.
    @param url: website url
    return: a dictionary of media accounts
    """
    soup = BeautifulSoup(urllib.request.urlopen(url).read())

    media_account_dict = {}
    # get the table with media account information
    account_table = soup.findAll('table')[0].tbody
    for (i, row) in enumerate(account_table.findAll('tr')):
        # skip the table head
        if i == 0:
            continue
        # get name of each row
        user_name = row.findAll('td')[1].text
        real_name = row.findAll('td')[2].text
        # add names without @
        media_account_dict[real_name] = user_name[1:]
    return media_account_dict


def export_media_list(url: str):
    """
    Export a list of media accounts from website url.
    @param url: website url
    """
    media_account_dict = get_media_dict(url)
    # export to a csv file
    media_df = pd.DataFrame(list(zip(media_account_dict.keys(), media_account_dict.values())),
                            columns=['real_name', 'user_name'])
    media_df.head()
    media_df.to_csv('../data/external/media_accounts.csv', index=False)
