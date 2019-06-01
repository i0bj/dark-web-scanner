def main():

    parser = argparse.ArgumentParser("This program will scan the dark web for any specified content")

    parser.add_argument("-k", "--keyword", help="This will search for any search term ex: 'John Doe")
    args = parser.parse_args()

    global keyword

    keyword = args.keyword

    # Use 'AND' for explicit results
    # This will query the Dark Search API for information found on the dark web.
    api_prefix = "https://darksearch.io/api/search"
    query = {"query": keyword,
              "page": 1,
             }

    def tor_crawl():

        def update_progress(job_title, progress):
            length = 20 # modify this to change the length
            block = int(round(length*progress))
            msg = "\r{0}: [{1}] {2}%".format(job_title, "#"*block + "-"*(length-block), round(progress*100, 2))
            if progress >= 1: msg += " DONE\r\n"
            sys.stdout.write(msg)
            sys.stdout.flush()

        for i in range(100):
            time.sleep(0.1)
            update_progress("Scanning DeepWeb for " + keyword, i/100.0)
        update_progress(keyword, 1)

        url_response = requests.get(api_prefix, params=query)
        data = url_response.json()
        # Changed header from generic Python header
        url_response.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        if url_response.status_code != 200:
            print("[-] Can't access the Deep Web")
        elif data["total"] == 0:
            print("No results found on the Deep Web")
        elif data["total"] >= 1:
            print("Results found, please check email.")
            # gmail_password = input("Type your password and press enter: ")
            port = 587 # smtp port
            smtp_server = "smtp.gmail.com"
            sender_email = "Enter your email address here"  # sending address
            gmail_password = "If you want a hardcoded password, do not recommend" # Hard coded password
            receiver_email = "Enter the receiving email" # Enter the address you want to receive the email
            subject = "Enter the email subject here"
            message = "Enter"

            eml = MIMEMultipart()
            eml["From"] = sender_email
            eml["To"] = receiver_email
            eml["Subject"] = subject

            eml.attach(MIMEText(message, "plain"))

            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, gmail_password)
            text = eml.as_string()
            server.sendmail(sender_email, receiver_email, text)

    tor_crawl()


main()
