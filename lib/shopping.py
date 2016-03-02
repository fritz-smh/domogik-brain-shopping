# -*- coding: utf-8 -*-
def shopping(args, cfg_i18n, log):
    """ Interface to manage a shopping list
        @param args : 0 : action (add, remove, get, clean)
                      1... : data
    """
    from domogik.butler.list import ItemList

    # Processing
    the_list = ItemList(log, "shopping")
    action = args[0]
    data = " ".join(args[1:])

    log.debug(u"Shopping : action='{0}', data='{1}'".format(action, data))

    if action.lower() in ['add', 'remove', 'clean']:
        if action.lower() == "add":
            status, code = the_list.add(data)
        elif action.lower() == "remove":
            status, code = the_list.remove(data)
        elif action.lower() == "clean":
            status, code = the_list.clean()

        if status == True:
            return cfg_i18n["OK"]
        else:
            return cfg_i18n["ERRORS"][code]
    elif action.lower() == "get":
        items = the_list.get_as_list()
        if items != []:
            items = ", ".join(the_list.get_as_list())
        else:
            items = cfg_i18n["EMPTY_LIST"]
        return items
    
