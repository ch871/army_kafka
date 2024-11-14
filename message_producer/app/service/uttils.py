def check_terror_message(message: str):
    if "explo" in message:
        return "explosive"
    if "hostage" in message:
        return "hostage"
