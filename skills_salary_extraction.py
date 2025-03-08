import pandas as pd
import re

def extract_skills(description):
    """
    Extracts specific skills from the job description.
    Customize the list of skills in the regex pattern as needed.
    """
    # The regex will match any of the listed skills (case insensitive)
    # skills = re.findall(r'\b(Python|Java|SQL|Excel|Communication|Management)\b', description, re.IGNORECASE)
    skills = re.findall(
                    r'\b('
                    r'Python|'
                    r'Machine Learning|'
                    r'Deep Learning|'
                    r'TensorFlow|'
                    r'PyTorch|'
                    r'Keras|'
                    r'Scikit-learn|'
                    r'NumPy|'
                    r'Pandas|'
                    r'Data Analysis|'
                    r'Data Visualization|'
                    r'Algorithms|'
                    r'Statistics|'
                    r'Linear Algebra|'
                    r'Probability Theory|'
                    r'Neural Networks|'
                    r'Convolutional Neural Networks \(CNN\)|'
                    r'Recurrent Neural Networks \(RNN\)|'
                    r'LSTM|'
                    r'Natural Language Processing \(NLP\)|'
                    r'Computer Vision|'
                    r'Reinforcement Learning|'
                    r'Optimization|'
                    r'Data Mining|'
                    r'Feature Engineering|'
                    r'Big Data|'
                    r'Apache Spark|'
                    r'Hadoop|'
                    r'SQL|'
                    r'NoSQL|'
                    r'Data Warehousing|'
                    r'Cloud Computing|'
                    r'AWS|'
                    r'Microsoft Azure|'
                    r'Google Cloud Platform|'
                    r'API Development|'
                    r'Model Deployment|'
                    r'Model Evaluation|'
                    r'A/B Testing|'
                    r'Experimentation|'
                    r'Software Development Lifecycle|'
                    r'Version Control \(Git\)|'
                    r'Object-Oriented Programming|'
                    r'Data Structures|'
                    r'Design Patterns|'
                    r'Agile Methodologies|'
                    r'DevOps|'
                    r'Containerization \(Docker\)|'
                    r'Kubernetes|'
                    r'Microservices|'
                    r'C\+\+|'
                    r'Java|'
                    r'R Programming|'
                    r'Julia|'
                    r'Scripting|'
                    r'Data Cleaning|'
                    r'Feature Selection|'
                    r'Hyperparameter Tuning|'
                    r'Ensemble Methods|'
                    r'Decision Trees|'
                    r'Random Forest|'
                    r'Gradient Boosting|'
                    r'XGBoost|'
                    r'LightGBM|'
                    r'CatBoost|'
                    r'Probabilistic Models|'
                    r'Bayesian Inference|'
                    r'Simulation|'
                    r'Experimental Design|'
                    r'Dimensionality Reduction|'
                    r'Principal Component Analysis \(PCA\)|'
                    r'Singular Value Decomposition \(SVD\)|'
                    r'Matrix Factorization|'
                    r'Collaborative Filtering|'
                    r'Recommender Systems|'
                    r'Transfer Learning|'
                    r'Generative Adversarial Networks \(GANs\)|'
                    r'Autoencoders|'
                    r'Time Series Analysis|'
                    r'Forecasting|'
                    r'Signal Processing|'
                    r'Speech Recognition|'
                    r'Robotics|'
                    r'Cognitive Computing|'
                    r'Ethics in AI|'
                    r'Explainable AI \(XAI\)|'
                    r'Data Privacy|'
                    r'Security|'
                    r'Edge Computing|'
                    r'Embedded Systems|'
                    r'Computer Architecture|'
                    r'Real-Time Systems|'
                    r'Distributed Systems|'
                    r'High-Performance Computing|'
                    r'Parallel Computing|'
                    r'Simulation and Modeling|'
                    r'Research Methodologies|'
                    r'Scientific Computing|'
                    r'Critical Thinking|'
                    r'Problem Solving'
                    r')\b',
                description,
                re.IGNORECASE)
    
    
    # Return unique skills
    return list(set(skills))

def get_midpoint(salary_str):
    """
    1. Searches for two dollar amounts in the string.
    2. Removes commas and converts them to floats.
    3. Returns the midpoint of the two amounts.
    """
    pattern = r"\$(\d[\d,]*)\D+\$(\d[\d,]*)"
    match = re.search(pattern, salary_str)
    if match:
        low_str, high_str = match.groups()
        low = float(low_str.replace(",", ""))
        high = float(high_str.replace(",", ""))
        return (low + high) / 2
    return None  # If no match, return None

def main():
    # Read the CSV file containing job listings.
    try:
        df = pd.read_csv('C:\\Users\\hugoa\\DSAI_MAIN\\DSAI-Group2\\DSAI-Group2\\Mini-Project\\mini_project.csv')
    except Exception as e:
        print("Error reading the CSV file:", e)
        return

    # Combine 2 cols into 'Job Description'
    df['Job Description'] = df['Responsibilities'].fillna('') + " " + df['Requirements'].fillna('')

    # Check if the expected column exists.
    if 'Job Description' not in df.columns:
        print("Error: 'Job Description' column not found in the CSV file.")
        return

    # Apply the extraction functions to each job description.
    df['Skills'] = df['Job Description'].apply(extract_skills)
    df["Mid Salary"] = df["Salary"].apply(get_midpoint)
   
    # Save the updated DataFrame to a new CSV file.
    try:
        df.to_csv('C:\\Users\\hugoa\\DSAI_MAIN\\DSAI-Group2\\DSAI-Group2\\Mini-Project\\mini_project_updated.csv', index=False)
        print("Skills and salary range have been successfully extracted and saved to 'mini_project_updated.csv'.")
    except Exception as e:
        print("Error saving the CSV file:", e)

if __name__ == '__main__':
    main()
