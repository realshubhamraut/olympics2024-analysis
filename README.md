# Olympics 2024 Analysis

Interesting thing about this project is it involves creating a SQLite database from CSV files with multiple tables and establishing the connection using SQLite module. The analysis includes various visualizations and data processing steps using Python libraries such as pandas, numpy, matplotlib, seaborn, and scikit-learn.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/realshubhamraut/olympics2024-analysis.git
    cd olympics2024-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Create Database**:
    - Your can directly analyze the data using csv files but if you want to create a sqlite database, see next step.
    - Run the `create-database.py` script to create SQLite databases from the CSV files:
        ```sh
        python create-database.py
        ```

2. **Analyze Data**:
    - Open the `analysis.ipynb` Jupyter Notebook to perform data analysis and visualization:
        ```sh
        jupyter notebook analysis.ipynb
        ```
##### stars to my projects are greatly appreciated

    
---


You can pull up an issue or try to add more features to analysis based on data, it will be greatly appreciated

