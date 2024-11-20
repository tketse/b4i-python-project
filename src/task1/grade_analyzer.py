import pandas as pd

def load_csv(file_path):
    # Loads CSV file To dataframe #
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print('Error: File not found.')
    except pd.errors.EmptyDataError:
        print(f"{file_path} is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occured {e}")
        return None
    
    
def calculate_average(df):
    # Calculates averages from grades dataframe #
    if df is None:
        print("There is no data to analyze")
        return
    
    averages = {}
    for subject in df['subject'].unique():
        subject_data = df[df['subject'] == subject]
        avg_grade = subject_data['grade'].mean()
        max_grade = subject_data['grade'].max()
        min_grade = subject_data['grade'].min()
        passing_students = subject_data[subject_data['grade'] >= 60].shape[0]
        
        averages[subject] = {
            'average': avg_grade,
            'highest': max_grade,
            'lowest': min_grade,
            'passing': passing_students
        }
    return averages

def display_averages(averages):
    # Displays averages in readable format. #
    if not averages:
        print('No averages to display')
        return
    
    for subject, values in averages.items():
        print(f" Subject: {subject}")
        print(f" Average Grade: {values['average']:.2f}")
        print(f" Highest Grade: {values['highest']}")
        print(f" Lowest Grade: {values['lowest']}")
        print(f" Passing Students: {values['passing']}")
        print(f"-" * 40)
        

if __name__ == "__main__":
    file_path = "data/grades.csv"
    grades_df = load_csv(file_path)
    averages = calculate_average(grades_df)
    display_averages(averages)