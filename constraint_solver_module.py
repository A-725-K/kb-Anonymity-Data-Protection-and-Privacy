from z3 import *


def add_range_constraints(solver, dict_z3):
    solver.add(dict_z3['LuogoNascita']>=0, dict_z3['LuogoNascita']<=79)
    solver.add(Or(dict_z3['Genere']==0, dict_z3['Genere']==1))
    solver.add(Or(dict_z3['Gestione']==0, dict_z3['Gestione']==1, dict_z3['Gestione']==2))
    solver.add(Or(\
            And(dict_z3['DataProtocollo']>=20191001,dict_z3['DataProtocollo']<=20191031),\
            And(dict_z3['DataProtocollo']>=20191101,dict_z3['DataProtocollo']<=20191130),\
            And(dict_z3['DataProtocollo']>=20191201,dict_z3['DataProtocollo']<=20191231)\
    ))
    solver.add(Or(\
            And(dict_z3['DataAccadimento']>=20191001,dict_z3['DataAccadimento']<=20191031),\
            And(dict_z3['DataAccadimento']>=20191101,dict_z3['DataAccadimento']<=20191130),\
            And(dict_z3['DataAccadimento']>=20191201,dict_z3['DataAccadimento']<=20191231)\
    ))
    solver.add(dict_z3['DataAccadimento']<=dict_z3['DataProtocollo'])
    solver.add(dict_z3['LuogoAccadimento']>=8,dict_z3['LuogoAccadimento']<=11)
    solver.add(dict_z3['Eta']>=3,dict_z3['Eta']<=90)
    solver.add(Or(dict_z3['ModalitaAccadimento']==0,dict_z3['ModalitaAccadimento']==1))
    solver.add(Or(dict_z3['ConSenzaMezzoTrasporto']==0,dict_z3['ConSenzaMezzoTrasporto']==1))
    solver.add(dict_z3['SettoreAttivitaEconomica_Macro']>=-1,dict_z3['SettoreAttivitaEconomica_Macro']<=18)
    solver.add(dict_z3['GestioneTariffaria']>=-1,dict_z3['GestioneTariffaria']<=4,dict_z3['GestioneTariffaria']!=0)
    solver.add(dict_z3['GrandeGruppoTariffario']>=-1,dict_z3['GrandeGruppoTariffario']<=9)
    solver.add(Or(dict_z3['Deceduto']==0,dict_z3['Deceduto']==1))


def set_constraints(S, solver, dict_z3):
    for (attr, op, val) in S:
        if op == '==':
            solver.add(dict_z3[attr] == val)
        elif op == '!=':
            solver.add(dict_z3[attr] != val)
        elif op == '>=':
            solver.add(dict_z3[attr] >= val)
        elif op == '<=':
            solver.add(dict_z3[attr] <= val)
        elif op == '>':
            solver.add(dict_z3[attr] > val)
        elif op == '<':
            solver.add(dict_z3[attr] < val)
        else:
            print('[!!] This operation ({}) is not allowed'.format(op))
            exit(1)


def z3model2row(model,dict_z3):
    row = {}
    for k, v in dict_z3.items():
        row[k] = model[v].as_long()
    return row


def ConstraintSolverModule(S):
    #Z3 variables and solver
    solver = Solver()
    dict_z3 = {
        'LuogoNascita': Int('LuogoNascita'),
        'Genere': Int('Genere'),
        'Gestione': Int('Gestione'),
        'DataProtocollo': Int('DataProtocollo'),
        'DataAccadimento': Int('DataAccadimento'),
        'LuogoAccadimento': Int('LuogoAccadimento'),
        'Eta': Int('Eta'),
        'ModalitaAccadimento': Int('ModalitaAccadimento'),
        'ConSenzaMezzoTrasporto': Int('ConSenzaMezzoTrasporto'),
        'SettoreAttivitaEconomica_Macro': Int('SettoreAttivitaEconomica_Macro'),
        'GestioneTariffaria': Int('GestioneTariffaria'),
        'GrandeGruppoTariffario': Int('GrandeGruppoTariffario'),
        'Deceduto': Int('Deceduto')
    }
    
    add_range_constraints(solver, dict_z3)
    set_constraints(S, solver, dict_z3)

    if solver.check() == sat:
        model = solver.model()
        return z3model2row(model, dict_z3)

    return None
