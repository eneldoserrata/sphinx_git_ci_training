class AccountInvoice(object):

    id = 1
    number = 1
    partner_id = 1

    def save(self, values):
        """
            :param values: Este valor es un diccionario.
        """
        
        sql = "insert into account_invoice (id, number, partner_id) values (value[0],value[1],value[2])"
