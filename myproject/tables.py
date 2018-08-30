from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    name = Col('Name')
    code = Col('Code')
    fair_price = Col('Fair Price')
    gain = Col('Gain')
