import json

companyName = input("Enter your Company Name: ")
contactEmail = input("Enter your contact E-mail: ")

while "@" not in contactEmail:
    print("Invalid email. Please enter a valid email address.")
    contactEmail = input("Enter your contact E-mail: ")

dataCollectionType = input("What type of data do we collect? ")
dataUsage = input("How is the data used? ")
dataStorageLimit = input("How long is the data stored? ")
cookieStorage = input("How long are cookies stored? ")  

privacyData = {
    "company_name": companyName,
    "contact_email": contactEmail,
    "data_collection_type": dataCollectionType,
    "data_usage": dataUsage,
    "data_storage_limit": dataStorageLimit,     
    "cookie_storage": cookieStorage 
}

# Save to JSON with UTF-8 encoding
with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacyData, file, indent=4, ensure_ascii=False)
print("All data has been successfully saved to .json!")

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Privacy Policy</title> 
</head>
<body>
    <h1>Privacy Policy for "{company_name}"</h1>
    <p>Contact: {contact_email}</p>

    <h2>What type of data do we collect?</h2>
    <p>{data_collection_type}</p>

    <h2>How is the data used?</h2>
    <p>{data_usage}</p>

    <h2>How long do we store the data?</h2>
    <p>{data_storage_limit}</p>

    <h2>How do we handle cookies?</h2>  <!-- Added cookie section -->
    <p>{cookie_storage}</p>
</body>
</html>
"""

privacy_policy = html_template.format(**privacyData)

# Save to HTML file
with open("privacy_template.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)

print("All data has been successfully saved to HTML!")
