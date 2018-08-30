from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    code = Col('Code')
    fair_price = Col('Fair Price')
    gain = Col('Gain')


class ResultsEdit(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    code = Col('Code')
    fair_price = Col('Fair Price')
    gain = Col('Gain')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(id='id'))



class ResultsDelete(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    code = Col('Code')
    fair_price = Col('Fair Price')
    gain = Col('Gain')
    edit = LinkCol('Delete', 'delete', url_kwargs=dict(name='name'))
