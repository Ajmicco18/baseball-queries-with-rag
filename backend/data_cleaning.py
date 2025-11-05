import pandas as pd
import os

# function to convert csv file to a Json file


def convertToJson():
    # defining the path of our directory
    directory_path = 'mlb-dataset/'

    # checking to see if the path exists and if the path is a valid directory
    if os.path.exists(directory_path) and os.path.isdir(directory_path):

        # iterating through each file in the directory
        for filename in os.listdir(directory_path):

            # creating a filepath by concatenating the directory path and the file name in the directory
            filepath = os.path.join(directory_path, filename)

            # checking to make sure the concatenated filepath is an actual file
            if os.path.isfile(filepath):
                # try catch to perform csv to json conversion
                try:
                    # stripping the directory path from the filepath name
                    new_directory = 'json-data/'

                    # creating a pandas dataframe from the filepath
                    df = pd.read_csv(filepath)

                    # converting the dataframe to a json file using pandas' to_json function and stripping the file of its .csv
                    df.to_json(os.path.join(new_directory,
                               filename.strip('.csv'))+'.json', orient='records', indent=4)

                except Exception as e:
                    # returning an exception if there is an error
                    print(f"Error reading {filename}: {e}")
        # return "hello world"
    else:
        # return "Not a directory"
        print(f"Directory '{directory_path}' not found or is not a directory.")


print(convertToJson())
