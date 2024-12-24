import win32evtlog

def read_usb_logs(logtype='System'):
    server = 'localhost'
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    hand = win32evtlog.OpenEventLog(server, logtype)
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    print(f"Total records in {logtype} = {total}")
    print(f"Total records in {logtype} on server {server} = {total}")
    events = []
    while True:
        event_batch = win32evtlog.ReadEventLog(hand, flags, 0)
        if not event_batch:
            break
        events.extend(event_batch)

    usb_logs = extract_usb_logs(events)
    
    if usb_logs:
        print_usb_logs(usb_logs)
    else:
        print("No USB related logs found")
    
    win32evtlog.CloseEventLog(hand)
    return usb_logs

def extract_usb_logs(events):
    usb_logs = []
    for event in events:
        try:
            if event.StringInserts:
                for insert in event.StringInserts:
                    if 'USB' in insert:
                        usb_logs.append({
                            'EventCategory': event.EventCategory,
                            'TimeGenerated': event.TimeGenerated,
                            'SourceName': event.SourceName,
                            'EventID': event.EventID,
                            'EventType': event.EventType,
                            'EventDescription': insert
                        })
        except AttributeError:
            continue
    return usb_logs

def print_usb_logs(usb_logs):
    print("USB related logs:")
    for log in usb_logs:
        print(f"Event Category: {log['EventCategory']}")
        print(f"Time Generated: {log['TimeGenerated']}")
        print(f"Source Name: {log['SourceName']}")
        print(f"Event ID: {log['EventID']}")
    print(f"Event Type: {log['EventType']}")
    print(f"Event Description: {log['EventDescription']}")
    print("-" * 20)
    print()
    print(f"Event Description: {log['EventDescription']}")
    print("-" * 20)

if __name__ == "__main__":
    read_usb_logs()
    read_usb_logs('System')

# Output: Total records in System = 38924
# Output: Daudz ieraksti

