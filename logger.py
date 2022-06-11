file_name = "log.txt"

def operations_logger(error, result_string, result):
    with open (file_name, 'a') as file:
        string_to_file = "Error: " + result_string + '\n' if error else result_string + str(result) +'\n'
        file.write(string_to_file)

operations_logger(False, 'a + b = ', -5)        
    
