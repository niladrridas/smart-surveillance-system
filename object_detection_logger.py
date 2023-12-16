import csv
import datetime

def log_data(objects):
    with open('detection_log.csv', 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'object']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        for obj in objects:
            writer.writerow({'timestamp': timestamp, 'object': obj})

# Call log_data when objects are detected
