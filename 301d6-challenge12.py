#!/usr/bin/env python3

# Script: Ops 301 Class 11 Ops Challenge Solution
# Author: John Alfred C. Alona
# Date of latest revision: "03/29/2023"
# Purpose: 

# Create a Python script that performs the following:
import requests
#     Prompt the user to type a string input as the variable for your destination URL.
URL = input("Please type destination URL: ")
if URL.startswith("http://") or URL.startswith("https://"):
    print("Select HTTP Request Method for the URL")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")
    print("5. HEAD")
    print("6. PATCH")
    print("7. OPTIONS")
    getreq = input("Select from the options above: ")
    #     Prompt the user to select a HTTP Method of the following options:
    #         GET
    #         POST
    #         PUT
    #         DELETE
    #         HEAD
    #         PATCH
    #         OPTIONS
        
        #     Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
    if getreq == "1":
        print("Doing a request.get for " + URL)
    if getreq == "2":
        print("Doing a request.post for " + URL)
    if getreq == "3":
        print("Doing a request.put for " + URL)
    if getreq == "4":
        print("Doing a request.delete for " + URL)
    if getreq == "5":
        print("Doing a request.head for " + URL)
    if getreq == "6":
        print("Doing a request.patch for " + URL)
    if getreq == "7":
        print("Doing a request.options for " + URL)
    cnfrm = input("do you want to continue?y/n?")
    responses = {
    # The list is separated by kind.
    # Informational 1xx

        100: ("Continue", "Client should continue with request"),
        101: ("Switching", "Protocols - Server is switching protocols."),
        102: ("Processing", "Server has received and is processing the request."),
        103: ("Processing", "Server has received and is processing the request."),
        122: ("Request-uri too long", "URI is longer than a maximum of 2083 characters."),

    # Success 2xx

    # These codes indicate success. The body section if present is the object returned by the request. It is a MIME format object. It is in MIME format, and may only be in text/plain, text/html or one fo the formats specified as acceptable in the request.

        200: ("Ok", "The request was fulfilled."),
        201: ("Created", "Following a POST command, this indicates success, but the textual part of the response line indicates the URI by which the newly created document should be known."),
        202: ("Accepted", "The request has been accepted for processing, but the processing has not been completed. The request may or may not eventually be acted upon, as it may be disallowed when processing actually takes place. there is no facility for status returns from asynchronous operations such as this."),
        203: ("Partial Information", "When received in the response to a GET command, this indicates that the returned metainformation is not a definitive set of the object from a server with a copy of the object, but is from a private overlaid web. This may include annotation information about the object, for example."),
        204: ("No Response", "Server has received the request but there is no information to send back, and the client should stay in the same document view. This is mainly to allow input for scripts without changing the document at the same time."),
        205: ("Reset Content", "Request processed, no content returned, reset document view."),
        206: ("Partial Content", "partial resource return due to request header."),
        207: ("Multi-Status", "XML, can contain multiple separate responses."),
        208: ("Already Reported", "results previously returned."),
        226: ("Im Used", "request fulfilled, reponse is instance-manipulations."),

    # Redirection 3xx

    # The codes in this section indicate action to be taken (normally automatically) by the client in order to fulfill the request.

        301: ("Moved", "The data requested has been assigned a new URI, the change is permanent. (N.B. this is an optimisation, which must, pragmatically, be included in this definition. Browsers with link editing capabiliy should automatically relink to the new reference, where possible)"),
        302: ("Found", "The data requested actually resides under a different URL, however, the redirection may be altered on occasion (when making links to these kinds of document, the browser should default to using the Udi of the redirection document, but have the option of linking to the final document) as for 'Forward'."),
        303: ("Method", "Like the found response, this suggests that the client go try another network address. In this case, a different method may be used too, rather than GET."),
        304: ("Not Modified", "If the client has done a conditional GET and access is allowed, but the document has not been modified since the date and time specified in If-Modified-Since field, the server responds with a 304 status code and does not send the document body to the client."),
        305: ("Use Proxy", "Content located elsewhere, retrieve from there."),
        306: ("Switch Proxy", "Subsequent requests should use the specified proxy."),
        307: ("Temporary Redirect", "Connect again to different URI as provided."),
        308: ("Permanent Redirect", "Connect again to a different URI using the same method."),

    # Client side errors 4xx

    # The 4xx codes are intended for cases in which the client seems to have erred, and the 5xx codes for the cases in which the server is aware that the server has erred. It is impossible to distinguish these cases in general, so the difference is only informational.

    # The body section may contain a document describing the error in human readable form. The document is in MIME format, and may only be in text/plain, text/html or one for the formats specified as acceptable in the request.

        400: ("Bad Request", "The request had bad syntax or was inherently impossible to be satisfied."),
        401: ("Unauthorized", "The parameter to this message gives a specification of authorization schemes which are acceptable. The client should retry the request with a suitable Authorization header."),
        402: ("Payment Required", "The parameter to this message gives a specification of charging schemes acceptable. The client may retry the request with a suitable ChargeTo header."),
        403: ("Forbidden", "The request is for something forbidden. Authorization will not help."),
        404: ("Not Found", "The server has not found anything matching the URI given."),
        405: ("Method Not Allowed", "Request method not supported by that resource."),
        406: ("Not Acceptable", "Content not acceptable according to the Accept headers."),
        407: ("Proxy Authentication Required", "Client must first authenticate itself with the proxy."),
        408: ("Request Timeout", "Server timed out waiting for the request."),
        409: ("Conflict", "Request could not be processed because of conflict."),
        410: ("Gone", "Resource is no longer available and will not be available again."),
        411: ("Length Required", "Request did not specify the length of its content."),
        412: ("Precondition Failed", "Server does not meet request preconditions."),
        413: ("Request Entity Too Large", "Request is larger than the server is willing or able to process."),
        414: ("Request URI Too Large", "URI provided was too long for the server to process."),
        415: ("Unsupported Media Type", "Server does not support media type."),
        416: ("Requested Rage Not Satisfiable", "Client has asked for unprovidable portion of the file."),
        417: ("Expectation Failed", "Server cannot meet requirements of Expect request-header field."),
        418: ("I'm a teapot", "I'm a teapot."),
        420: ("Enhance Your Calm", "Twitter rate limiting."),
        421: ("Misdirected Request", "Server is not able to produce a response."),
        422: ("Unprocessable Entity", "Request unable to be followed due to semantic errors."),
        423: ("Locked", "Resource that is being accessed is locked."),
        424: ("Failed Dependency", "Request failed due to failure of a previous request."),
        426: ("Upgrade Required", "Client should switch to a different protocol."),
        428: ("Precondition Required", "Origin server requires the request to be conditional."),
        429: ("Too Many Requests", "User has sent too many requests in a given amount of time."),
        431: ("Request Header Fields Too Large", "Server is unwilling to process the request."),
        444: ("No Response", "Server returns no information and closes the connection."),
        449: ("Retry With", "Request should be retried after performing action."),
        450: ("Blocked By Windows Parental Controls", "Windows Parental Controls blocking access to webpage."),
        451: ("Wrong Exchange Server", "The server cannot reach the client's mailbox."),
        499: ("Client Closed Request", "Connection closed by client while HTTP server is processing."),

    # Server side error 5xx

    # This means that even though the request appeared to be valid something went wrong at the server level and it wasn’t able to return anything.

        500: ("Internal Error", "The server encountered an unexpected condition which prevented it from fulfilling the request."),
        501: ("Not Implemented", "The server does not support the facility required."),
        502: ("Service temporarily overloaded", "The server cannot process the request due to a high load (whether HTTP servicing or other requests). The implication is that this is a temporary condition which maybe alleviated at other times."),
        503: ("Gateway timeout", "This is equivalent to Internal Error 500, but in the case of a server which is in turn accessing some other service, this indicates that the respose from the other service did not return within a time that the gateway was prepared to wait. As from the point of view of the clientand the HTTP transaction the other service is hidden within the server, this maybe treated identically to Internal error 500, but has more diagnostic value."),
        504: ("Gateway Timeout", "Gateway did not receive response from upstream server."),
        505: ("Http Version Not Supported", "Server does not support the HTTP protocol version."),
        506: ("Variant Also Negotiates", "Content negotiation for the request results in a circular reference."),
        507: ("Insufficient Storage", "Server is unable to store the representation."),
        508: ("Loop Detected", "Server detected an infinite loop while processing the request."),
        509: ("Bandwidth Limit Exceeded", "Bandwidth limit exceeded."),
        510: ("Not Extended", "Further extensions to the request are required."),
        511: ("Network Authentication Required", "Client needs to authenticate to gain network access."),
        598: ("Network Read Timeout Error", "Network read timeout behind the proxy."),
        599: ("Network Connect Timeout Error", "Network connect timeout behind the proxy."),

    }
    if getreq == "1":
        cnfrm
        if cnfrm == "y":
            get = requests.get(URL)
            print("status code is ", + get.status_code)
            print(str(get.status_code), "means", responses[get.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "2":
        cnfrm
        if cnfrm == "y":
            pos = requests.post(URL)
            print("status code is ", + pos.status_code)
            print(str(pos.status_code), "means", responses[pos.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "3":
        cnfrm
        if cnfrm == "y":
            put = requests.put(URL)
            print("status code is ", + put.status_code)
            print(str(put.status_code), "means", responses[put.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "4":
        cnfrm
        if cnfrm == "y":
            dlt = requests.delete(URL)
            print("status code is ", + dlt.status_code)
            print(str(dlt.status_code), "means", responses[dlt.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "5":
        cnfrm
        if cnfrm == "y":
            head = requests.head(URL)
            print("status code is ", + head.status_code)
            print(str(head.status_code), "means", responses[head.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "6":
        cnfrm
        if cnfrm == "y":
            pat = requests.patch(URL)
            print("status code is ", + pat.status_code)
            print(str(pat.status_code), "means", responses[pat.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")
    if getreq == "7":
        cnfrm
        if cnfrm == "y":
            opt = requests.options(URL)
            print("status code is ", + opt.status_code)
            print(str(opt.status_code), "means", responses[opt.status_code])
        elif cnfrm == "n":
            print("exiting..")
            exit()
        else:
            print("y for yes, n for no")

    #     For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
    # List of codes (https://github.com/waldemarnt/http-status-codes)
else:
    print("Not a valid link")

# Stretch Goals (Optional Objectives)

# Pursue stretch goals if you are a more advanced user or have remaining lab time.

#     Have your script perform authentication into api.github.com using the auth command.

#     Add timeouts to your script.

#     Add error handling to your script.
