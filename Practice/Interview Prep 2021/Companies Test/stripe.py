# Part 1

# In an HTTP request, the Accept-Language header describes the list of
# languages that the requester would like content to be returned in. The header
# takes the form of a comma-separated list of language tags. For example:

#   Accept-Language: en-US, fr-CA, fr-FR

# means that the reader would accept:

#   1. English as spoken in the United States (most preferred)
#   2. French as spoken in Canada
#   3. French as spoken in France (least preferred)

# We're writing a server that needs to return content in an acceptable language
# for the requester, and we want to make use of this header. Our server doesn't
# support every possible language that might be requested (yet!), but there is a
# set of languages that we do support. Write a function that receives two arguments:
# an Accept-Language header value as a string and a set of supported languages,
# and returns the list of language tags that will work for the request. The
# language tags should be returned in descending order of preference (the
# same order as they appeared in the header).

# In addition to writing this function, you should use tests to demonstrate that it's
# correct, either via an existing testing system or one you create.

# Examples:

# parse_accept_language(
#   "en-US, fr-CA, fr-FR",  # the client's Accept-Language header, a string
#   ["fr-FR", "en-US"]      # the server's supported languages, a set of strings
# )
# returns: ["en-US", "fr-FR"]

# parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"])
# returns: ["fr-FR"]

# parse_accept_language("en-US", ["en-US", "fr-CA"])
# returns: ["en-US"]

# Requirements
# Accept-Language header(string, {supported languages}) -> list of language tags for the request descending order of preference (the
# same order as they appeared in the header).

# Repeated case

# Part 2
# Accept-Language headers will often also include a language tag that is not
# region-specific - for example, a tag of "en" means "any variant of English". Extend
# your function to support these language tags by letting them match all specific
# variants of the language.

# Examples:

# parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"])
# returns: ["en-US"]

# parse_accept_language("fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-CA", "fr-FR"]

# parse_accept_language("fr-FR, fr", ["en-US", "fr-CA", "fr-FR"])
# returns: ["fr-FR", "fr-CA"]


def parse_accept_language(client_language_header, server_supported_language):

    accepted_language_header = []
    client_language_header_list = client_language_header.split(",")
    print(f"client language header list : {client_language_header_list}")

    for language_header in client_language_header_list:
        language_header = language_header.strip()
        if '-' in language_header:
            # check if there is hypen
            # if there is no hypen -> we want to
            for server_language_header in server_supported_language:

                if language_header == server_language_header:

                    if language_header not in accepted_language_header:
                        accepted_language_header.append(language_header)
        else:
            for server_language_header in server_supported_language:
                if match_prefix(language_header, server_language_header):
                    if server_language_header not in accepted_language_header:
                        accepted_language_header.append(server_language_header)

    print(accepted_language_header)
    return accepted_language_header


def match_prefix(client_language_header, server_supported_language):
    # client language header does not have a hyphen

    prefix = server_supported_language.split("-")[0]
    if client_language_header == prefix:
        return True

    return False


assert parse_accept_language(
    "en-US, fr-CA, fr-FR", ["fr-FR", "en-US"]) == ["en-US", "fr-FR"]

assert parse_accept_language("fr-CA, fr-FR", ["en-US", "fr-FR"]) == ["fr-FR"]

assert parse_accept_language("en-US", ["en-US", "fr-CA"]) == ["en-US"]
assert parse_accept_language("", ["en-US", "fr-CA"]) == []

assert parse_accept_language("en-US, en-US", ["en-US", "fr-CA"]) == ["en-US"]


assert parse_accept_language("en", ["en-US", "fr-CA", "fr-FR"]) == ["en-US"]

assert parse_accept_language(
    "fr", ["en-US", "fr-CA", "fr-FR"]) == ["fr-CA", "fr-FR"]

assert parse_accept_language(
    "fr, fr-FR", ["en-US", "fr-CA", "fr-FR"]) == ["fr-CA", "fr-FR"]


assert parse_accept_language(
    "fr-FR, r", ["en-US", "fr-CA", "fr-FR"]) == ["fr-FR"]


assert parse_accept_language(
    "fr-FR, r", ["en-US", "fr-CA", "fr-FR"]) == ["fr-FR"]
