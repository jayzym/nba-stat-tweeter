import twitter
api = twitter.Api(consumer_key="1hOfhqwYDvXnbkz5kgwkCPPiq",
    consumer_secret="1hOfhqwYDvXnbkz5kgwkCPPiq",
    access_token_key="2923921738-tLmv9IMqOyCtpDPCvMxwF2iqdIB9LJEQoQ4l26k",
    access_token_secret="q2PPaGt24cHw5feyTq7BiMaHQ43NJHTVaN2O7fVYuguaM")

def main():
    try:
        status = api.PostUpdate('test')
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)

    print("{0} just posted: {1}".format(status.user.name, status.text))


if __name__ == "__main__":
    main()
