from datetime import datetime

def fechaPublicacion():
    date_time = datetime.now()
    date_time_format = datetime.strftime(date_time, "%Y/%m/%d, %H:%M:%S")
    print(date_time_format)

    return date_time_format