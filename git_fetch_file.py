
# coding: utf-8

# In[ ]:


# https://requests.readthedocs.io pip3 install PyGithub requests

# fetches the requested file

def git_fetch_file(file_name, path, branch='master'):

    import requests

    git_token = 'xxxxx' # git personal token

    path = path.replace(' ','%20')
    path = path.replace('/','%2F')

    url = f'https://git.domain.com/api/v4/projects/{path}%2F{file_name}/raw?ref={branch}'

    r = requests.get(url, headers={'PRIVATE-TOKEN':git_token})

    r.encoding = r.apparent_encoding # in case of nontypical coding
    
    # help(requests.status_codes)     "* 200: ``ok``, ``okay``, ``all_ok``, ``all_okay``, ``all_good``, ``\o/``, ``✓``"
    if r.status_code == 200 and len(r.text) > 50:  
        return r.text


# In[ ]:


# additional details for github 

# authentication to github
g = Github("username", "password")
user = g.get_user()

# fetch a file through raw link 
gh_file = requests.get("https://raw.githubusercontent.com/AdVarga90/Various/blob/main/Excel_pivot_field_extractor.ipynb").content

