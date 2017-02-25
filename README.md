# PersistIQ Python API Wrapper
[API docs](http://apidocs.persistiq.com/)

## Installation
### Git
`pip install git+git://github.com:tizz98/persistiq.git@master`

### PyPi
_Coming soon_

## Usage
### Setup
- Add `PERSIST_IQ_API_KEY='xxxxxxxx'` to your environment variables
    - bash: `echo export PERSIST_IQ_API_KEY='xxxxxxxx' >> ~/.bashrc`
    - zsh: `echo export PERSIST_IQ_API_KEY='xxxxxxxx' >> ~/.zshrc`
    - windows: ???
- Open up a new terminal or:
    - bash: `. ~/.bashrc`
    - zsh: `. ~/.zshrc`
    - windows: ???

### Resources
#### User
```python
from persistiq import User

for user in User.list():
    print user.id, user.name
```

#### Lead
```python
from persistiq import Lead

# NOTE:
# Leads will automatically be paginated
# to only get the first 100 without pagination set:
# >>> Lead.paginate = False

for lead in Lead.list():
    print lead.id, lead.data
```

#### Campaign
```python
from persistiq import Campaign

# NOTE:
# Campaigns will automatically be paginated
# to only get the first 100 without pagination set:
# >>> Campaign.paginate = False

for campaign in Campaign.list():
    print campaign.id, campaign.name
```
