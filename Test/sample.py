message_types = ["Warning:", "Errors:"]

t= any("error" in message_type.lower() for message_type in message_types)

print(t)