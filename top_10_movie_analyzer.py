import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/imdb.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

top_10_data = data.nlargest(10, 'popularity')

def plot_correlation_matrix():
    correlation_matrix = top_10_data.corr(numeric_only=True)
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix (Top 10 Movies)')
    plt.show()

def plot_genres_distribution():
    plt.figure(figsize=(14, 6))
    sns.countplot(y='genres', data=top_10_data, order=top_10_data['genres'].value_counts().index)
    plt.title('Distribution of Genres (Top 10 Movies)')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genres')
    plt.show()

def plot_release_year_distribution():
    plt.figure(figsize=(14, 6))
    sns.countplot(x='release_year', data=top_10_data, order=top_10_data['release_year'].value_counts().index)
    plt.title('Number of Movies Released per Year (Top 10 Movies)')
    plt.xlabel('Release Year')
    plt.ylabel('Number of Movies')
    plt.xticks(rotation=45)
    plt.show()

def plot_budget_vs_revenue():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='budget', y='revenue', data=top_10_data)
    plt.title('Budget vs. Revenue (Top 10 Movies)')
    plt.xlabel('Budget')
    plt.ylabel('Revenue')
    plt.show()

def plot_vote_avg_vs_popularity():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='vote_average', y='popularity', data=top_10_data)
    plt.title('Vote Average vs. Popularity (Top 10 Movies)')
    plt.xlabel('Vote Average')
    plt.ylabel('Popularity')
    plt.show()

def plot_budget_distribution():
    plt.figure(figsize=(10, 6))
    sns.histplot(top_10_data['budget'], bins=10, kde=True)
    plt.title('Distribution of Budget (Top 10 Movies)')
    plt.xlabel('Budget')
    plt.ylabel('Frequency')
    plt.show()

def plot_runtime_by_genre():
    plt.figure(figsize=(14, 8))
    sns.boxplot(x='runtime', y='genres', data=top_10_data, order=top_10_data['genres'].value_counts().index)
    plt.title('Runtime by Genre (Top 10 Movies)')
    plt.xlabel('Runtime (minutes)')
    plt.ylabel('Genres')
    plt.show()

def plot_pairplot():
    sns.pairplot(top_10_data[['budget', 'revenue', 'popularity', 'vote_average']])
    plt.suptitle('Pairplot of Budget, Revenue, Popularity, and Vote Average (Top 10 Movies)', y=1.02)
    plt.show()

def plot_genre_pie_chart():
    genre_counts = top_10_data['genres'].value_counts()
    plt.figure(figsize=(10, 10))
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Movies by Genre (Top 10 Movies)')
    plt.show()


def show_summary_statistics():
    print(top_10_data.describe())

# Menu to choose analysis for top 10 movies
def analysis_menu():
    while True:
        print("\nSelect the analysis you want to perform:")
        print("1. Correlation Matrix")
        print("2. Genres Distribution (Bar Chart)")
        print("3. Movies Released per Year (Bar Chart)")
        print("4. Budget vs Revenue (Scatter Plot)")
        print("5. Vote Average vs Popularity (Scatter Plot)")
        print("6. Budget Distribution (Histogram)")
        print("7. Runtime by Genre (Boxplot)")
        print("8. Pairplot of Key Numerical Variables")
        print("9. Proportion of Movies by Genre (Pie Chart)")
        print("10. Summary Statistics")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            plot_correlation_matrix()
        elif choice == '2':
            plot_genres_distribution()
        elif choice == '3':
            plot_release_year_distribution()
        elif choice == '4':
            plot_budget_vs_revenue()
        elif choice == '5':
            plot_vote_avg_vs_popularity()
        elif choice == '6':
            plot_budget_distribution()
        elif choice == '7':
            plot_runtime_by_genre()
        elif choice == '8':
            plot_pairplot()
        elif choice == '9':
            plot_genre_pie_chart()
        elif choice == '10':
            show_summary_statistics()
        elif choice == '11':
            print("Exiting the menu.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 11.")


        print("\n\n\n") 
        another = input("Do you want to perform another analysis? (yes/no): ").strip().lower()
        if another != 'yes':
            print("Session ended.")
            break


analysis_menu()