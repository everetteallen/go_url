def go_url(request):
    from flask import redirect, request
    import urllib.request
    import os

    request_string = request.path.strip("/")
    
    # Here we get our GSheet id and columns to use from the function runtime variables

    searchCol = os.environ.get('searchCol')
    dataCol = os.environ.get('dataCol')
    sheetID = os.environ.get('sheetID')
    
    # query the google sheet to get the url from the patch title  
    # Example: column A has keyword to lookup and column B has URL to redirect to
    sheetLink = "https://docs.google.com/spreadsheets/d/" + sheetID + "/gviz/tq?tqx=out:csv&tq=%20select%20" + dataCol + "%20WHERE%20" + searchCol + "=%27" + request_string + "%27"

    try:
        lstring = urllib.request.urlopen(sheetLink).read().decode('utf-8').strip('\"')
        
    except:
        return "<h1 style='color: red;'> ERROR - Can not get link for " + f'{request_string}' + " from sheet </h1>"
    
    if not lstring.strip():
        return "<h1 style='color: red;'> Link for keyword " +  f'{request_string}' + " not found </h1>"
        
    return redirect(lstring, code = 302)