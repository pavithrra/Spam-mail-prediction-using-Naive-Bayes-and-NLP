import pandas as pd

def mapping_parallelize(df1):

    print("Processing ....")

    bag_of_words = []
    for index, row in df1.iterrows():
        bag_of_words = bag_of_words + row['words']
    
    bag_of_words = list(set(bag_of_words))
    column_names = ["mail_id"] + bag_of_words
    df2 = pd.DataFrame(columns= column_names)

    for index, row in df1.iterrows():
        print("Processing mail id: ", index)
        # Adding mail id
        df2_dict = dict.fromkeys(column_names,[0])
        df2_dict['mail_id'] = index
        # Populating the words columns
        for word in row['words']:
            if word in bag_of_words:
                df2_dict[word] = 1
        
        df2_row = pd.DataFrame.from_dict(df2_dict)
        df2 = df2.append(df2_row)

    df2.to_csv("test.csv", index=False, header=True)
    return df2