from z3 import *

def add_range_constraints(solver, dict_z3):
    
    solver.add(dict_z3['LuogoNascita'] >=0, dict_z3['LuogoNascita'] <=79)
    solver.add(Or(dict_z3['Genere']==0, dict_z3['Genere']==1))
    solver.add(Or(dict_z3['Gestione']==0, dict_z3['Gestione']==1, dict_z3['Gestione']==2))
    solver.add(Or(\
            And(dict_z3['DataProtocollo']>=20191001,dict_z3['DataProtocollo']<=20191031),\
            And(dict_z3['DataProtocollo']>=20191101,dict_z3['DataProtocollo']<=20191030),\
            And(dict_z3['DataProtocollo']>=20191201,dict_z3['DataProtocollo']<=20191230)\
    ))
    solver.add(Or(\
            And(dict_z3['DataAccadimento']>=20191001,dict_z3['DataAccadimento']<=20191031),\
            And(dict_z3['DataAccadimento']>=20191101,dict_z3['DataAccadimento']<=20191030),\
            And(dict_z3['DataAccadimento']>=20191201,dict_z3['DataAccadimento']<=20191230)\
    ))
    solver.add(dict_z3['LuogoAccadimento']>=8,dict_z3['LuogoAccadimento']<=11)
    solver.add(dict_z3['Eta']>=10,dict_z3['Eta']<=83)
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
            print('This operation ({}) is not allowed'.format(op))
            exit(1)


def ConstraintSolverModule(S):
    solver = Solver()
    #z3 variables

    dict_z3 = {
        'LuogoNascita': BitVec('LuogoNascita', 32),
        'Genere': BitVec('Genere', 32),
        'Gestione': BitVec('Gestione', 32),
        'DataProtocollo': BitVec('DataProtocollo', 32),
        'DataAccadimento': BitVec('DataAccadimento', 32),
        'LuogoAccadimento': BitVec('LuogoAccadimento', 32),
        'Eta': BitVec('Eta', 32),
        'ModalitaAccadimento': BitVec('ModalitaAccadimento', 32),
        'ConSenzaMezzoTrasporto': BitVec('ConSenzaMezzoTrasporto', 32),
        'SettoreAttivitaEconomica_Macro': BitVec('SettoreAttivitaEconomica_Macro', 32),
        'GestioneTariffaria': BitVec('GestioneTariffaria', 32),
        'GrandeGruppoTariffario': BitVec('GrandeGruppoTariffario', 32),
        'Deceduto': BitVec('Deceduto', 32)
    }
    
    add_range_constraints(solver, dict_z3)
    set_constraints(S, solver, dict_z3)
