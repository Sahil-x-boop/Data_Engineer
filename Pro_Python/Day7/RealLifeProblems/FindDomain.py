emails = ["sahil.talwar@gmail.com", "info@openai.com", "support@microsoft.com"]

domains = [email.split("@")[1] for email in emails]
print(f"Domains: {domains}")
