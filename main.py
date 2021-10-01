import csv
import time
import os
import psutil

def french_dictionary(): #initialising french dictionary
    with open('french_dictionary.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for i in csv_reader:
            french_dict[i[0]] = [i[1],0]

def translation(ip_file): #translating to french from english
    
    fp1 = open('t8.shakespeare.translated.txt', 'w')
    check = french_dict.keys() 
    with open(ip_file, 'r') as text:
        while True:
            line = text.readline() #reads all line in the file
            if not line:
                break
            sentence = ''
            for word in line.split(): #reads words
                filtered = filter(str.isalpha,word)
                ip_word = "".join(filtered)
                if ip_word in check:
                    available = french_dict[ip_word][0]
                    french_dict[ip_word][1] += 1
                    word = word.replace(ip_word, available)
                sentence += word + ' '
            sentence = sentence.strip()
            fp1.write(sentence + '\n')
    fp1.close()
    print(f'File {input_file} is translated from english to french!!')
    return True

def frequency_csv(): # generating frequence of words in the file
    
    with open('frequency.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English', 'French', 'Frequency'])
        for i in french_dict:
            writer.writerow([i, french_dict[i][0], french_dict[i][1]])
    print('Frequency generation is completed!!')
    return True

def performance(process_time, memory_used): # calculating the performance of the program
    memory_used = psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2
    process_time = process_complete_time - process_starting_time

    with open('performance.txt', 'w') as file:
        file.write(f"Time to process : {process_time} seconds\n")
        file.write(f"Memory used : {memory_used} MB")
    print('Performance is calculated!!')

if __name__ == '__main__':
    process_starting_time = time.time()
    french_dict = {}
    ip_file = 't8.shakespeare.txt'

    if len(sys.argv) == 2:
        input_file = sys.argv[1]

    french_dictionary()
    translation(ip_file)
    frequency_csv()
    process_complete_time = time.time()
    
    performance(process_time, memory_used)