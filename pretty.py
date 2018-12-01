#get the list of websites being checked
def get_info():
    websites = []
    with open('config.txt') as f:
        configs = f.read()
    webs = configs.split('\n')
    for web in webs:
        if web:
            websites.append(web)
    return websites

#get the data from the files
def gather():
    txtFiles = get_info()
    data = ""
    for txtfile in txtFiles:
        data_lines = []
        file = open(txtfile + ".txt", "r")
        for line in file:
            data_lines.append(line)
        file.close()
        data = data + strip(data_lines)
    return data

def strip(data):
    dns_names = []
    dns_addr = []
    dns_success = []
    html_page = ""

    for line in data:
        if line != data[0]:
            if "not" in line:
                dns_success.append("No")
            else:
                dns_success.append("Yes")
            line = line.replace("For DNS", '')
            line = line.replace(':', '')
            line = line.replace("'", '')
            line = line.replace('(IP', '')
            line = line.replace('),', '')
            line = line.replace('domain', '')
            line = line.replace('has', '')
            line = line.replace('updated to the new IP address.', '')
            line = line.replace('has ', '')
            line = line.replace('been', '')
            line = line.replace('not', '')
            word = line.split()
            dns_names.append(word[0])
            dns_addr.append(word[1])

    #checksum to ensure the dns attribute variables are the same quantity in each list
    #print(str(len(dns_names)) + " " + str(len(dns_addr)) + " " + str(len(dns_success)))
    #generate table
    try:
        html_page = data[0] + "<br/>"
    except:
        page = "empty"
    html_page += '''<table style="width:100%"><tr><th>Host</th><th>DNS Address</th><th>Update Status</th></tr>'''
    for i in range(len(dns_names)):
        if dns_names[i] != "boldandcounter.co.uk":
            print(dns_names[i] + " " + dns_addr[i] + ' ' + dns_success[i])
            html_page += "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(dns_names[i], dns_addr[i], dns_success[i])
    html_page += "</table> <br/> <br/>"

    return html_page


def pretty_main():
    pretty_txt = gather()

    #generate the txt
    file = open("pretty.txt", "w")
    file.write(pretty_txt)
    file.close()

pretty_main()
